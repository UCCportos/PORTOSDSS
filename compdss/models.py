from django.db import models
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your models here.

class Data_csv(models.Model):

    csv = models.FileField()
    upload_date = models.DateTimeField(auto_now_add=True)

class Timeseries_data(models.Model):

    time = models.CharField(max_length=100)
    local_time = models.CharField(max_length=100)
    radiation_surface = models.FloatField(default=0.0)


class Calculation(models.Model):
    location = models.CharField(max_length=100, default=0.0)
    port_consumption = models.CharField(max_length=100, default=0.0)
    Country = models.CharField(max_length=100, default=0.0)
    panel_area = models.CharField(max_length=100, default=0.0)
    solar_radiation = models.CharField(max_length=100, default=0.0)
    efficiency = models.CharField(max_length=100, default=0.0)
    performance_ratio = models.CharField(max_length=100, default=0.0)
    turbine_cp = models.CharField(max_length=100, default=0.0)
    pole_height = models.CharField(max_length=100, default=0.0)
    turbine_radius = models.CharField(max_length=100, default=0.0)
    #air_density = models.CharField(max_length = 100, default = 0.0)
    velocity = models.CharField(max_length=100, default=0.0)
    wind_hours = models.CharField(max_length=100, default=0.0)
    turbine_cp_tide = models.CharField(max_length=100, default=0.0)
    tide_range = models.CharField(max_length=100, default=0.0)
    radius_turbine = models.CharField(max_length=100, default=0.0)
    #water_density = models.CharField(max_length = 100, default = 0.0)
    mean_velocity = models.CharField(max_length=100, default=0.0)
    tide_hours = models.CharField(max_length=100, default=0.0)
    #water_density_wave = models.CharField(max_length = 100, default = 0.0)
    wave_height = models.CharField(max_length=100, default=0.0)
    wave_period = models.CharField(max_length=100, default=0.0)
    pto_efficiency = models.CharField(max_length=100, default=0.0)
    wave_hours = models.CharField(max_length=100, default=0.0)
    solar_energy = models.CharField(max_length=100, default=0.0)
    swept_area_wind = models.CharField(max_length=100, default=0.0)
    wind_energy = models.CharField(max_length=100, default=0.0)
    swept_area_tide = models.CharField(max_length=100, default=0.0)
    tidal_energy = models.CharField(max_length=100, default=0.0)
    wave_energy = models.CharField(max_length=100, default=0.0)
    solar_energy_loss = models.CharField(max_length=100, default=0.0)
    wind_energy_loss = models.CharField(max_length=100, default=0.0)
    tidal_energy_loss = models.CharField(max_length=100, default=0.0)
    wave_energy_loss = models.CharField(max_length=100, default=0.0)
    total_energy = models.CharField(max_length=100, default=0.0)
    energy_percent_solar = models.CharField(max_length=100, default=0.0)
    energy_percent_wind = models.CharField(max_length=100, default=0.0)
    energy_percent_tidal = models.CharField(max_length=100, default=0.0)
    energy_percent_wave = models.CharField(max_length=100, default=0.0)
    ci_value = models.CharField(max_length=100, default=0.0)
    s_cost = models.CharField(max_length=100, default=0.0)
    wi_cost = models.CharField(max_length=100, default=0.0)
    t_cost = models.CharField(max_length=100, default=0.0)
    wa_cost = models.CharField(max_length=100, default=0.0)
    solar_operational_years = models.CharField(max_length=100, default=0.0)
    wind_operational_years = models.CharField(max_length=100, default=0.0)
    tidal_operational_years = models.CharField(max_length=100, default=0.0)
    wave_operational_years = models.CharField(max_length=100, default=0.0)
    solar_LCOE = models.CharField(max_length=100, default=0.0)
    wind_LCOE = models.CharField(max_length=100, default=0.0)
    tidal_LCOE = models.CharField(max_length=100, default=0.0)
    wave_LCOE = models.CharField(max_length=100, default=0.0)
    solar_co2 = models.CharField(max_length=100, default=0.0)
    wind_co2 = models.CharField(max_length=100, default=0.0)
    tide_co2 = models.CharField(max_length=100, default=0.0)
    wave_co2 = models.CharField(max_length=100, default=0.0)
    total_co2 = models.CharField(max_length=100, default=0.0)
