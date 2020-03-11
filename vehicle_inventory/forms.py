from django import forms

# Models
from vehicle_inventory.models import Vehicle


class VehicleForm(forms.ModelForm):
    """VehicleForm model form."""
    
    class Meta:
        """Form settings """
        
        model = Vehicle
        fields = ('model','description','color','doors','lot')