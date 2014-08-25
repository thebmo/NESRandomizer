from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
#testestse
# class IndexView(generic.ListView):
    # template_name= 'nes/index.html'
def index(request):
    return render(request, 'nes/index.html',)