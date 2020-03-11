""" Make serializers."""

# Djangon
from rest_framework import serializers

# Model
from makes.models import Make


class MakeSerializer(serializers.Serializer):
    """Make serializers."""

    name = serializers.CharField()
    