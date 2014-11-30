from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from . templatetags import tools_extras as TOOLS
from nes.templatetags import nes_extras as NES
from nes.models import *
from news.models import NewsPost
from news import forms as NEWS

# Create your views here.

def new_post(request):
    template = 'tools/news_update.html'
    news_form = NEWS.NewsPostForm
    return render( request, template, {'news_form': news_form})

# loads a user's profile
def lookup_user(request, user_id):
    print 'test'
    template = 'tools/profile.html'
    user = User.objects.get(pk=user_id)
    beaten = NES.fetch_beaten(user)
    owned = NES.fetch_owned(user)
    for beat in beaten:
        print beat.title
    return render(request, template, { 'user':user, 'beaten':beaten, 'owned':owned })


# index of performable actions
def index(request):
    if request.user.is_staff:
        template = 'tools/index.html'
        return render(request, template,)
    else:
        return redirect('index')


# User listing
def users(request):
    if request.user.is_staff:
        template = 'tools/list_users.html'
        users = list(User.objects.all())
        users.remove(users[0])

        return render(request, template, { 'users':users })
    else:
        return redirect('index')


# deletes the passed user
def delete_user(request, user_id):
    if request.user.is_staff:
        user = User.objects.get(pk=user_id)
        TOOLS.delete_user(user)
        
        return redirect('/tools/users/')
    else:
        return redirect('index')