from django.db import models
from django.contrib.auth.models import User
from django.db import models
from soilcore.models import SoilType

class CropHealthPrediction(models.Model):
    soil_type = models.ForeignKey(SoilType, on_delete=models.SET_NULL, null=True)
    ph = models.FloatField()
    temperature = models.FloatField()
    moisture = models.FloatField()
    salinity = models.FloatField()
    risk_level = models.CharField(max_length=20)
    predicted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.soil_type.name if self.soil_type else 'Unknown'} - {self.risk_level}"

