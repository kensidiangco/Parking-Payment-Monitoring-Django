from django.shortcuts import render, redirect
from .models import Tenant, Car, parking_in
from .forms import tenantForm, carForm, ParkInForm

from datetime import datetime, timedelta

def dashboard(request):
	tenants = Tenant.objects.all()
	cars = Car.objects.all()
	tenantActive = parking_in.objects.filter(active=True)
	tenantInactive = parking_in.objects.filter(active=False)

	#HAHAAHAHA LOGIC CODES
	dateNow = datetime.now().date()
	tenantsCount = len(tenants)
	active = len(tenantActive)
	inactive = len(tenantInactive)
	context = {
	'tenants': tenants,
	'cars': cars,
	'dateNow': dateNow,
	'tenantsCount': tenantsCount,
	'active': active,
	'inactive': inactive
	}

	return render(request, 'dashboard.html', context)

def paymentLog(request):
	parkIn = parking_in.objects.all()

	tenantActive = parking_in.objects.filter(active=True)
	for status in tenantActive:
		if status.due_date == datetime.now().date():
			status.active = False
			status.save()

		context = {
	'parkIn': parkIn,
	}
	return render(request, 'paymentLog.html', context)

def newtenant(request):
	form = tenantForm()
	carform = carForm()

	if request.method == "POST":
		form = tenantForm(request.POST)
		carform = carForm(request.POST)

		if form.is_valid() and carform.is_valid():
			form.save()
			carF = carform.save(commit=False)
			carF.owner = Tenant.objects.last()
			carF.save()
			return redirect('dashboard')


	context = {'form': form, 'carForm': carForm}
	return render(request, 'newtenant.html', context)

def parkingfee(request):
	form = ParkInForm()

	if request.method == 'POST':
		form = ParkInForm(request.POST)
		if form.is_valid():
			tenant = form.save(commit=False)
			cash = form.cleaned_data.get('cash')
			month = cash / 4000
			days = month * 30
			tenant.due_date = datetime.now().date() + timedelta(days=int(days))
			if tenant.due_date == datetime.now().date():
				tenant.active = False
			else:
				tenant.active = True
			tenant.save()

			return redirect('dashboard')

	context = {'form': form}
	return render(request, 'parkingfee.html', context)

def removeTenant(request, id):
	tenantR = Tenant.objects.get(id=id)
	tenantR.delete()
	return redirect('dashboard')

def removePayment(request, id):
	tenantPayment = parking_in.objects.get(id=id)
	tenantPayment.delete()

	return redirect('dashboard')