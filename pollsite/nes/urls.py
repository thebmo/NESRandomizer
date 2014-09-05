from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.random_game, name='random'),
    # url(r'^(\?selections\=<selection>\s+$)', views.random, name='random'),
    )