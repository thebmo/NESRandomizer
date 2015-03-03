from django.shortcuts import render, redirect
# from nes.templatetags import nes_extras as NES
from reports.templatetags import reports_extras as NES

# index of performable actions
def index(request):
    
    if request.user.is_staff:
        most_owned = NES.fetch_most_owned()
        most_beaten = NES.fetch_most_beaten()
        template = 'reports/index.html'
        return render(request, template, {'most_owned': most_owned, 'most_beaten': most_beaten})

    else:
        return redirect('index')
        