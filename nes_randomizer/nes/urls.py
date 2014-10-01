from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^games/(?P<id>\d+)', views.search_games, name='gamedeets'),
    url(r'^games/', views.search_games, name='games'),
    url(r'^random/', views.random_game, name='random'),
    )