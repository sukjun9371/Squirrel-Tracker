from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Squirrel



def index(request):
    squirrels =  Squirrel.objects.all()
    context = {
            'squirrels' : squirrels,
            }

    return render(request,'sightings/index.html',context)

def detail(request,unique_squirrel_id):
    squirrel = get_object_or_404(Squirrel, pk=unique_squirrel_id)
    context = {
           'squirrel': squirrel,
            }
    return render(request,'sightings/detail.html',context)

  
def add(request):
    return render(request,'sightings/add.html')

def stats(request):
    return render(request,'sightings/stats.html')

# Create your views here.
