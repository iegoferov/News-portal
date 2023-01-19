from news.models import *

1. Создать двух пользователей (с помощью метода User.objects.create_user('username')).
u1 = User.objects.create_user('Вася')
u2 = User.objects.create_user('Петя')

2. Создать два объекта модели Author, связанные с пользователями.
au1 = Author.objects.create(user=u1)
au2 = Author.objects.create(user=u2)

3. Добавить 4 категории в модель Category.

Category.objects.create(category_name='Спорт')
Category.objects.create(category_name='Искусство')
Category.objects.create(category_name='Здоровье')
Category.objects.create(category_name='Путешествие')

4. Добавить 2 статьи и 1 новость.
Post.objects.create(post_topic='Обзор фигурного катания', post_text='sdfsdfsdf sdf sdf sdfwerwe dsf h sdfhusiudfh sdfuyh
g isduf sdiufh isudf isudfh sidufh sdufh sdufh suidfh siudfh sidf uhsdifuh sidufh sidufh sdf iuh', author_id=3, position='AR
T')
Post.objects.create(post_topic='Еда в поезде', post_text='sdfsdfsdf sdf sdf sdfwerwe dsf h sdfhusiudfh sdfuyhg isduf sdi
ufh isudf isudfh sidufh sdufh sdufh suidfh siudfh sidf uhsdifuh sidufh sidufh sdf iuh', author_id=3, position='NEW')

Post.objects.create(post_topic='Результаты соревнований', post_text='sdfsdfsdf sdf sdf sdfwerwe dsf h sdfhusiudfh sdfuyh
g isduf sdiufh isudf isudfh sidufh sdufh sdufh suidfh siudfh sidf uhsdifuh sidufh sidufh sdf iuh', author_id=4, position='AR
T')

5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
PostCategoty.objects.create(post=Post.objects.get(id=4), category=Category.objects.get(id=5))
PostCategoty.objects.create(post=Post.objects.get(id=4), category=Category.objects.get(id=6))
PostCategoty.objects.create(post=Post.objects.get(id=5), category=Category.objects.get(id=7))
PostCategoty.objects.create(post=Post.objects.get(id=5), category=Category.objects.get(id=8))
PostCategoty.objects.create(post=Post.objects.get(id=6), category=Category.objects.get(id=5))

6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
Comment.objects.create(comment_post=Post.objects.get(id=4), comment_user=u1, text_comment='Очень хороший пост')
Comment.objects.create(comment_post=Post.objects.get(id=4), comment_user=u2, text_comment='Очень плохой пост')
Comment.objects.create(comment_post=Post.objects.get(id=5), comment_user=u2, text_comment='Нормально')
Comment.objects.create(comment_post=Post.objects.get(id=6), comment_user=u1, text_comment='Пойдет')

7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
Post.objects.get(id=4).like()
>>> Post.objects.get(id=4).like()
>>> Post.objects.get(id=5).like()
>>> Post.objects.get(id=6).dislike()
>>> Post.objects.get(id=6).dislike()
>>> Comment.objects.get(id=6).like()
>>> Comment.objects.get(id=7).dislike()
>>> Comment.objects.get(id=7).dislike()
>>> Comment.objects.get(id=8).like()
>>> Comment.objects.get(id=8).like()
>>> Comment.objects.get(id=9).like()
>>> Comment.objects.get(id=9).dislike()

8. Обновить рейтинги пользователей.
Author.objects.get(id=3).update_rating()
Author.objects.get(id=4).update_rating()

9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
a = Author.objects.order_by('-rating')[:1]
a[0].id  #3
a[0].user.username   #'Вася'

10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
p = Post.objects.order_by('-rating')
p[0].time, p[0].author.user.username, p[0].rating, p[0].post_topic, p[0].preview()

# (datetime.datetime(2023, 1, 19, 12, 12, 30, 96146, tzinfo=datetime.timezone.utc), 'Вася', 2, 'Обзор фигурного катания', 'sdf
sdfsdf sdf sdf sdfwerwe dsf h sdfhusiudfh sdfuyhg isduf sdiufh isudf isudfh sidufh sdufh sdufh suidfh siudfh sidf uhsdifuh s
idufh sidufh sdf iuh')

11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
Comment.objects.filter(comment_post_id=p[0].id).values('time', 'comment_user_id', 'rating', 'text_comment')


