from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django import forms
from . templatetags import tools_extras as TOOLS
from nes.templatetags import nes_extras as NES
from nes.models import *
from news.models import NewsPost
from news import forms as NEWS

# Create your views here.

# new post page
def new_post(request):
    if request.user.is_staff:
        template = 'tools/news_update.html'
        news_form = NEWS.NewsPostForm(initial={'user': request.user.id})
        
        if request.POST:
            if request.POST['title'] != '' and request.POST['body'] != '':
                p = NewsPost(title=request.POST['title'], body=request.POST['body'], user_id=request.user.id)
                p.save()
        
        return render( request, template, {'news_form': news_form})

    else:
        return redirect('index')


# loads a user's profile
def lookup_user(request, user_id):
    template = 'tools/profile.html'
    user = User.objects.get(pk=user_id)
    beaten = NES.fetch_beaten(user)
    owned = NES.fetch_owned(user)

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