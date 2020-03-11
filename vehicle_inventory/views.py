from rest_framework.decorators import api_view
from rest_framework.response import Response

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


@api_view(['POST'])
def create_vehicle(request):
    """Create a Vehicle."""
    serializer = CreateVehicleSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    vehicle = serializer.save()

    return Response(VehicleSerializer(vehicle).data)