from django.urls import path
from . import views

app_name = 'soildata'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('crop-advisor/', views.crop_advisor, name='crop_advisor'),
    path('crop-health/', views.crop_health_prediction, name='crop_health'),

]
