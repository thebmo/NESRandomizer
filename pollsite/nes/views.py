from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *
import random
from . import forms

# Create your views here.

# class IndexView(generic.ListView):
    # template_name= 'nes/index.html'

def index(request):
    template_name= 'nes/index.html'
    return render(request, template_name,)

def random_game(request):
    template_name = 'nes/random.html'
    if 'selection' in request.GET:
        s = request.GET['selection']

        # if s == 'all':
        all_games = random.choice(Game.objects.all())
        genres = request.GET.getlist('genre')
        game_url= str(all_games.title).replace(' ','+')
        
        id = request.user.id
        games_owned = OwnedGame.objects.filter(user_id=id)
        
        owned = False
        beaten = False
        for game in games_owned:
            if all_games.id == game.game_id:
                owned = True
                beaten = game.beaten
                
            return render(request, template_name, {'games':all_games, 'genres':genres, 'game_url':game_url, 'owned':owned, 'beaten':beaten})
    return render(request, template_name,)