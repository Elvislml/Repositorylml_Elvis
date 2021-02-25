from django.shortcuts import render, redirect
from apps.modelo.models import Cliente, Cuenta, Transaccion
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import FormularioTransaccion
# Create your views here.

@login_required
def index(request):
    usuario = request.user
    if usuario.groups.filter(name="transacciones").exists():
        listaCuentas = Cuenta.objects.all()
        """busqueda = request.POST.get("busqueda")
        if busqueda:
            listaClientes = Cliente.objects.filter(
                Q(nombres__icontains = busqueda) | 
                Q(apellidos__icontains = busqueda)| 
                Q(cedula = busqueda)
            ).distinct()
        """
        return render (request,"cuentas/index_transacciones.html", locals())
    else:
        return render(request, 'login/forbidden.html', locals())
    listaCuentas = Cuenta.objects.all()
    return render (request, "clientes/index.html", locals())

def getCuentaCliente(request, numero):
    usuario = request.user
    if usuario.groups.filter(name="transacciones").exists():
        cuenta = Cuenta.objects.get(numero = numero)
        if cuenta:
            cliente = Cliente.objects.get(cedula = cuenta.cliente)
        return render (request,"transaccion/cuentaCliente.html", locals())
    else:
        return render(request, 'login/forbidden.html', locals())
    listaCuentas = Cuenta.objects.all()
    return render (request, "clientes/index.html", locals())


def depositar(request, numero):
    usuario = request.user
    if usuario.groups.filter(name="transacciones").exists():
        formularioTran = FormularioTransaccion()
        cuenta = Cuenta.objects.get(numero = numero)
        if request.method == 'POST':
            transaccion = Transaccion()
            transaccion.tipo = 'deposito'
            transaccion.valor = float(request.POST.get('valor'))
            transaccion.descripcion = request.POST.get('descripcion')
            transaccion.cuenta = cuenta
            transaccion.save()
            valorTotal = float(request.POST.get('valor')) + float(cuenta.saldo)
            cuenta.saldo = valorTotal
            cuenta.save()
            return redirect (index)
        return render (request,"transaccion/depositar.html", locals())
    else:
        return render(request, 'login/forbidden.html', locals())
    listaCuentas = Cuenta.objects.all()
    return render (request, "clientes/index.html", locals())