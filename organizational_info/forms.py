# organizational_info/forms.py
from django import forms
from .models import InternalControl, CorporateGovernance, AccountingProcess

class InternalControlForm(forms.ModelForm):
    class Meta:
        model = InternalControl
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CorporateGovernanceForm(forms.ModelForm):
    class Meta:
        model = CorporateGovernance
        fields = ['policy_name', 'details']
        widgets = {
            'policy_name': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AccountingProcessForm(forms.ModelForm):
    class Meta:
        model = AccountingProcess
        fields = ['process_name', 'details']
        widgets = {
            'process_name': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),
        }
