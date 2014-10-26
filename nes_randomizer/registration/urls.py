from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.register, name='register'),
    url(r'^$', views.delete_user, name='delete'),
    )

