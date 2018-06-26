from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    books = models.ManyToManyField('books.Book')
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    auth_profile = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Lector(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    lector_profile = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
