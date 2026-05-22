import pickle
import numpy as np
import os
from django.shortcuts import render
from .forms import MaternalHealthForm

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "mom_ai_model.pkl")
encoder_path = os.path.join(BASE_DIR, "label_encoder.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)
with open(encoder_path, "rb") as f:
    encoder = pickle.load(f)

def home(request):
    return render(request, "predictor/home.html")

def predict(request):
    if request.method == "POST":
        form = MaternalHealthForm(request.POST)
        if form.is_valid():
            # Data must match training features order: Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate
            data = np.array([[
                form.cleaned_data['age'],
                form.cleaned_data['systolic_bp'],
                form.cleaned_data['diastolic_bp'],
                form.cleaned_data['bs'],
                form.cleaned_data['body_temp'],
                form.cleaned_data['heart_rate']
            ]])
            
            prediction = model.predict(data)
            risk_level = encoder.inverse_transform(prediction)[0]
            
            return render(request, "predictor/result.html", {
                "risk": risk_level,
                "data": form.cleaned_data
            })
    else:
        form = MaternalHealthForm()
    
    return render(request, "predictor/form.html", {"form": form})
