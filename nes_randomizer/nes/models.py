from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=200, unique=True)
    publisher = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    year = votes = models.IntegerField(default=0)
    region = models.CharField(max_length=200)
    format = models.CharField(max_length=200)
    license = models.CharField(max_length=200)
    rating = models.FloatField(default=0)
    votes = models.IntegerField(default=0)
    description = models.TextField(max_length=2000)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class BeatenGame(models.Model):
    game = models.ForeignKey(Game)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ('game',)
        unique_together = ['game', 'user']


class OwnedGame(models.Model):
    game = models.ForeignKey(Game)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ('game',)
        unique_together = ['game', 'user']
