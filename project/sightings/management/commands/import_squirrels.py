import csv

from django.core.management.base import BaseCommand

from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Get squirrels into pot'
    
    def add_arguments(self,parser):
        parser.add_argument('squirrels_file', help='file containing squirrel details')

    def handle(self, *args, **options):
        file_ = options['squirrels_file']
        
        with open(file_) as fp:
            reader = csv.DictReader(fp)

            for item in reader:
               obj = SquirrelDetail()
               obj.latitude =item['Y']
               obj.longitude = item['X']
               obj.unique_squirrel_id = item['Unique Squirrel ID']
               obj.hectare = item['Hectare']
               obj.shift = item['Shift']
               obj.date = item['Date']
               obj.hectare_squirrel_number = item['Hectare Squirrel Number']
               obj.age = item['Age']
               obj.primary_fur_color = item['Primary Fur Color']
               obj.highlight_fur_color = item['Highlight Fur Color']
               obj.color_notes = item['Color notes']
               obj.location = item['Location']
               obj.specific_location = item['Specific Location']
               obj.running = item['Running']
               obj.chasing = item['Chasing']
               obj.climbing = item['Climbing']
               obj.eating = item['Eating']
               obj.foraging = item['Foraging']
               obj.other_activities = item['Other Activities']
               obj.kuks = item['Kuks']
               obj.quaas = item['quaas']
               obj.moans = item['Moans']
               obj.tail_flags = item['Tail flags']
               obj.tail_twitch = item['Tail twitches']
               obj.approaches = item['Approaches']
               obj.indifferent = item['Indifferent']
               obj.runs_from = item['Runs from']
               obj.other_interactions = item['Other Interaction']

               obj.save()


        msg = f'You are importing from {file_}' 
        self.stdout.write(self.style.SUCCESS(msg))
