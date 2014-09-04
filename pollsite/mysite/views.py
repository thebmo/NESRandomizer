from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.views import generic

from django.contrib.auth import authenticate, logout, login



# class IndexView(generic.ListView):
    # template_name = 'mysite/index.html'

def index(request):
    user = authenticate(username='', password='')
    if user is not None:
        # verifies user
        if user.is_active:
           return render(request, 'mysite/index.html', {'user':user})
        
    return render(request, 'mysite/index.html',)

def login_view(request):
    error=''
    username=''
    password=''
    
    if 'username' in request.GET:
        username=request.GET['username']
        password=request.GET['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'mysite/index.html',)
        error = 'Login Failed'    
    return render(request, 'mysite/login.html', {'error':error, 'username':username, 'password':password, })

def logout_view(request):
    logout(request)
    # return redirect('mysite/index.html',)
    return render(request, 'mysite/index.html',)