""" Vehicle serializers."""

# Djangon
from rest_framework import serializers

# Validators
from rest_framework.validators import UniqueValidator

# Model
from vehicle_inventory.models import Vehicle
from makes.models import Make

# Serializers
from makes.serializers import MakeSerializer


class VehicleSerializer(serializers.Serializer):
    """Vehicle serializers."""

    make = MakeSerializer(many=False, read_only=True)
    # make_id = serializers.IntegerField(write_only=True)
    model = serializers.CharField()
    description = serializers.CharField()
    color = serializers.CharField()
    doors = serializers.IntegerField()
    lot = serializers.CharField()


class CreateVehicleSerializer(serializers.Serializer):
    """Create Vehicle serializer."""

    make = serializers.CharField()
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

    def validate(self, data):
        maketem = Make.objects.filter(name=data["make"])
        if  not maketem:
            make = Make(name=data["make"])
            make.save()
            
        
        return data
    
    def create(self, data):
        """Create circle."""
        maketem = Make.objects.get(name=data["make"])
        data["make"] = maketem
        
        return Vehicle.objects.create(**data)
