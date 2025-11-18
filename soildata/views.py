from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import UserProfile
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from account.models import UserProfile
from soilcore.models import SoilType
from .models import CropHealthPrediction
import json

@login_required
def dashboard(request):
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)

    total_soil_types = SoilType.objects.count()
    total_predictions = CropHealthPrediction.objects.count()


    recent_soil_types = SoilType.objects.all()[:5]
    recent_predictions = CropHealthPrediction.objects.order_by('-predicted_at')[:5]

    risk_counts = {
        "Healthy": CropHealthPrediction.objects.filter(risk_level="Healthy").count(),
        "Moderate": CropHealthPrediction.objects.filter(risk_level="Moderate").count(),
        "High": CropHealthPrediction.objects.filter(risk_level="High").count(),
    }

    context = {
        "user": user,
        "profile": profile,
        "total_soil_types": total_soil_types,
        "total_predictions": total_predictions,
        "recent_soil_types": recent_soil_types,
        "recent_predictions": recent_predictions,
        "risk_counts": json.dumps(risk_counts), 
    }
    return render(request, "dashboard.html", context)


@login_required
def crop_advisor(request):
    recommendations = []
    tips = []
    ph_value = None
    soil_type_input = ""
    location_input = ""

    if request.method == "POST":
        # Get values from the form
        ph_raw = request.POST.get("ph")
        soil_type_input = request.POST.get("soil_type", "").strip()
        location_input = request.POST.get("location", "").strip()

        try:
            ph_value = float(ph_raw)
        except (ValueError, TypeError):
            ph_value = None

        if ph_value is not None:
            soils = SoilType.objects.filter(ph_min__lte=ph_value, ph_max__gte=ph_value)

            if soil_type_input:
                soils = soils.filter(name__icontains=soil_type_input)

            if location_input:
                soils = soils.filter(location__icontains=location_input)

            for soil in soils:
                if soil.suitable_crops:
                    crops_list = [c.strip() for c in soil.suitable_crops.split(",")]
                    recommendations.extend(crops_list)

                # Tips: you can customize what tips to show
                if soil.description:
                    tips.append(soil.description)

            # Remove duplicates
            recommendations = list(set(recommendations))
            tips = list(set(tips))

    context = {
        "recommendations": recommendations,
        "tips": tips,
        "ph_value": ph_value,
        "soil_type_input": soil_type_input,
        "location_input": location_input,
    }
    return render(request, "crop_advisor.html", context)



def crop_health_prediction(request):
    try:
        soil_types = SoilType.objects.all()
    except Exception:
        soil_types = []

    if request.method == "POST":
        soil_type_id = request.POST.get("soil_type")
        crop = request.POST.get("crop")
        ph_raw = request.POST.get("ph")
        temp_raw = request.POST.get("temperature")
        moisture_raw = request.POST.get("moisture")
        if not soil_type_id or not crop or not ph_raw or not temp_raw or not moisture_raw:
            messages.error(request, "All fields are required.")
            return render(request, "crop_health.html", {"soil_types": soil_types})

        
        try:
            ph = float(ph_raw)
            temp = float(temp_raw)
            moisture = float(moisture_raw)
        except (TypeError, ValueError):
            messages.error(request, "Please enter valid numeric values for pH, temperature and moisture.")
            return render(request, "crop_health.html", {"soil_types": soil_types})

    
        salinity = round((ph * 0.15) + (moisture * 0.02) + (max(0, temp-25) * 0.1), 2)

        
        risk_score = 0

        
        if ph < 5.5 or ph > 8.0:
            risk_score += 35
        elif ph < 6.0 or ph > 7.5:
            risk_score += 15

        
        if temp < 15 or temp > 38:
            risk_score += 30
        elif temp < 20 or temp > 34:
            risk_score += 10

        if moisture < 20:
            risk_score += 25
        elif moisture < 35:
            risk_score += 10


        if salinity >= 4.0:
            risk_score += 30
        elif salinity >= 2.0:
            risk_score += 15

        if risk_score < 0:
            risk_score = 0
        if risk_score > 100:
            risk_score = 100

        if risk_score <= 40:
            status = "healthy"
        elif risk_score <= 70:
            status = "moderate"
        else:
            status = "high"

        soil_name = ""
        try:
            if soil_type_id:
                st = SoilType.objects.get(id=soil_type_id)
                soil_name = st.name
        except Exception:
            soil_name = ""

        prediction = {
            "soil_type": soil_name,
            "crop": crop,
            "ph": ph,
            "temperature": temp,
            "moisture": moisture,
            "salinity": salinity,
            "risk_level": status.title(),
            "risk_score": risk_score,
        }

        return render(request, "crop_health.html", {
            "soil_types": soil_types,
            "prediction": prediction,
            "status": status,
        })
    return render(request, "crop_health.html", {"soil_types": soil_types})

