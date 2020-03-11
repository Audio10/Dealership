from django.contrib import admin

# Model
from makes.models import Make

@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    """Make admin. """

    list_display = (
        'name',
        'country'
    )

    search_fields = ('name', 'country')

    list_filter = ('name','country')
