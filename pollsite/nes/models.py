from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    rating = models.FloatField(default=0)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ('title',)
    
class OwnedGame(models.Model):
    game=models.ForeignKey(Game)
    user=models.ForeignKey(User)
    # title = game.title
    
    class Meta:
        ordering = ('game',)