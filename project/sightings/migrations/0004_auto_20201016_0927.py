# Generated by Django 3.1.2 on 2020-10-16 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0003_auto_20201016_0832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squirrel',
            name='lattitude',
        ),
        migrations.AddField(
            model_name='squirrel',
            name='latitude',
            field=models.DecimalField(decimal_places=15, default=0, help_text='Latitude of the squirrel', max_digits=17),
        ),
    ]
