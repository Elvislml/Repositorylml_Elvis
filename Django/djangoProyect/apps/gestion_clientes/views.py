from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from apps.modelo.models import Cliente
from apps.modelo.models import Cuenta
from .forms import FormularioCliente,FormularioCuenta

# Create your views here.

def index(request):
    #manejo de ORM
    listaClientes = Cliente.objects.all()
    return render (request,"clientes/index.html", locals())


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
            return redirect(index)

    return render(request,"clientes/crear.html", locals())


def modificarCliente(request, cliente_id):
    cliente = Cliente.objects.get(cliente_id = cliente_id)
    data = {
        "formCliente" : FormularioCliente(instance = cliente)
    }

    if request.method == 'POST':
        formCliente = FormularioCliente(data = request.POST, instance=cliente)
        if formCliente.is_valid():
            formCliente.save()
            data['mensaje'] = "Modificado con exito"
            data["formCliente"] = formCliente
    return render(request, 'clientes/modificar.html', data)


def eliminarCliente(request, cliente_id):
    cliente = Cliente.objects.get(cliente_id=cliente_id)
    cliente.delete()
    return redirect(to="clientes")

#Cuentas

def listarCuentas(request, cedula):
    cliente = Cliente.objects.get(cedula=cedula)
    cuentas = Cuenta.objects.filter(cliente = cliente)
    return render(request, 'cuentas/index.html', locals())


def crearCuenta(request, cedula):
    formCuenta = FormularioCuenta(request.POST)
    cliente = Cliente.objects.get(cedula = cedula)
    if request.method == 'POST':
        if formCuenta.is_valid():
            cuenta = Cuenta()
            datos_cuenta = formCuenta.cleaned_data
            cuenta.numero = datos_cuenta.get("numero")
            cuenta.saldo = datos_cuenta.get("saldo")
            cuenta.tipoCuenta = datos_cuenta.get("tipoCuenta")
            cuenta.cliente = cliente
            cuenta.save()
            return redirect(index)
    return render(request, 'cuentas/crearCuentas.html', locals())

def modificarCuenta(request, numero):
    cuenta = Cuenta.objects.get(numero = numero)
    data = {
        "formCuenta" : FormularioCuenta(instance = cuenta)
    }

    if request.method == 'POST':
        formCuenta = FormularioCuenta(data = request.POST, instance=cuenta)
        if formCuenta.is_valid():
            formCuenta.save()
            data['mensaje'] = "Modificado con exito"
            data['formCuenta'] = formCuenta
    return render(request, 'cuentas/modificarCuentas.html', data)


def eliminarCuenta(request, numero):
    cuenta = Cuenta.objects.get(numero = numero)
    cuenta.delete()
    return redirect(to="clientes")
