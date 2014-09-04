from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic

from django.contrib.auth import authenticate, logout, login


# Create your views here.
def register(request):
    if request.user.is_authenticated():
        return redirect('index',)
    error=''
    username=''
    password=''
     
    return render(request, 'registration/register.html',)