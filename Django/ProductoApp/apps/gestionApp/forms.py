from django import forms
from apps.modelo.models import Proveedor, Producto

class FormularioProveedor(forms.ModelForm):    
    class Meta:
        model = Proveedor
        fields = [
            "cedula",
            "nombre",
            "apellido",
            "correo",
            "telefono",
            "celular",
            "direccion"]
        labels = {
            "cedula":"Cedula",
            "nombre":"Nombre",
            "apellido":"Apellido",
            "correo":"Correo",
            "telefono":"Telefono",
            "celular":"Celular",
            "direccion":"Direccion"
        }

        widgets = {
            "cedula":forms.TextInput(attrs = {'class':'form-control'}),
            "nombre":forms.TextInput(attrs = {'class':'form-control'}),
            "apellido":forms.TextInput(attrs = {'class':'form-control'}),
            "correo":forms.TextInput(attrs = {'class':'form-control'}),
            "telefono":forms.TextInput(attrs = {'class':'form-control'}),
            "celular":forms.TextInput(attrs = {'class':'form-control'}),
            "direccion":forms.TextInput(attrs = {'class':'form-control'})
        }
        
class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            "nombreProducto",
            "precio",
            "cantidad"
        ]

        labels = {
            "nombreProducto":"Nombre del Producto",
            "precio":"Precio",
            "cantidad":"Cantidad"
        }

        widgets = {
            "nombreProducto":forms.TextInput(attrs = {'class':'form-control'}),
            "precio":forms.TextInput(attrs = {'class':'form-control'}),
            "cantidad":forms.TextInput(attrs = {'class':'form-control'}),
        }
