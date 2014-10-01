from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^games/(?P<game_id>\d+)', views.game_details, name='details'),
    url(r'^games/', views.search_games, name='games'),
    url(r'^random/', views.random_game, name='random'),
    )