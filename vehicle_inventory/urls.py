"""Vehicles URLs."""

# Django
from django.urls import path

# Views.
from vehicle_inventory.views import create_vehicle, list_vehicles

urlpatterns = [
    path('vehicles/', list_vehicles),
    path('vehicles/create', create_vehicle)
]