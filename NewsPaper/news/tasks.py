from celery import shared_task
from django.template.loader import render_to_string
from NewsPaper import settings
from django.core.mail import EmailMultiAlternatives
import datetime
from news.models import Post, User


@shared_task
def send_message(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_create_email.html',
        {'text': preview,
         'link': f'http://127.0.0.1:8000/news/{pk}'},
    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@shared_task
def my_job():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=1)
    posts = Post.objects.filter(time__gte=last_week)
    categories = set(posts.values_list('post_category', flat=True))
    subscribers = []
    for category in categories:
        subscribers += User.objects.filter(subscriptions__category=category)
    subscribers = set([s.email for s in subscribers])
    html_content = render_to_string(
        'daily_post.html',
        {'link': 'http://127.0.0.1:8000',
         'posts': posts,
         }
    )
    msg = EmailMultiAlternatives(
        subject= 'Список новостей за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()