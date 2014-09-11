from django.shortcuts import render, get_object_or_404
from django.views import generic
from nes.models import *


# views below

def edit_profile(request):
    template = 'profiles/edit_profile.html'
    errors = []
    return render(request, template,)