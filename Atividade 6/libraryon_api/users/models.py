from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    books = models.ManyToManyField('books.Book')


class Lector(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
