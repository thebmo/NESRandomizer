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
        selection = request.GET['selection']
        beaten = request.GET['beaten']
        genres = request.GET.getlist('genre')

        # params = {        
            # 'selection' : request.GET['selection'],
            # 'beaten' : request.GET['beaten'],
            # 'genres' : request.GET.getlist('genre'),
            # }
        all_games = Game.objects.all()
        games_owned = OwnedGame.objects.filter(user_id=request.user.id)
        games = [] # this is the final selection of games
        
        if selection == 'owned':
            for game in all_games:
                for owned in games_owned:
                    if game.id == owned.game_id:
                        games.append(game)

        random_game = (random.choice(games) if games else random.choice(all_games))

        game_url= str(random_game.title).replace(' ','+')
        # remove my_games, beaten owned genres after testing done        
        return render(request, template_name, {'games':random_game, 'selection':selection, 'beaten':beaten, 'genres':genres, 'game_url':game_url})
    return render(request, template_name,)