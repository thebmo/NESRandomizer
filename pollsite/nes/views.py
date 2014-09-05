from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *
import random
from . import forms

# Create your views here.

# class IndexView(generic.ListView):
    # template_name= 'nes/index.html'


def random_game(request):
    template = 'nes/random.html'
    if 'selection' in request.GET:
        s = request.GET['selection']
        if s == 'all':
            games = random.choice(Game.objects.all())
            game_url= str(games.title).replace(' ','+')
            genres = request.GET.getlist('genre')
            
            id = request.user.id
            games_owned = OwnedGame.objects.filter(user_id=id)
            
            owned = False
            for game in games_owned:
                if games.id == game.game_id:
                    owned = True
                
            return render(request, template, {'games':games, 'genres':genres, 'game_url':game_url, 'owned':owned})
    return render(request, template,)