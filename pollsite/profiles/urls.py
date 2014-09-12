from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.view_profile, name='view_profile'),
    url(r'^owned_games/', views.edit_owned_games, name='owned'),
    url(r'^beaten_games/', views.edit_beaten_games, name='beaten'),
    )