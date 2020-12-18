from django.shortcuts import render,redirect
from apps.modelo.models import Cliente
from .forms import FormularioCliente,FormularioCuenta
# Create your views here.

def index(request):
    #manejo de ORM
    listaClientes = Cliente.objects.all()
    return render(request,"clientes/index.html", locals())

def crearCliente(request):
    formCliente = FormularioCliente(request.POST)
    if request.method == 'POST':
        return redirect(index)
    return render(request,"clientes/crear.html", locals())

def crearCuenta(request):
    return render(request,"Hola crear")

def modificarCliente(request):
    return render(request,"Hola crear")

def modificarCuenta(request):
    return render(request,"Hola crear")
