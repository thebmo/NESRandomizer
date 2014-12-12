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
    if request.user.is_staff:
        post = NewsPost.objects.get(pk=post_id)
        post.delete()
        print '%s deleted post: %s' % (request.user.username, post_id)
        return redirect('news:index')
    else:
        return redirect('news:index')

# updates the passed in post
def update_post(request, post_id):
    if request.user.is_staff:
        template = 'news/news_update.html'
        post = NewsPost.objects.get(pk=post_id)
        template_vars = {
            'post': post,
            }

        return render(request, template, template_vars)
    else:
        return redirect('news:index')