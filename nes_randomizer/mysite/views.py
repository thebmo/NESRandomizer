from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.views import generic

from django.contrib.auth import authenticate, logout, login

from nes.models import Game


# class IndexView(generic.ListView):
    # template_name = 'mysite/index.html'

# clear this view after
def import_games(request):
    file = 'C:\\Users\\bmo\\Desktop\\nes_parsed.txt'
    with open(file, 'r') as f:
        for line in f.readlines():
            game = line.replace('\n', '').split('|')
        
            g = Game(title=game[0], year=game[1],publisher=game[2],
                region=game[3], format=game[4], license=game[5], genre=game[6])
            g.save()
    return redirect('profiles/view_profile.html')
    
def index(request):
    user = authenticate(username='', password='')
    if user is not None:
        # verifies user
        if user.is_active:
           return render(request, 'mysite/index.html', {'user':user})
        
    return render(request, 'mysite/index.html',)

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