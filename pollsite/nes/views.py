from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *
import random
from . import forms
from .templatetags import nes_extras as NES

# Create your views here.

# class IndexView(generic.ListView):
    # template_name= 'nes/index.html'

def index(request):
    template_name= 'nes/index.html'
    return render(request, template_name,)

def random_game(request):
    template_name = 'nes/random.html'
    
    if 'selection' in request.GET:       
        params = {        
            'selection' : request.GET['selection'],
            'beaten' : request.GET['beaten'],
            'genres' : request.GET.getlist('genre'),
            }
        all_games = Game.objects.all()
        
        
        # sets the games owned argument for NES.filter_games()
        games_owned = {}
        if params['selection'] == 'owned':
            games_owned = OwnedGame.objects.filter(user_id=request.user.id)
            
        random_game = random.choice(NES.filter_games(all_games, params, games_owned))

        game_url= str(random_game.title).replace(' ','+')
      
        return render(request, template_name, {'game':random_game, 'selection':params['selection'], 'beaten':params['beaten'], 'genres':params['genres'], 'game_url':game_url})
    return render(request, template_name,)