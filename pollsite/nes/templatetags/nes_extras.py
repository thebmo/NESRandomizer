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
#127.0.0.1:8000/admin/nes/ownedgame/add/ params: a dict of parameters                #
# games_owned: a list of owned game objects   #
# returns a filters list of game objects      #
# ******************************************* #
def filter_games(all_games, params, games_owned):
    
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
        
        # start testing crap
        print '\nPARAMS:'
        for param in params['genres']:
            print param
        print '\n'
        # end testing crap
        
        for game in all_games:
            print '%s: %s' % (game.title, game.genre.lower())
            if game in games and game.genre.lower() not in params['genres']:
                games.remove(game)
                # print 'removing: %s' % game.title
    
    # # checks if user set the beaten filter
    if params['beaten'] != 'both':
        beaten = (False if params['beaten']  == 'yes' else True)
        # if params['beaten'] == 'yes':
        for game in all_games:
            for owned in games_owned:
                if game in games and game.id == owned.game_id and owned.beaten == beaten:
                    games.remove(game)
    
    
    
    # return (games if games else None)
    return games