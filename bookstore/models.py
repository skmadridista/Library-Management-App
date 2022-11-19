from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100,default='anonymous')
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)


    def __str__(self):
        return self.title