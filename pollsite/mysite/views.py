from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse as response, Http404
from django.template import RequestContext, loader

def home(request):
    return response("Hey this is totally the home page...")