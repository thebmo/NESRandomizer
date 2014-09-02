from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.views import generic

from django.contrib.auth import authenticate



# class IndexView(generic.ListView):
    # template_name = 'mysite/index.html'

def index(request):
    user = authenticate(username='', password='')
    if user is not None:
        # verifies user
        if user.is_active:
           return render(request, 'mysite/index.html', {'user':user})
        
    return render(request, 'mysite/index.html',)

def login(request):
    return render(request, 'mysite/login.html',)