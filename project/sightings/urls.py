from django.urls import path

from . import views


app_name = 'sightings'

urlpatterns = [
        path('',views.index, name="sightings"),
        path('add/',views.add, name="add" ),
        path('stats/',views.stats, name="stats"),
        path('create/',views.create, name="create"),
        path('<str:unique_squirrel_id>/',views.detail, name='detail'),
        path('<str:unique_squirrel_id>/update/', views.update, name='update'),
        ]


