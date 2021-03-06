from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views import generic
from nes.models import *
from nes.templatetags import nes_extras as NES
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password

# views below


# updates either email or password using the PATH
def edit_field(request):
    field = ''
    template = 'profiles/edit_field.html'
    errors = []
    notes = ''

    if 'password' in request.path:
        field = 'password'
    elif 'email' in request.path:
        field = 'email'

    # if you are updating, run below instead!
    user = User.objects.get(id=request.user.id)

    if 'email' in request.POST or 'new_pass' in request.POST:
        if 'email' in request.POST:
            if User.objects.filter(email__iexact=request.POST['email']):
                errors.append(('Email \'%s\' already registered.' % request.POST['email']))
            else:
                user.email = request.POST['email']
                user.save()
                notes = 'Email updated successfully to: %s' % user.email

        elif 'new_pass' in request.POST:
            if check_password(request.POST['password'], user.password):
                print 'password is good!'

                if request.POST['new_pass'] == request.POST['conf_pass']:
                    user.password = make_password(request.POST['new_pass'])
                    user.save()
                    notes = 'Password updated successfully'
                else:
                    errors.append('Passwords do not match.')
            else:
                errors.append('Current password invalid')
    template_vars = {
        'field': field,
        'errors': errors,
        'notes': notes
        }

    return render(request, template, template_vars)


# the profile view
def view_profile(request):
    if not request.user.is_authenticated():
        return redirect('index',)
    template = 'profiles/view_profile.html'
    errors = []

    email = request.user.email
    update_email = False

    # game info
    owned = NES.fetch_owned(request.user)
    beaten = NES.fetch_beaten(request.user)
    template_vars = {
        'email': email,
        'owned': owned,
        'beaten': beaten
        }

    return render(request, template, template_vars)


# handles the editing of beaten or owned games in the profile
def edit_games(request):

    # redirects if not logged in
    if not request.user.is_authenticated():
        return redirect('index',)

    template = 'profiles/edit_games.html'
    template_vars = {}

    # sets editing mode owned/beaten
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

        redirect_url = 'prof:view_profile'
        return redirect(redirect_url,)
    # end of update block

    # creates a list of just owned game ids
    if mode == 'owned':
        mode_games = NES.fetch_owned(request.user)

    else:
        mode_games = NES.fetch_beaten(request.user)

    all_games = NES.fetch_games()
    games = []

    # # poplulates the two lists
    for game in all_games:
        if game not in mode_games:
            games.append(game)

    template_vars = {
        'title': title,
        'games': games,
        'mode_games': mode_games
        }

    return render(request, template, template_vars)
