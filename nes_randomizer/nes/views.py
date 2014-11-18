from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *
import random
from . import forms
from .templatetags import nes_extras as NES


# Create your views here.
def game_details(request, game_id):
    template = 'nes/game_details.html'
    game = Game.objects.get(id=game_id)
    game_url = NES.create_google_url(game)
    game_search = NES.create_search_string(game)
    amazon_game = NES.fetch_from_amazon(game)
    desc = NES.fetch_game_html(game)
    videos = NES.fetch_game_videos(game)
    return render(request, template, {'game': game, 'game_url': game_url, 'game_search': game_search, 'amazon_game': amazon_game, 'desc': desc, 'videos': videos})


def search_games(request):
    template = 'nes/search_games.html'
    errors = []

    # the search box
    if request.POST:
        games = []

        # title search
        G = Game.objects.filter(title__icontains=request.POST['q'])
        for g in G:
            if g not in games:
                games.append(g)

        # genre search
        G = Game.objects.filter(genre__icontains=request.POST['q'])
        for g in G:
            if g not in games:
                games.append(g)

        # publisher search
        G = Game.objects.filter(publisher__icontains=request.POST['q'])
        for g in G:
            if g not in games:
                games.append(g)

        # year search
        G = Game.objects.filter(year__icontains=request.POST['q'])
        for g in G:
            if g not in games:
                games.append(g)

        if not games:
            errors.append('No games found that match this search.')
    else:
        games = Game.objects.all()
    return render(request, template, {'errors': errors, 'games': games})


# the index view
def index(request):
    template = 'nes/index.html'

    return render(request, template,)


# The random game generator view
def random_game(request):
    template = 'nes/random.html'
    errors = []
    # debug = True
    debug = False

    if 'selection' in request.POST:
        params = {
            'selection': request.POST['selection'],
            'beaten': request.POST['beaten'],
            'genres': request.POST.getlist('genre'),
            }
        all_games = Game.objects.all()
        games_owned = {}
        beaten_games = {}
        game_url = ''
        game_search = ''

        # sets the games owned argument for NES.filter_games()
        if params['selection'] == 'owned':
            games_owned = OwnedGame.objects.filter(user_id=request.user.id)

        if params['beaten'] != 'both':
            beaten_games = BeatenGame.objects.filter(user_id=request.user.id)

        random_game = NES.filter_games(all_games, params, games_owned, beaten_games)
        if random_game:
            random_game = random.choice(random_game)
            game_url = NES.create_google_url(random_game)
            game_search = NES.create_search_string(random_game)

        else:
            errors.append('No games match this criteria. Remove some filters!')

        return render(request, template, {'game': random_game, 'selection': params['selection'], 'beaten': params['beaten'], 'genres': params['genres'], 'game_url': game_url, 'errors': errors, 'debug': debug})
    return render(request, template,)
