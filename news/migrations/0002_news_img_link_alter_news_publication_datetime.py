# Generated by Django 4.1.6 on 2023-04-21 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='img_link',
            field=models.URLField(default=None),
        ),
        migrations.AlterField(
            model_name='news',
            name='publication_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
