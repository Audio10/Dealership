"""Vehicles URLs."""

# Django
from django.urls import path

# Views.
from vehicle_inventory.views import create_vehicle, list_vehicles, list_vehicles_portal

urlpatterns = [
    path('v1/portal/vehicles/', list_vehicles),
    path('', create_vehicle),
    path('v1/portal/vehicles/list', list_vehicles_portal),
]