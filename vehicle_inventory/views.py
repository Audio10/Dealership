from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect, render

# Forms
from vehicle_inventory.forms import VehicleForm

# Serializer
from vehicle_inventory.serializers import VehicleSerializer, CreateVehicleSerializer

# Models
from vehicle_inventory.models import Vehicle


@api_view(['Get'])
def list_vehicles(request):
    """List Vehicles."""
    vehicles = Vehicle.objects.all()
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)


@api_view(['Get'])
def list_vehicles_portal(request):
    """List Vehicles."""
    vehicles = Vehicle.objects.all()
    print(vehicles)
    return render(
        request=request,
        template_name="list.html",
         context={
            'vehicles': vehicles
        }
    )


@api_view(['GET', 'POST'])
def create_vehicle(request):
    """Create a Vehicle."""
    if request.method == 'POST':
        serializer = CreateVehicleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vehicle = serializer.save()
        return redirect('v1/portal/vehicles/list')

    else:
        return render(
            request=request,
            template_name="new.html",
        )
