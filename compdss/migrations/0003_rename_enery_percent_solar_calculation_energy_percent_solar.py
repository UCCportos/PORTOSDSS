# Generated by Django 4.0.3 on 2022-04-07 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compdss', '0002_calculation_energy_percent_tidal_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calculation',
            old_name='enery_percent_solar',
            new_name='energy_percent_solar',
        ),
    ]
