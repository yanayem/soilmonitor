from django.contrib import admin
from .models import CropHealthPrediction



@admin.register(CropHealthPrediction)
class CropHealthPredictionAdmin(admin.ModelAdmin):
    list_display = (
        'soil_type', 'ph', 'temperature', 'moisture',
        'salinity', 'risk_level', 'predicted_at'
    )
    search_fields = ('soil_type__name', 'risk_level')
    list_filter = ('risk_level', 'soil_type', 'predicted_at')

