from django.shortcuts import render, redirect
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


# deletes the passed in post
def delete_post(request, post_id):
    template = 'news/news_view.html'
    if request.user.is_staff:
        print 'test'
        return redirect('news:index')
    else:
        return redirect('news:index')
    return render(request, template, )