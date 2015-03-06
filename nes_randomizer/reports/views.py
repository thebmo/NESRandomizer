from django.shortcuts import render, redirect
from nes.templatetags.nes_extras import fetch_game
from reports.templatetags import reports_extras as REP

# index of performable actions
def index(request):
    
    most_owned = REP.fetch_most(owned=True)
    most_beaten = REP.fetch_most(beaten=True)
    genre_owned = REP.fetch_most(owned=True, genre=True)
    genre_beaten = REP.fetch_most(beaten=True, genre=True)
    
    template = 'reports/index.html'
    
    template_vars = {
        'most_owned': most_owned, 
        'most_beaten': most_beaten,
        'genre_beaten':genre_beaten,
        'genre_owned': genre_owned
        }
    
    return render(request, template, template_vars)


# Most owned by Genre
def genres(request):
    
    template = 'reports/most_beaten_owned_genres.html'
    genre_owned = REP.fetch_most(owned=True, genre=True)
    genre_beaten = REP.fetch_most(beaten=True, genre=True)
    
    return render(request, template, {'genre_beaten':genre_beaten, 'genre_owned': genre_owned})


# Most owned but unbeaten games
def unbeaten(request):
    template = 'reports/most_owned_unbeaten.html'
    
    # 3 dicts total: owned, user_beaten, beaten
    owned_dict = REP.fetch_most(owned=True, all=True)
    user_beaten_dict = REP.fetch_most(beaten=True, all=True)
    
    # Creates an updated dict of beaten games including unbeaten titles
    # Also sents owned to 0 if someone has beaten a game they do not
    # own
    beaten_dict = {k:0 for k in owned_dict}
    for k in user_beaten_dict:
        if k not in owned_dict:
            owned_dict[k] = 0
        beaten_dict[k] = user_beaten_dict[k]    

    # Builds out the stats list for the template
    stats = []
    for k in owned_dict:
        diff = abs(owned_dict[k]-beaten_dict[k])
        if diff != 0 and owned_dict[k] != 0:
            diff_percent = "{0:.2f}".format((diff/float(owned_dict[k]) * 100))
        else: diff_percent = 0
        stats.append(
            [
                fetch_game(k, title=True),         # title
                k,                                 # id
                owned_dict[k],                     # owned count
                beaten_dict[k],                    # beaten count
                diff,                              # absolute difference
                diff_percent                       # percent difference
                ]
            )
    
    # Sorts stats by ABS difference, then returns only 25 items
    stats = sorted(stats, reverse=True, key = lambda x: x[4])
    stats = stats[:25]   
    
    return render(request, template, {'stats': stats})