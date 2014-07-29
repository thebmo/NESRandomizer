from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse as response, Http404
from django.template import RequestContext, loader

from .models import Poll

# Create your views here.
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = RequestContext(request, { 'latest_poll_list': latest_poll_list, })

    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/details.html', {'poll': poll})

def results(request, poll_id):
    return response("You're looking at the resolts of poll %s" % poll_id)

def vote(request, poll_id):
    return response("You're voting on poll %s" % poll_id)