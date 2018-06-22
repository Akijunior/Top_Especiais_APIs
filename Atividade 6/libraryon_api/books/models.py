from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Book(models.Model):
    AGE_RANGE = (
        ('F', 'Free'),
        ('FT', '+14'),
        ('ST', '+16'),
        ('ET', '+18'),
    )
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    isbn = models.CharField(max_length=20)
    edition = models.CharField(max_length=20)
    year = models.IntegerField()
    amount_pages = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    age_range = models.CharField(max_length=2, choices=AGE_RANGE, default='F')
    authors = models.ManyToManyField('users.Author')
    genres = models.ManyToManyField('Genre')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', )


class Score(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    lector = models.ForeignKey('users.Lector', on_delete=models.CASCADE)
    score = models.DecimalField(decimal_places=2, validators=[
            MaxValueValidator(10.0), MinValueValidator(0.0)], max_digits=4)
    comment = models.CharField(max_length=200, blank=True)
    evaluation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Livro: " + str(self.book.title) + "Nota: " + str(self.score)

    class Meta:
        ordering = ('score', )


class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
