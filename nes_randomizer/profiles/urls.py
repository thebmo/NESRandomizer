from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.view_profile, name='view_profile'),
    url(r'^owned_games/', views.edit_games, name='owned'),
    url(r'^beaten_games/', views.edit_games, name='beaten'),
    url(r'^update_email/', views.edit_field, name='email'),
    url(r'^update_password/', views.edit_field, name='password'),
    )