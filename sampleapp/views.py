from django.shortcuts import render, redirect
from .models import Tenant, Car, parking_in
from .forms import tenantForm, carForm, ParkInForm

from datetime import datetime, timedelta, date

def dashboard(request):
	logged = Tenant.objects.all()
	cars = Car.objects.all()
	PDTenants = parking_in.objects.all()

	paid = len(PDTenants)
	dateNow = datetime.now().date()
	logged = len(logged)

	context = {
	'cars': cars,
	'dateNow': dateNow,
	'logged': logged,
	'paid': paid
	}

	return render(request, 'dashboard.html', context)

def paymentLog(request):
	parkIn = parking_in.objects.all()
	PDTenants = parking_in.objects.all()

	person = len(parkIn)
	active = 0
	inactive = 0

	for e in PDTenants:
		if e.dueDate:
			inactive += 1
		else:
			active += 1

	context = {
	'parkIn': parkIn,
	'active': active,
	'inactive': inactive,
	'person': person
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