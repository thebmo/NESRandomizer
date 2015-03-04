from django.shortcuts import render, redirect
# from nes.templatetags import nes_extras as NES
from reports.templatetags import reports_extras as REP

# index of performable actions
def index(request):
    
    most_owned = REP.fetch_most(owned=True)
    most_beaten = REP.fetch_most(beaten=True)
    genre_owned = REP.fetch_most(owned=True, genre=True)
    genre_beaten = REP.fetch_most(beaten=True, genre=True)
    
    template = 'reports/index.html'
    
    return render(request, template, {'most_owned': most_owned, 'most_beaten': most_beaten,'genre_beaten':genre_beaten, 'genre_owned': genre_owned})


# Most owned by Genre
def genres(request):
    
    genre_owned = REP.fetch_most(owned=True, genre=True)
    genre_beaten = REP.fetch_most(beaten=True, genre=True)
    template = 'reports/most_beaten_owned_genres.html'
    
    return render(request, template, {'genre_beaten':genre_beaten, 'genre_owned': genre_owned})

        