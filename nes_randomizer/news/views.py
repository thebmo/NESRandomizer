from django.shortcuts import render
from .models import NewsPost

# Lists out all posts in descending order
def index(request):
    template = 'news/index.html'
    posts = list(NewsPost.objects.all())
    posts.reverse()
    
    return render(request, template, {'posts': posts})