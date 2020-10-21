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
    AM = Squirrel.objects.filter(shift="AM")
    PM = Squirrel.objects.filter(shift="PM")
    Adult = Squirrel.objects.filter(age="Adult")
    Juven = Squirrel.objects.filter(age="Juvenile")
    AbGr = Squirrel.objects.filter(location="Above Ground")
    GrPl =Squirrel.objects.filter(location="Ground Plane")
    Gray = Squirrel.objects.filter(primary_fur_color="Gray")
    Cinnamon = Squirrel.objects.filter(primary_fur_color="Cinnamon")
    Black = Squirrel.objects.filter(primary_fur_color="Black")
    Run = Squirrel.objects.filter(running="TRUE")
    Cha = Squirrel.objects.filter(chasing="TRUE")
    Cli = Squirrel.objects.filter(climbing="TRUE")
    Eat = Squirrel.objects.filter(eating="TRUE")
    For = Squirrel.objects.filter(foraging="TRUE")

        
    context = {
            'squirrels' : squirrels,
            'AM': AM,
            'PM' : PM,
            'Adult' : Adult,
            'Juven' : Juven,
            'AbGr' : AbGr,
            'GrPl' : GrPl,
            'Gray' : Gray,
            'Cinnamon' : Cinnamon,
            'Black' : Black,
            'Run' : Run,
            'Cha' : Cha,
            'Cli' : Cli,
            'Eat' : Eat,
            'For' : For,
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
