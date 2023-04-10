from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
from django.core.cache import cache
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy

class Author(models.Model): # Модель, содержащая объекты всех авторов
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    def __str__(self):
        return f'{self.user}'
    def update_rating(self):
        #суммарный рейтинг каждой статьи автора;
        au_post_rat = self.post_set.aggregate(author_post_rating=Sum('rating'))
        sum_au_post_rat = 0
        sum_au_post_rat += au_post_rat.get('author_post_rating')

        #суммарный рейтинг всех комментариев автора
        au_comment_rat = self.user.comment_set.aggregate(author_comment_rating=Sum('rating'))
        sum_au_comment_rat = 0
        sum_au_comment_rat += au_comment_rat.get('author_comment_rating')

        #суммарный рейтинг всех комментариев к статьям автора
        sum_post_comm_rat = 0
        for post in self.post_set.all():
            rat = post.comment_set.aggregate(post_comment_rating=Sum('rating'))
            if rat.get('post_comment_rating'):
                sum_post_comm_rat += rat.get('post_comment_rating')

        self.rating = sum_au_post_rat * 3 + sum_au_comment_rat + sum_post_comm_rat
        self.save()

class Category(models.Model): # Категории новостей/статей
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.category_name}'

class Post(models.Model): #модель должна содержать в себе статьи и новости, которые создают пользователи
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    article = 'ART'
    news = 'NEW'
    POSITIONS = [(article, 'статья'), (news, 'новость')]
    position = models.CharField(max_length=3, choices=POSITIONS, default='-')
    time = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategoty')
    post_topic = models.CharField(max_length=255, default='Тут мог быть заголовок', help_text=_('post_topic'))
    post_text = models.TextField(default='Тут мог быть текст')
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.post_text[0:255]

    def __str__(self):
        return f'{self.post_topic.title()}: {self.time} :{self.rating}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'product-{self.pk}')  # затем удаляем его из кэша, чтобы сбросить его
class PostCategoty(models.Model): #Промежуточная модель для связи «многие ко многим»:
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )

