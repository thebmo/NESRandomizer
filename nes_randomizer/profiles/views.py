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

# handles the editing of beaten or owned games in the profile
def edit_games(request):
    # redirects if not logged in
    if not request.user.is_authenticated():
        return redirect('index',)
        
    template = 'profiles/edit_games.html'
    
    
    print "path: %s" % request.path
    if 'owned_games' in request.path:
        mode = 'owned'
        title = ['Edit Your Owned Games', 'Unowned', 'Owned']
    else:
        mode = 'beaten'
        title = ['Edit Your Beaten Games', 'Not Beaten', 'Beaten']
    
    # This block handles the updates
    # if 'Owned' in request.POST or 'Unowned' in request.POST:
    if title[1] in request.POST or title[2] in request.POST:
        if title[1] in request.POST:
            game_ids = request.POST.getlist(title[1])
            for game_id in game_ids:
                if mode == 'owned':
                    g = OwnedGame(game_id=game_id, user_id=request.user.id)
                else:
                    g = BeatenGame(game_id=game_id, user_id=request.user.id)
                    
                g.save()
        
        if title[2] in request.POST:
            game_ids = request.POST.getlist(title[2])
            for game_id in game_ids:
                if mode == 'owned':
                    OwnedGame.objects.filter(game_id=game_id, user_id=request.user.id).delete()
                else:
                    BeatenGame.objects.filter(game_id=game_id, user_id=request.user.id).delete()
        
        
        redirect_url = ':'.join(('prof', mode))
        return redirect(redirect_url,)
    # end of update block
    
    
    # creates a list of just owned game ids
    mode_ids = []
    if mode == 'owned':
        for game in NES.fetch_owned(request):
            mode_ids.append(game.game_id)
    else:   
        for game in NES.fetch_beaten(request):
            mode_ids.append(game.game_id)
    
    all_games = NES.fetch_games(request)
    games = []
    mode_games = []
    
    # poplulates the two lists
    for game in all_games:
        if game.id in mode_ids:
            mode_games.append(game)
        else:
            games.append(game)

    return render(request, template,{'title':title, 'games':games, 'mode_games':mode_games})
    
    