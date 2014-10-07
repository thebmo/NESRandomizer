from django import template
from nes.models import *

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# fetches all games in the DB
def fetch_games(request):
    return Game.objects.all()

# fetches owned games for the user
def fetch_owned(request):
    return OwnedGame.objects.filter(user_id=request.user.id)

# fetches beaten games for the user
def fetch_beaten(request):
    return BeatenGame.objects.filter(user_id=request.user.id)

# returns a google search link to be used in templates
def create_google_url(game):
    return (''.join(('https://www.google.com/#q=nes+', str(game.title).replace(' ','+'))))

# creates and returns a string for searching api's
def create_search_string(game):
    return (''.join(('nes+', str(game.title).replace(' ','+'))))
    
    
# ******************************************* #
# filter_games()                              #
# filters all games by passed in filters from #
# random.html form arguments                  #
# games: a list of game objects               #
# params: a dict of parameters                #
# games_owned: a list of owned game objects   #
# beaten_games: a list of beaten game objects #
# returns a filters list of game objects      #
# ******************************************* #
def filter_games(all_games, params, games_owned, beaten_games):
    
    games = list(all_games)

    # removes games that user does not own if an argument
    if params['selection'] == 'owned':
        
        for game in all_games:
            not_owned = True
            for owned in games_owned:
                if game.id == owned.game_id:
                    not_owned = False
                    break
            if not_owned:
                games.remove(game)

    # removes games that don't match the genre if selected
    if params['genres']:
        
        # # start testing crap
        # print '\nPARAMS:'
        # for param in params['genres']:
            # print param
        # print '\n'
        # # end testing crap
        
        for game in all_games:
            if game in games and game.genre not in params['genres']:
                games.remove(game)
                # print 'removing: %s' % game.title
    
    # checks if user set the beaten filter
    if params['beaten'] != 'both':
        beaten = (True if params['beaten']  == 'yes' else False)
        # if params['beaten'] == 'yes':
        for game in all_games:

            # beaten filter = true, remove games that are not on list
            if beaten:
                beat = False
                for beaten_game in beaten_games:
                    if game.id == beaten_game.game_id:
                        beat = True
                if game in games and not beat:
                    games.remove(game)
                    
            # beaten filter = false, remove games taht are on list
            if not beaten:
                beat = False
                for beaten_game in beaten_games:
                    if game in games and game.id == beaten_game.game_id:
                        games.remove(game)
                
    
    
    return games
# end filter_games() #