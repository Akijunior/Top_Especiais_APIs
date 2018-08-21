from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from users.models import Author


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
    thumb = models.ImageField(verbose_name='Imagem representativa',
                              upload_to='core/images', default='book.png', blank=True, null=True)
    score_average = models.DecimalField(decimal_places=2, validators=[
            MaxValueValidator(10.0), MinValueValidator(0.0)], max_digits=4, default=0.0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', )


class Score(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='scores')
    lector = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='scores', default=1,
                               null=True, blank=True)
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


def post_save_reply(created, instance, **kwargs):
    book = Book.objects.get(pk=instance.book.pk)
    Score.objects.exclude(pk=instance.pk).filter(lector=instance.lector.pk, book=book.pk).delete()
    amount = book.scores.count()
    total_score = 0
    for score in book.scores.all():
        total_score += score.score
    book.score_average = total_score/amount
    book.save()



def book_save_reply(created, instance, **kwargs):
    authors = instance.authors.all()
    for i in range(len(authors)):
        authors[i].books.add(instance)
        authors[i].save()

models.signals.post_save.connect(
    post_save_reply, sender=Score, dispatch_uid='post_save_reply'
)

models.signals.post_save.connect(
    book_save_reply, sender=Book, dispatch_uid='book_save_reply'
)

