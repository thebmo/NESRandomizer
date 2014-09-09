from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
    
# ******************************************* #
# filter_games()                              #
# filters all games by passed in filters from #
# random.html form arguments                  #
# games: a list of game objects               #
# params: a dict of parameters                #
# games_owned: a list of owned game objects   #
# returns a filters list of game objects      #
# ******************************************* #
def filter_games(all_games, params, games_owned):
    
    games = list(all_games)
    print '\nall games:'
    for game in games:
        print game.title
        
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
        for game in all_games:
            if game.genre not in params['genres']:
                games.remove(game)
    
    # checks if user set the beaten filter
    if params['beaten'] != 'both':
    
    
    
    return games if games else None