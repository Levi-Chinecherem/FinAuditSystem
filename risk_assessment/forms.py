# risk_assessment/forms.py
from django import forms
from .models import RiskAssessment

class RiskAssessmentForm(forms.ModelForm):
    class Meta:
        model = RiskAssessment
        fields = ['category', 'description', 'impact', 'likelihood', 'mitigation_plan']

        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'impact': forms.TextInput(attrs={'class': 'form-control'}),
            'likelihood': forms.TextInput(attrs={'class': 'form-control'}),
            'mitigation_plan': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
