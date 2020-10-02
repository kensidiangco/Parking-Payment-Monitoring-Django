from django.db import models


class Tenant(models.Model):
	name =models.CharField(max_length=100)
	phone = models.CharField(max_length=11)
	address = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Car(models.Model):
	owner = models.ForeignKey(Tenant, on_delete=models.CASCADE)
	brand_name = models.CharField(max_length=100)
	plate_number = models.CharField(max_length=10)

	def __str__(self):
		return self.brand_name
		  
class parking_in(models.Model):
	tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
	cash = models.DecimalField(decimal_places=2, max_digits=9999999)
	date = models.DateField(auto_now_add=True)
	due_date = models.DateField(blank=False)
	active = models.BooleanField()
	

class parking_out(models.Model):
	tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
	date = models.DateField(auto_now_add=True)

