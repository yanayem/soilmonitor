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


from django.db import models

class CommunityPost(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    high_salinity_solution = models.BooleanField(default=False)  

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.name if self.name else 'Anonymous'})"
