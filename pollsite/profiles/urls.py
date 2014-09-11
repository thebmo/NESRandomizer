from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.view_profile, name='view_profile'),
    # url(r'^random/', views.random_game, name='random'),
    )