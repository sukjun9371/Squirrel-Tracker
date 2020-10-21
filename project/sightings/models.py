from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):
    latitude = models.DecimalField(
            max_digits=17,
            decimal_places=15,
            help_text=_('Latitude of the squirrel'),
            default=0,
            )

    longitude = models.DecimalField(
            max_digits=16,
            decimal_places=14,
            help_text=_('Longitude of the squirrel'),
            )

    unique_squirrel_id = models.CharField(
            max_length=14,
            help_text=_('unique ID of the squirrel'),
            primary_key=True,
            )

    hectare = models.CharField(
            max_length = 3,
            help_text=_('combination of one axis that runs N-S (01~42) + another axis that runs E-W (A-I)'),
            blank=True,
            default="",
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
            default=Pm,
            )

    date = models.DateField(
            help_text=_('Date when you saw the squirrel'),
            default=None,
            blank=True,
            null=True,
            )


    hectare_squirrel_number = models.IntegerField(
            blank=True,
            default="1",
            )

    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Unknown = 'unknown'

    AGE_CHOICES = [
            (Adult,_('Adult')),
            (Juvenile,_('Juvenile')),
            (Unknown,_('unknown')),
            ]

    age = models.CharField(
            max_length=20,
            help_text=_('your guess: how old was the squirrel?'),
            choices=AGE_CHOICES,
            default=Adult,
             )


    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    Black = 'Black'

    COLOR_CHOICES = [
            (Gray,_('Gray')),
            (Cinnamon, _('Cinnamon')),
            (Black, _('Black')),
            ]

    primary_fur_color = models.CharField(
            max_length=15,
            help_text=_('primary fur color of the squirrel seen'),
            choices=COLOR_CHOICES,
            blank=True,
            )

    highlight_fur_color = models.CharField(
            max_length = 20,
            blank = True,
          default = ""
            )

    def combination_color(self):
        return self.primary_fur_color + self.hightlight_fur_color

    color_notes = models.CharField(
            blank=True,
            max_length=160,
            default = ""
            )

    Ground_Plane = 'Ground Plane'
    Above_Ground = 'Above Ground'

    LOC_CHOICES = [
            (Ground_Plane,_('Ground Plane')),
            (Above_Ground,_('Above Ground')),
            ]

    location = models.CharField(
            blank=True,
            max_length=15,
            choices=LOC_CHOICES,
            )

    def above_ground_sighter(self):
        if self.location == 'Ground Plane':
            return False

    specific_location = models.CharField(
            blank=True,
            max_length = 120,
            default=""
            )

    TRUE = 'TRUE'
    FALSE = 'FALSE'

    BOOLEAN_CHOICES = [
            (TRUE,_('TRUE')),
            (FALSE,_('FALSE')),
            ]

    running = models.CharField(
            blank=True,
            max_length = 10,
            choices = BOOLEAN_CHOICES,
            default=FALSE,
            help_text=_('Was the squirrel running?'),
            )

    chasing = models.CharField(
            blank=True,
            max_length = 10,
            choices = BOOLEAN_CHOICES,
            default=FALSE,
            help_text=_('Was the squirrel chasing something?'),
            )


    climbing = models.CharField(
            blank=True,
            max_length = 10,
            choices = BOOLEAN_CHOICES,
            default=FALSE,
            help_text=_('Was the squirrel climbing?'),
            )


    eating = models.CharField(
            blank=True,
            max_length = 10,
            choices = BOOLEAN_CHOICES,
            default=FALSE,
            help_text=_('Was the squirrel eating?'),
            )

    foraging = models.CharField(
            blank=True,
            max_length = 10,
            choices = BOOLEAN_CHOICES,
            default=FALSE,
            help_text=_('Was the squirrel foraging?'),
            )

    other_activities = models.CharField(
            blank=True,
            max_length=160,
            default=""
            )

    kuks = models.CharField(
            blank=True,
            max_length = 10,
            choices = BOOLEAN_CHOICES,
            default=FALSE,
            help_text=_('Squirrel was heard kukking, a chirpy vocal communication used for a variety of reasons.'),
            )

    quaas = models.CharField(
            blank=True,
            max_length = 10,
            choices = BOOLEAN_CHOICES,
            default=FALSE,
            help_text=_('Squirrel was heard quaaing, an elongated vocal communication which can indicate the presence of a ground predator such as a dog.'),
            )

    moans = models.CharField(
            blank=True,
            max_length = 10,
            choices = BOOLEAN_CHOICES,
            default=FALSE,
            help_text=_('Squirrel was heard moaning, a high-pitched vocal communication which can indicate the presence of an air predator such as a hawk.'),
            )

    tail_flags = models.CharField(
            blank=True,
            max_length = 10,
            choices = BOOLEAN_CHOICES,
            default=FALSE,
            help_text=_("Squirrel was seen flagging its tail. Flagging is a whipping motion used to exaggerate squirrel's size and confuse rivals or predators. Looks as if the squirrel is scribbling with tail into the air." ),
            )

    tail_twitch = models.CharField(
            blank=True,
            max_length = 10,
            choices = BOOLEAN_CHOICES,
            default=FALSE,
            help_text=_("Squirrel was seen twitching its tail. Looks like a wave running through the tail, like a breakdancer doing the arm wave. Often used to communicate interest, curiosity."),
            )

    approaches = models.CharField(
            blank=True,
            max_length = 10,
            choices = BOOLEAN_CHOICES,
            default=FALSE,
            help_text=_("Squirrel was seen approaching human, seeking food."),
            )

    indifferent = models.CharField(
            blank=True,
            max_length = 10,
            choices = BOOLEAN_CHOICES,
            default=FALSE,
            help_text=_("Squirrel was indifferent to human presence."),
            )

    runs_from = models.CharField(
            blank=True,
            max_length = 10,
            choices = BOOLEAN_CHOICES,
            default=FALSE,
            help_text=_("Squirrel was seen running from humans, seeing them as a threat."),
            )

    other_interactions = models.CharField(
            blank=True,
            max_length=120,
            default=""
            )

    def lat_long(self):
        return (self.latitude, self.longitude)


    def __str__(self):
        return self.unique_squirrel_id





# Create your models here.
