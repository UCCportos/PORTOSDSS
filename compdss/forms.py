from .models import *
from django import forms


class Csv_Form(forms.ModelForm):
	class Meta:
		model = Data_csv
		fields ='__all__'

class Csvdata_Form(forms.ModelForm):
	class Meta:
		model = Timeseries_data
		fields ='__all__'

class Calculation_Form(forms.ModelForm):
	class Meta:
		model = Calculation
		fields ='__all__'
