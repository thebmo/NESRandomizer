from django.shortcuts import render
from .models import NewsPost


# Lists out all posts in descending order
def index(request):
    template = 'news/index.html'
    posts = list(NewsPost.objects.all())
    posts.reverse()
    template_vars = {
        'posts': posts
        }

    return render(request, template, template_vars)
