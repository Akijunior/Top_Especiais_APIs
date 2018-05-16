from django.db import models


# Create your models here.
class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name='nome', max_length=200, unique=True)
    release_date = models.DateTimeField()
    game_category = models.CharField(max_length=200)
    played = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Jogo'
        ordering = ('name',)
