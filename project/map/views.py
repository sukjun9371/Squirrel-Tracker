from django.shortcuts import render
from django.http import HttpResponse
from sightings.models import Squirrel

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
            }

    return render(request,'map/index.html', context)
# Create your views here.
