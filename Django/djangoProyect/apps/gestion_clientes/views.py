from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"clientes/index.html")

def crearCliente(request):
    return render(request,"clientes/crear.html")

def crearCuenta(request):
    return render(request,"Hola crear")

def modificarCliente(request):
    return render(request,"Hola crear")

def modificarCuenta(request):
    return render(request,"Hola crear")
