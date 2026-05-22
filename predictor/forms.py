from django import forms

class MaternalHealthForm(forms.Form):
    age = forms.IntegerField(label="Age (years)", min_value=10, max_value=100)
    systolic_bp = forms.IntegerField(label="Systolic BP (Upper value)", min_value=70, max_value=200)
    diastolic_bp = forms.IntegerField(label="Diastolic BP (Lower value)", min_value=40, max_value=120)
    bs = forms.FloatField(label="Blood Sugar (mmol/L)", min_value=1.0, max_value=30.0)
    body_temp = forms.FloatField(label="Body Temperature (F)", min_value=95.0, max_value=110.0)
    heart_rate = forms.IntegerField(label="Heart Rate (bpm)", min_value=40, max_value=150)
