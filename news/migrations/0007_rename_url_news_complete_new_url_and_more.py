# Generated by Django 4.1.6 on 2023-04-22 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_news_img_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='url',
            new_name='complete_new_url',
        ),
        migrations.RemoveField(
            model_name='news',
            name='img_link',
        ),
        migrations.AddField(
            model_name='news',
            name='new_img_url',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
    ]
