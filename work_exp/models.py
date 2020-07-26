from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(default='default name', max_length=10)
    position = models.CharField(default='default position', max_length=25)
    description = models.CharField(default='default description', max_length=150)
    start_date = models.CharField(default='start date', max_length=15)
    end_date = models.CharField(default='end date', max_length=15)
    logo = models.FilePathField(path='/img', default="default")