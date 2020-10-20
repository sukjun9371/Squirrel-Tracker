from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse

from .forms import AddRequestForm

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
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels' : squirrels,
            }
    return render(request,'sightings/stats.html',context)

def create(request):
    if request.method == 'POST':
        form = AddRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'sightings/add.html')
        else:
            return JsonResponse({'errors':form.errors},status=400)
    return redirect(request,'sightings/add.html')

def update(request,unique_squirrel_id):

    squirrel = get_object_or_404(Squirrel, pk=unique_squirrel_id)
    context = {
            'squirrel' : squirrel,
            }

    if request.method == 'POST':
        squirrel.latitude = request.POST['latitude']
        squirrel.longitude = request.POST['longitude']
        squirrel.shift = request.POST['shift']
        squirrel.date = request.POST['date']
        squirrel.age = request.POST['age']
        squirrel.save()
        return render(request, 'sightings/detail.html', context)

    else:
        return render(request,'sightings/update.html', context)


#Create your views here.
