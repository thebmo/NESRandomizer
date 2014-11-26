import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.CharField(max_length=1000)
    
    def __unicode__(self):
        return self.title