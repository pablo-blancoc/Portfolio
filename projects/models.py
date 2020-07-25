from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, default="default")
    short = models.CharField(max_length=100, default="default")
    description = models.TextField(default="default")
    technology1 = models.CharField(max_length=20, default="default")
    technology2 = models.CharField(max_length=20, default="default")
    technology3 = models.CharField(max_length=20, default="default")
    link_text = models.CharField(max_length=20, default='default')
    link = models.URLField(default='default')
    image = models.FilePathField(path='/img', default="default")