# Generated by Django 4.1.6 on 2023-04-21 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_img_link_alter_news_publication_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='img_link',
        ),
    ]
