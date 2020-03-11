from django.db import models
from makes.models import Make

""" Vehicle Model """
class Vehicle(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    model = models.CharField(unique=True, max_length=60)
    description = models.CharField(max_length=255)
    color = models.CharField(blank=False, null=False,max_length=30)
    doors = models.PositiveIntegerField(default=2)
    lot = models.CharField(
        max_length=20,
        help_text='This is the lot number of Vehicle'
    )

    
    def __str__(self):
        """Return the Vehicle model."""
        return self.model


