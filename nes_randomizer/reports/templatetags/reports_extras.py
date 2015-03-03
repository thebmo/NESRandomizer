from collections import Counter
from nes.models import *
from nes.templatetags.nes_extras import get_genres


# Gets the total number of games beaten/owned from all users
def total_games(beaten=False, owned=False):
    # Chooses the correct operation based on params
    if beaten:
        games = BeatenGame.objects.all()
    elif owned:
        games = OwnedGame.objects.all()
    else:
        return 0
    
    return len(games)


# Returns a list of top 10 or x games beaten or owned
def fetch_most(count=10, beaten=False, owned=False, genre=False):
    # 0 title/string - 1 count - 2 game id/pk
    top = []
    
    # dict of tallied games owned
    # 'gameid': tally_count
    total = {}
    
    # Chooses the correct operation based on params
    if beaten:
        games = BeatenGame.objects.all()
    elif owned:
        games = OwnedGame.objects.all()
    else:
        return []
    
    
    # Handles the top <count> games
    if (beaten or owned) and not genre:
        for game in games:
            if str(game.game_id) not in total:
                total[str(game.game_id)] = 1
            else:
                total[str(game.game_id)] += 1

        c = Counter(total)
        c = c.most_common()[:count] # <<<<< x is a int value

        for item in c:
            game = Game.objects.get(pk=int(item[0]))
            top.append([game.title, item[1], int(item[0])])
    
    # Handles the Genre reports
    if genre:
        genres = {}
        for game in games:
            game_genre = Game.objects.get(pk=game.game_id).genre
            if game_genre not in genres:
                genres[game_genre]=1
            else:
                genres[game_genre]+=1
        
        # A list of lists containing key/values of genres/counts as a %
        top = [
            [
                k,
                float("{0:.2f}".format( v / float(len(games)) * 100)), # this was to calculate percentages
                v
            ] for k, v in genres.items()
        ]
            
    return top