""" Vehicle serializers."""

# Djangon
from rest_framework import serializers

# Validators
from rest_framework.validators import UniqueValidator

# Model
from vehicle_inventory.models import Vehicle


class VehicleSerializer(serializers.Serializer):
    """Vehicle serializers."""

    make = serializers.StringRelatedField()
    model = serializers.CharField()
    description = serializers.CharField()
    color = serializers.CharField()
    doors = serializers.IntegerField()
    lot = serializers.CharField()


class CreateVehicleSerializer(serializers.Serializer):
    """Create Vehicle serializer."""

    make = serializers.StringRelatedField()
    model = serializers.CharField(
        max_length=60,
        validators=[
            UniqueValidator(queryset=Vehicle.objects.all())
        ]
    )
    description = serializers.CharField(max_length=255, required=False)
    color = serializers.CharField(max_length=30)
    doors = serializers.IntegerField()
    lot = serializers.CharField(max_length=20)
    
    
    def create(self, data):
        """Create circle."""
        return Vehicle.objects.create(**data)