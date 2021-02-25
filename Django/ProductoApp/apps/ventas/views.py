from django.shortcuts import render, redirect
from apps.modelo.models import Producto, Ventas
from .forms import FormularioVentas

# Create your views here.
def index(request):
    listaProductos = Producto.objects.all()
    return render(request,'Ventas/indexVentas.html', locals())


def comprar(request, producto_id):
    formVentas = FormularioVentas()
    producto = Producto.objects.get(producto_id = producto_id)
    if request.method == 'POST':
        ventas = Ventas()
        ventas.cantidad = float(request.POST.get('cantidad'))
        ventas.total = float(request.POST.get('cantidad')) * float(producto.precio)
        ventas.producto = producto
        ventas.save()
        cantidadDisponible = float(producto.cantidad) - float(request.POST.get('cantidad'))
        producto.cantidad = cantidadDisponible
        producto.save()
        return redirect (index)
    return render (request,'Ventas/comprarProducto.html', locals())
        
def listaCompras(request):
    listaVentas = Ventas.objects.all()
    return render(request, 'Ventas/listaCompras.html', locals())
