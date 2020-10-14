from django.urls import path

from . import views


app_name = 'sightings'

urlpatterns = [
        path('',views.index),
        path('<str:unique_squirrel_id>/',views.detail, name='detail'),
        path('add/',views.add),
        path('stats/',views.stats),
        ]


