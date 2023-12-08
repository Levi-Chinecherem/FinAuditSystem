from django import forms
from .models import AuditLog

class AuditLogForm(forms.ModelForm):
    class Meta:
        model = AuditLog
        fields = ['action', 'description', 'related_object']

        widgets = {
            'action': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'related_object': forms.Select(attrs={'class': 'form-select'}),
        }
