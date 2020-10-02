from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tenant/payment', views.paymentLog, name='paymentLog'),
    path('new/tenant', views.newtenant, name='newtenant'),
    path('new/parkingfee', views.parkingfee, name='parkingfee'),
    path('remove/<int:id>/', views.removeTenant, name='removeTenant'),
    path('cancel/<int:id>/', views.removePayment, name='removePayment'),
    ]