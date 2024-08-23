from django import forms
from .models import Lots, CutOfBanana

class LotForm(forms.ModelForm):
    class Meta:
        model = Lots
        fields = ['nome_titular', 'local', 'hectares', 'numero']

class CutForm(forms.ModelForm):
    class Meta:
        model = CutOfBanana
        fields = ['primeira', 'segunda', 'kg_caixa', 'data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }