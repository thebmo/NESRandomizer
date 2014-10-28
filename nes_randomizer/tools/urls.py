from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^users', views.users, name='users'),
    url(r'^delete/(?P<user_id>\d+)', views.delete_user, name='delete'),
    
    )