from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    publication_datetime = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    complete_new_url = models.URLField(default='')
    country = models.CharField(max_length=50)
    new_img_url = models.URLField()
