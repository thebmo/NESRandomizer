from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^users', views.users, name='users'),
    url(r'^new_post', views.new_post, name='new_post'),
    url(r'^delete/(?P<user_id>\d+)', views.delete_user, name='delete'),
    url(r'^user/(?P<user_id>\d+)', views.lookup_user, name='profile'),
    
    )