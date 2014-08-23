from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    rating = models.FloatField(default=0)
    votes = models.IntegerField(default=0)