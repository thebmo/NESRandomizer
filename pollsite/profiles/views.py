from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from nes.models import *
from nes.templatetags import nes_extras as NES

# views below

def view_profile(request):
    if not request.user.is_authenticated():
        return redirect('index',)
    template = 'profiles/view_profile.html'
    errors = []
    
    email= request.user.email
    update_email= False
    # if request.POST['email'].lower() != email.lower():
        # update_email = True
    
    # game info
    owned = NES.fetch_owned(request)
    beaten = NES.fetch_beaten(request)
    games = NES.fetch_games(request)
    
    return render(request, template, {'email':email, 'owned':owned, 'beaten':beaten, 'games':games })
    
def update_email(request):
    return redirect('view_profile')

def edit_owned_games(request):
    if not request.user.is_authenticated():
        return redirect('index',)
    template = 'profiles/edit_games.html'
    title = ['Edit Your Owned Games', 'Unowned', 'Owned']
    
    all_games = NES.fetch_games(request)
    
    # creates a list of just owned game ids
    owned_ids = []
    for game in NES.fetch_owned(request):
        owned_ids.append(game.game_id)
    
    games = []
    owned_games = []
    
    # poplulates the two lists
    for game in all_games:
        if game.id in owned_ids:
            owned_games.append(game)
        else:
            games.append(game)
    
    return render(request, template,{'title':title, 'games':games, 'owned_games':owned_games})
    
def edit_beaten_games(request):
    if not request.user.is_authenticated():
        return redirect('index',)
    template = 'profiles/edit_games.html'
    title = 'Edit Your Beaten Games'
    return render(request, template,{'title':title})
    