import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    body = models.TextField(max_length=1000)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title
