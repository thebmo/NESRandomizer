from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *
# from random import randrange as rand
import random
from . import forms

# Create your views here.

# class IndexView(generic.ListView):
    # template_name= 'nes/index.html'

    
def index(request):
    if 'selection' in request.GET:
        s = request.GET['selection']
        if s == 'all':
            games = random.choice(Game.objects.all())
            # game = random.choice(games)
            game_url= str(games.title).replace(' ','+')
            genres = request.GET.getlist('genre')
        
            return render(request, 'nes/test.html', {'games':games, 'genres':genres, 'game_url':game_url})
    return render(request, 'nes/index.html',)
