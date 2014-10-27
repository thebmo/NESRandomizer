from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.db import IntegrityError
from .templatetags import registration_extras as REG

# Create your views here.

def delete_user(request):
    user = User.objects.get(id=request.user.id)
    REG.delete_user(user)
    return redirect('index',)
    

# user registration page
def register(request):
    if request.user.is_authenticated():
        return redirect('index',)
    error=''
    if 'username' in request.POST:
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        first_name=''
        last_name=''
        if 'first_name' in request.POST:
            first_name=request.POST['first_name']
        if 'last_name' in request.POST:
            last_name=request.POST['last_name']
        
        # checks if username or email already taken
        if User.objects.filter(username__iexact = username):
            error='Username \'%s\' unavailable.' % username
            return render(request, 'registration/register.html', {'error':error})
        elif email and User.objects.filter(email__iexact = email):
            error='Email \'%s\' already in use.' % email
            return render(request, 'registration/register.html', {'error':error})
        else:
            user= User.objects.create_user(username, email, password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index',)
            
    
    
    return render(request, 'registration/register.html',)