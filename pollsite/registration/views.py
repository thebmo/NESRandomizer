from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.db import IntegrityError


# Create your views here.
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
        
        if email and User.objects.filter(email=email).count() > 0:
            error='Email \'%s\' already in use.' % email
            return render(request, 'registration/register.html', {'error':error})
        
        try:
            user= User.objects.create_user(username, email, password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index',)
        
        except IntegrityError as e:
            if 'username' in e.message:
                error='Username \'%s\' unavailable.' % username
                
            return render(request, 'registration/register.html', {'error':error})
            
    
    
    return render(request, 'registration/register.html',)