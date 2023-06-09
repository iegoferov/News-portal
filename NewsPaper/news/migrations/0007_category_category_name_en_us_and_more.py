# Generated by Django 4.1.5 on 2023-04-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_remove_category_subscribers_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_name_en_us',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_ru',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_text_en_us',
            field=models.TextField(default='Тут мог быть текст', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_text_ru',
            field=models.TextField(default='Тут мог быть текст', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_topic_en_us',
            field=models.CharField(default='Тут мог быть заголовок', help_text='post_topic', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_topic_ru',
            field=models.CharField(default='Тут мог быть заголовок', help_text='post_topic', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_topic',
            field=models.CharField(default='Тут мог быть заголовок', help_text='post_topic', max_length=255),
        ),
    ]
