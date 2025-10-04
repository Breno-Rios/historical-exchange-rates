# forms.py
from django import forms
from config.settings.base import ALLOWED_CURRENCIES


class RateForms(forms.Form):
    # Campos extras que não estão no modelo
    start_date = forms.DateField(
        label="Start Date",
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    end_date = forms.DateField(
        label="End Date",
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    base_code = forms.CharField(
        label="Base Code",
        max_length=3,
        initial='USD',     
        required=True,     
        disabled=True      
        
    )
    currency = forms.ChoiceField(
        label="Currency Code",
        choices=[(c, c) for c in ALLOWED_CURRENCIES],
        initial='BRL',     
        required=True,
    )

    class Meta:
        fields = ['start_date', 'end_date', 'base_code', 'currency']


