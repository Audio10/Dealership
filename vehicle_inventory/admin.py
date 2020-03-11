from django.contrib import admin

# Model
from vehicle_inventory.models import Vehicle

@admin.register(Vehicle)
class CircleAdmin(admin.ModelAdmin):
    """Circle admin. """

    list_display = (
        'make',
        'model',
        'description',
        'color',
        'doors',
        'lot'
    )

    search_fields = ('make', 'model','lot')

    list_filter = ('color','doors')
