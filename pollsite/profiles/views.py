from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from nes.models import *
from nes.templatetags import nes_extras as NES

# views below

def view_profile(request):
    if not request.user.is_authenticated():
        return redirect('index',)
    template = 'profiles/view_profile.html'
    errors = []
    
    email= request.user.email
    update_email= False
    # if request.POST['email'].lower() != email.lower():
        # update_email = True
    
    # game info
    owned = NES.fetch_owned(request)
    beaten = NES.fetch_beaten(request)
    games = NES.fetch_games(request)
    
    return render(request, template, {'email':email, 'owned':owned, 'beaten':beaten, 'games':games })
    
def update_email(request):
    return redirect('view_profile')