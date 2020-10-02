from django import forms
from .models import *

class tenantForm(forms.ModelForm):
	class Meta:
		model = Tenant
		fields = ('name', 'phone', 'address',)
		widgets = {
		'name': forms.TextInput(attrs = {
			'placeholder': 'Full Name',
			'class': 'form-control'
			}),
		'phone': forms.NumberInput(attrs = {
			'placeholder': 'Phone no.',
			'class': 'form-control'
			}),
		'address': forms.TextInput(attrs = {
			'placeholder': 'House no. - Street name - Town/City',
			'class': 'form-control'
			}),
		}

class carForm(forms.ModelForm):
	class Meta:
		model = Car
		fields = ('brand_name', 'plate_number',)
		widgets = {
		'brand_name': forms.TextInput(attrs = {
			'placeholder': 'Car Brand',
			'class': 'form-control'
			}),
		'plate_number': forms.TextInput(attrs = {
			'placeholder': 'Plate no.',
			'class': 'form-control'
			}),
		}

class ParkInForm(forms.ModelForm):
	class Meta:
		model = parking_in
		fields = ('tenant', 'cash')
		widgets = {
		'tenant': forms.Select(attrs = {
			'placeholder': 'Tenant',
			'class': 'form-control'
			}),
		'cash': forms.NumberInput(attrs = {
			'placeholder': 'Cash',
			'class': 'form-control',
			'id': 'cash',
			'name': 'cash',
			}),
		}