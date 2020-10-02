from django.contrib import admin
from .models import Tenant, Car, parking_in, parking_out
# Register your models here.
admin.site.register(Tenant)
admin.site.register(Car)
admin.site.register(parking_out)
admin.site.register(parking_in)