from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth import authenticate, logout, login

from news.models import NewsPost
# from nes.models import Game
from reports.templatetags import reports_extras as REP


# class IndexView(generic.ListView):
    # template_name = 'mysite/index.html'

# 404 view
def fourohfour(request):
    template = 'mysite/404.html'
    return render(request, template, )


# clear this view after
# def import_games(request):
    # file = 'C:\\Users\\bmo\\Desktop\\nes_parsed.txt'
    # with open(file, 'r') as f:
        # for line in f.readlines():
            # game = line.replace('\n', '').split('|')
        
            # g = Game(title=game[0], year=game[1],publisher=game[2],
                # region=game[3], format=game[4], license=game[5], genre=game[6])
            # g.save()
    # return redirect('profiles/view_profile.html')


# index view
def index(request):
    most_owned = REP.fetch_most_owned()
    most_beaten = REP.fetch_most_beaten()
    user = authenticate(username='', password='')
    post = []
    if NewsPost.objects.all():
        post = list(NewsPost.objects.all())[-1]
    # post.reverse()
    # post=post[0]
    if user is not None:
        # verifies user
        if user.is_active:
           return render(request, 'mysite/index.html', {'user':user, 'most_owned': most_owned, 'most_beaten': most_beaten, 'post': post})
        
    return render(request, 'mysite/index.html', {'most_owned': most_owned, 'most_beaten': most_beaten, 'post': post})

def login_view(request):
    
    # if user is logged in, redirects to index
    if request.user.is_authenticated():
        return redirect('index',)
    error=''
    username=''
    password=''
    
    # if user is logging in
    if 'username' in request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index',)
        error = 'Login Failed'    
    return render(request, 'mysite/login.html', {'error':error, 'username':username, 'password':password, })

def logout_view(request):
    logout(request)
    return redirect('index',)