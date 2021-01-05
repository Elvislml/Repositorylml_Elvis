from django.shortcuts import render,redirect
from apps.modelo.models import Cliente
from apps.modelo.models import Cuenta
from .forms import FormularioCliente,FormularioCuenta
# Create your views here.

def index(request):
    #manejo de ORM
    listaClientes = Cliente.objects.all()
    return render(request,"clientes/index.html", locals())

def crearCliente(request):
    formCliente = FormularioCliente(request.POST)
    formCuenta = FormularioCuenta(request.POST)
    if request.method == 'POST':
        if formCliente.is_valid() and formCuenta.is_valid():
            cliente = Cliente()
            datos_cliente = formCliente.cleaned_data
            cliente.cedula = datos_cliente.get('cedula')
            cliente.nombres = datos_cliente.get('nombres')
            cliente.apellidos = datos_cliente.get('apellidos')
            cliente.genero = datos_cliente.get('genero')
            cliente.estadoCivil = datos_cliente.get('estadoCivil')
            cliente.correo = datos_cliente.get('correo')
            cliente.telefono = datos_cliente.get('telefono')
            cliente.celular = datos_cliente.get('celular')
            cliente.direccion = datos_cliente.get('direccion')
            #ORM
            cliente.save()

            cuenta = Cuenta()
            datos_cuenta = formCuenta.cleaned_data
            cuenta.numero = datos_cuenta.get('numero')
            cuenta.saldo = datos_cuenta.get('saldo')
            cuenta.tipoCuenta = datos_cuenta.get('tipoCuenta')
            cuenta.cliente = cliente
            #ORM    
            cuenta.save()
            return redirect(index)
    return render(request,"clientes/crear.html", locals())


def modificarCliente(request, cedula):
    return render(request, 'clientes/modificar.html', locals())

def modificarCuenta(request):
    return render(request,"Hola crear")
