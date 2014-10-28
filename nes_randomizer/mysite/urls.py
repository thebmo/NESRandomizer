from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/', views.login_view, name='login'),
    url(r'^import/', views.import_games, name='import'), #remove this after
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^nes/', include('nes.urls', namespace='nes')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^register/', include('registration.urls', namespace='reg')),
    url(r'^profiles/', include('profiles.urls', namespace='prof')),
    url(r'^tools/', include('tools.urls', namespace='tools')),
    url(r'^admin/', include(admin.site.urls), name='admin'),
)
