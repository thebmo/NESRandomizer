from django.shortcuts import render, redirect
# from nes.templatetags import nes_extras as NES
from reports.templatetags import reports_extras as REP

# index of performable actions
def index(request):
    
    if request.user.is_staff:
        most_owned = REP.fetch_most(owned=True)
        most_beaten = REP.fetch_most(beaten=True)
        template = 'reports/index.html'
        return render(request, template, {'most_owned': most_owned, 'most_beaten': most_beaten})

    else:
        return redirect('index')


# test
def genres(request):
    
    if request.user.is_staff:
        most_owned = REP.fetch_most(owned=True, genre=True)
        # most_beaten = REP.fetch_most(beaten=True)
        template = 'reports/most_beaten_owned_genres.html'
        return render(request, template, {'most_owned': most_owned})

    else:
        return redirect('index')
        