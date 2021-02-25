from django import forms
from apps.modelo.models import Ventas

class FormularioVentas(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = [
            "cantidad"
        ]

        labels = {
            "cantidad":"Cantidad Deseada"
        }

        widgets = {
            "cantidad":forms.TextInput(attrs = {'class':'form-control'}),
        }
