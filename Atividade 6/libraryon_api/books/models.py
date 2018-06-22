from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    isbn = models.CharField(max_length=20)
    edition = models.CharField(max_length=20)
    year = models.IntegerField()
    amount_pages = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    authors = models.ManyToManyField('users.Author')
    genres = models.ManyToManyField('Genre')


class Score(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    lector = models.ForeignKey('users.Lector', on_delete=models.CASCADE)
    score = models.DecimalField(decimal_places=2, validators=[
            MaxValueValidator(10.0), MinValueValidator(0.0)], max_digits=4)
    comment = models.CharField(max_length=200, blank=True)
    evaluation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)


class Genre(models.Model):
    AGE_RANGE = (
        ('F', 'Free'),
        ('FT', '+14'),
        ('ST', '+16'),
        ('ET', '+18'),
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    age_range = models.CharField(max_length=2, choices=AGE_RANGE, default='F')