# Generated by Django 4.0.3 on 2022-05-03 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compdss', '0007_calculation_ci_value_calculation_solar_co2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calculation',
            old_name='tide_LCOE',
            new_name='tidal_LCOE',
        ),
        migrations.RenameField(
            model_name='calculation',
            old_name='tide_operational_years',
            new_name='tidal_operational_years',
        ),
    ]
