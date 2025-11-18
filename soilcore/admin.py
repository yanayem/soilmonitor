from django.contrib import admin
from .models import SoilType, Newsletter


@admin.register(SoilType)
class SoilTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'ph_min', 'ph_max', 'ph_range')
    search_fields = ('name', 'location')
    list_filter = ('location',)


