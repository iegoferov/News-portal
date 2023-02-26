from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from .models import PostCategoty, Subscription
from NewsPaper import settings
from .tasks import send_message

# def send_message(preview, pk, title, subscribers):
#     html_content = render_to_string(
#         'post_create_email.html',
#         {'text': preview,
#          'link': f'http://127.0.0.1:8000/news/{pk}'},
#     )
#     msg = EmailMultiAlternatives(
#         subject=title,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers,
#     )
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()

@receiver(m2m_changed, sender=PostCategoty)
def post_created(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.post_category.all()
        subscribers = []
        for category in categories:
            subscribers += User.objects.filter(subscriptions__category=category)
        subscribers = [s.email for s in subscribers]
        send_message.delay(instance.preview(), instance.pk, instance.post_topic, subscribers)




