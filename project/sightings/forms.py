from django.forms import ModelForm

from .models import Squirrel

class AddRequestForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = [
                'latitude',
                'longitude',
                'unique_squirrel_id',
                'shift',
                'date',
                'age',
                'primary_fur_color',
                'location',
                'specific_location',
                'running',
                'chasing',
                'climbing',
                'eating',
                'foraging',
                'other_activities',
                'kuks',
                'quaas',
                'moans',
                'tail_flags',
                'tail_twitch',
                'approaches',
                'indifferent',
                'runs_from',
                'other_interactions',
                ]

       
