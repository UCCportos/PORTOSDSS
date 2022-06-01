from django.shortcuts import render
from django.shortcuts import redirect
import pandas as pd
from .forms import *
from .models import *
import csv
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
	if request.POST:
		Calculation.objects.all().delete()
		response_forms = {}
		#try:
		panel_area = float(request.POST['panel_area'])
		solar_radiation = float(request.POST['solar_radiation'])
		efficiency = float(request.POST['efficiency'])
		performance_ratio = float(request.POST['performance_ratio'])
			#s_cost = float(request.POST['s_cost'])
			#solar_operational_years = float(request.POST['solar_operational_years'])
			#ci_value = float(request.POST['ci_value'])
		solar_energy = (panel_area*solar_radiation*efficiency*performance_ratio)/100
		solar_energy_loss = ((solar_energy) - (0.18*solar_energy))
			#solar_LCOE = (s_cost/(solar_operational_years*solar_energy))
			#solar_co2 = (solar_energy*ci_value)
		#print(solar_energy)
		#except:
			#print('no solar data')

		#try:
		swept_area_wind = 3.14 * float(request.POST['turbine_radius'])**2
		wind_energy = (((0.5) * (float(request.POST['air_density'])) * (float(request.POST['velocity'])**3) * (float(request.POST['turbine_cp']) * swept_area_wind )) / 1000) * (float(request.POST['wind_hours']))
			#wi_cost = float(request.POST['wi_cost'])
			#wind_operational_years = float(request.POST['wind_operational_years'])
		wind_energy_loss = ((wind_energy) - (0.15*wind_energy))
			#wind_LCOE = (wi_cost/(wind_operational_years*wind_energy))
			#wind_co2 = (wind_energy*ci_value)
		#except:
			#print('no wind data')

		#try:
			#t_cost = float(request.POST['t_cost'])
			#tidal_operational_years = float(request.POST['tidal_operational_years'])
		swept_area_tide = 3.14 * float(request.POST['radius_turbine'])**2
		tidal_energy = (((0.5) * (float(request.POST['water_density'])) * (float(request.POST['mean_velocity'])**3) * (float(request.POST['turbine_cp_tide']) * (swept_area_tide))) / 1000) * (float(request.POST['tide_hours']))
		tidal_energy_loss = ((tidal_energy) - (0.16*tidal_energy))
			#tidal_LCOE = (t_cost/(tidal_operational_years*tidal_energy))
			#tide_co2 = (tidal_energy*ci_value)
		#except:
			#print('no tide data')

		#try:
		wave_power = (((float(request.POST['water_density_wave'])) * 9.81 ) / (64 * 3.14)) / (float(request.POST['wave_height'])**2) * (float(request.POST['wave_period']))
		wave_energy = (((float(request.POST['pto_efficiency'])) * wave_power)  / 1000) * (float(request.POST['wave_hours']))
			#wa_cost = float(request.POST['wa_cost'])
			#wave_operational_years = float(request.POST['wave_operational_years'])
		wave_energy_loss = ((wave_energy) - (0.16*wave_energy))
			#wave_LCOE = (wa_cost/(wave_operational_years*wind_energy))
			#wave_co2 = (wave_energy*ci_value)
		#except:
			#print('no wave data')

		#try:
		total_energy = (solar_energy + wind_energy + tidal_energy + wave_energy)
		energy_percent_solar = (solar_energy/total_energy)*100
		energy_percent_wind = (wind_energy/total_energy)*100
		energy_percent_tidal = (tidal_energy/total_energy)*100
		energy_percent_wave = (wave_energy/total_energy)*100
			#total_co2 = (solar_co2 + wind_co2 + tide_co2 + wave_co2)
		#except:
			#print('no data')

		print(total_energy)
		print(energy_percent_solar)
		print(energy_percent_wind)
		print(energy_percent_tidal)
		print(energy_percent_wave)

		

		
		response_forms.update({'Location' : request.POST['Location']})
		response_forms.update({'panel_area' : float(request.POST['panel_area'])})
		response_forms.update({'solar_radiation' : float(request.POST['solar_radiation'])})
		response_forms.update({'efficiency' : float(request.POST['efficiency'])})
		response_forms.update({'performance_ratio' : float(request.POST['performance_ratio'])})
		response_forms.update({'turbine_cp' : float(request.POST['turbine_cp'])})
		response_forms.update({'pole_height' : float(request.POST['pole_height'])})
		response_forms.update({'turbine_radius': float(request.POST['turbine_radius'])})
		response_forms.update({'air_density': float(request.POST['air_density'])})
		response_forms.update({'velocity': float(request.POST['velocity'])})
		response_forms.update({'wind_hours': float(request.POST['wind_hours'])})
		response_forms.update({'turbine_cp_tide': float(request.POST['turbine_cp_tide'])})
		response_forms.update({'tide_range': float(request.POST['tide_range'])})
		response_forms.update({'radius_turbine': float(request.POST['radius_turbine'])})
		response_forms.update({'water_density': float(request.POST['water_density'])})
		response_forms.update({'mean_velocity': float(request.POST['mean_velocity'])})
		response_forms.update({'tide_hours': float(request.POST['tide_hours'])})
		response_forms.update({'water_density_wave': float(request.POST['water_density_wave'])})
		response_forms.update({'wave_height': float(request.POST['wave_height'])})
		response_forms.update({'wave_period': float(request.POST['wave_period'])})
		response_forms.update({'pto_efficiency': float(request.POST['pto_efficiency'])})
		response_forms.update({'wave_hours': float(request.POST['wave_hours'])})
		#response_forms.update({'ci_value' : float(request.POST['ci_value'])})
		#response_forms.update({'s_cost' : float(request.POST['s_cost'])})
		#response_forms.update({'wi_cost' : float(request.POST['wi_cost'])})
		#response_forms.update({'t_cost' : float(request.POST['t_cost'])})
		#response_forms.update({'wa_cost' : float(request.POST['wa_cost'])})
		#response_forms.update({'solar_operational_years' : float(request.POST['solar_operational_years'])})
		#response_forms.update({'wind_operational_years' : float(request.POST['wind_operational_years'])})
		#response_forms.update({'tidal_operational_years' : float(request.POST['tidal_operational_years'])})
		#response_forms.update({'wave_operational_years' : float(request.POST['wave_operational_years'])})
		response_forms.update({'solar_energy' : solar_energy})
		response_forms.update({'swept_area_wind' : swept_area_wind})
		response_forms.update({'wind_energy' : wind_energy})
		response_forms.update({'swept_area_tide' : swept_area_tide})
		response_forms.update({'tidal_energy' : tidal_energy})
		response_forms.update({'wave_energy' : wave_energy})
		response_forms.update({'solar_energy_loss' : solar_energy_loss})
		response_forms.update({'wind_energy_loss' : wind_energy_loss})
		response_forms.update({'tidal_energy_loss' : tidal_energy_loss})
		response_forms.update({'wave_energy_loss' : wave_energy_loss})
		response_forms.update({'total_energy' : total_energy})
		response_forms.update({'energy_percent_solar' : energy_percent_solar})
		response_forms.update({'energy_percent_wind' : energy_percent_wind})
		response_forms.update({'energy_percent_tidal' : energy_percent_tidal})
		response_forms.update({'energy_percent_wave' : energy_percent_wave})
		#response_forms.update({'solar_LCOE' : solar_LCOE})
		#response_forms.update({'wind_LCOE' : wind_LCOE})
		#response_forms.update({'tidal_LCOE' : tidal_LCOE})
		#response_forms.update({'wave_LCOE' : wave_LCOE})
		#response_forms.update({'solar_co2' : solar_co2})
		#response_forms.update({'wind_co2' : wind_co2})
		#response_forms.update({'tide_co2' : tide_co2})
		#response_forms.update({'wave_co2' : wave_co2})
		#response_forms.update({'total_co2' : total_co2})
		#response_forms.update({'Country' : request.POST['Country']})



		print (response_forms)

		form = Calculation_Form (response_forms)

		if form.is_valid():
			form.save() 
			print('form is valid')
			return redirect('result')
		else:
			print(form)

	return render(request,'index.html')

def result(request):
	obj = Calculation.objects.all()[0]
	chart_data = [obj.solar_energy, obj.wind_energy, obj.tidal_energy, obj.wave_energy]
	chart_data_1 = [obj.solar_energy_loss, obj.wind_energy_loss, obj.tidal_energy_loss, obj.wave_energy_loss]
	chart_data_2 = [obj.energy_percent_solar, obj.energy_percent_wind, obj.energy_percent_tidal, obj.energy_percent_wave]
	print (chart_data)
	return render(request, 'result.html', {'obj':obj, 'chart_data': chart_data, 'chart_data_1': chart_data_1, 'chart_data_2': chart_data_2})

	

def data(request):
	if request.method == 'POST':
		print(request.FILES)
		form = Csv_Form(request.POST, request.FILES)
		Timeseries_data.objects.all().delete()
		data = csv.reader(request.FILES['csv'].read().decode('utf8').splitlines())
		next(data)
		iterator_list = []
		for row in data:
			form1 = Csvdata_Form({'time':row[0],'local_time':row[1],'radiation_surface':float(row[2])})
			if form1.is_valid:
				form1.save()

		if form.is_valid():
			form.save()
			print('form is valid')
			return redirect('index')
		else:
			print(form)
	else:
		form = Csv_Form()
	context= {'form':form}
	return render(request,'data.html',context)



def contact(request):
	return render(request,'contact_us.html')

def instruct(request):
	return render(request,'instruct.html')