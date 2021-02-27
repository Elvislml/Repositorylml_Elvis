from django import forms
from apps.modelo.models import Cliente, Cuenta


class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["cedula", "apellidos", "nombres", "genero",
                  "estadoCivil", "correo", "telefono", "celular", "direccion"]

        labels = {
            "cedula": "Cedula",
            "apellidos": "Apellido",
            "nombres": "Nombre",
            "genero":"Genero",
            "estadoCivil": "Estado Civil",
            "correo": "Correo",
            "telefono": "Telefono",
            "celular": "Celular",
            "direccion": "Direccion"
        }

        widgets = {
            "cedula":forms.TextInput(attrs = {'class':'form-control'}),
            "apellidos": forms.TextInput(attrs = {'class':'form-control'}),
            "nombres": forms.TextInput(attrs = {'class':'form-control'}),
            "genero":forms.Select(attrs = {'class':'form-select'}),
            "estadoCivil" : forms.Select(attrs = {'class':'form-select'}),
            "correo" : forms.EmailInput(attrs = {'class':'form-control'}),
            "telefono" : forms.TextInput(attrs = {'class':'form-control'}),
            "celular":forms.TextInput(attrs = {'class':'form-control'}),
            "direccion": forms.Textarea(attrs = {'class':'form-control'})
        }


class FormularioCuenta(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ["numero", "tipoCuenta", "saldo"]

        labels = {
            "numero" : "Numero de Cuenta",
            "tipoCuenta" : "Tipo de Cuenta",
            "saldo" : "Saldo"
        }

        widgets = {
            "numero" : forms.TextInput(attrs = {'class':'form-control'}),
            "tipoCuenta" : forms.Select(attrs = {'class':'form-select'}),
            "saldo" : forms.TextInput(attrs = {'class':'form-control'})
        }
