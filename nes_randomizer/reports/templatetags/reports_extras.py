from collections import Counter
from nes.models import *


# returns a list of top 10 or x games beaten
def fetch_most_beaten(count=10):
    # 0 title/string - 1 count - 2 game id/pk
    top_beaten = []
    
    # dict of tallied games owned
    total_beaten = {}
    beaten = BeatenGame.objects.all()

    for beat in beaten:
        if str(beat.game_id) not in total_beaten:
            total_beaten[str(beat.game_id)] = 1
        else:
            total_beaten[str(beat.game_id)] += 1

    c = Counter(total_beaten)
    c = c.most_common()[:10] # <<<<< x is a int value
    for item in c:
        game = Game.objects.get(pk=int(item[0]))
        top_beaten.append([game.title, item[1], int(item[0])])

    return top_beaten


# returns a list of top 10 or x games owned
def fetch_most_owned(count=10):
    # 0 title/string - 1 count - 2 game id/pk
    top_owned = []
    
    # dict of tallied games owned
    total_owned = {}
    owned = OwnedGame.objects.all()

    for own in owned:
        if str(own.game_id) not in total_owned:
            total_owned[str(own.game_id)] = 1
        else:
            total_owned[str(own.game_id)] += 1

    c = Counter(total_owned)
    c = c.most_common()[:10] # <<<<< x is a int value
    for item in c:
        game = Game.objects.get(pk=int(item[0]))
        top_owned.append([game.title, item[1], int(item[0])])

    return top_owned