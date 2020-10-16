from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):
    lattitude = models.DecimalField(
            max_digits=17,
            decimal_places=15,
            help_text=_('Lattitude of the squirrel'),
            )

    longitude = models.DecimalField(
            max_digits=16,
            decimal_places=14,
            help_text=_('Longitude of the squirrel'),
            )

    unique_squirrel_id = models.CharField(
            max_length=14,
            help_text=_('unique ID of the squirrel'),
            )

    Am = 'AM'
    Pm = 'PM'

    SHIFT_CHOICES = [
            (Am,_('AM')),
            (Pm,_('PM')),
            ]

    shift = models.CharField(
            max_length=10,
            help_text=_('AM or PM'),
            choices=SHIFT_CHOICES,
            default=Am,
            )

    date = models.DateField(
            help_text=_('Date when you saw the squirrel'),
            )

    Adult = 'adult'
    Juvenile = 'juvenile'
    Unknown = 'unknown'

    AGE_CHOICES = [
            (Adult,_('adult')),
            (Juvenile,_('juvenile')),
            (Unknown,_('unknown')),
            ]

    age = models.CharField(
            max_length=20,
            help_text=_('your guess: how old was the squirrel?'),
            choices=AGE_CHOICES,
             )

    Gray = 'gray'
    Black = 'black'
    Cinnamon = 'cinnamon'
    Unknown = 'unknown'

    FUR_CHOICES = [
            (Gray,_('gray')),
            (Black,_('black')),
            (Cinnamon,_('cinnamon')),
            (Unknown,_('unknown')),
            ]

    primary_fur_color = models.CharField(
            max_length=10,
            help_text=_('Primary fur color of the squirrel'),
            choices=FUR_CHOICES,
            default=Unknown,
            )


    def __str__(self):
        return self.unique_squirrel_id




# Create your models here.
