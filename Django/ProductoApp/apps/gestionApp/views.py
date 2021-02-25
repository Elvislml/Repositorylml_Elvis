from django.shortcuts import render, redirect
from apps.modelo.models import Proveedor, Producto
from .forms import FormularioProveedor, FormularioProducto

# Create your views here.

def index(request):
    listaProveedores = Proveedor.objects.all()
    return render(request, "Proveedor/index.html",locals())


def crearProveedor(request):
    formProveedor = FormularioProveedor(request.POST or None)
    formProducto = FormularioProducto(request.POST or None)
    if request.method == 'POST':
        if formProveedor.is_valid() and formProducto.is_valid():
            proveedor = Proveedor()
            datosProveedor = formProveedor.cleaned_data
            proveedor.cedula = datosProveedor.get('cedula')
            proveedor.nombre = datosProveedor.get('nombre')
            proveedor.apellido = datosProveedor.get('apellido')
            proveedor.correo = datosProveedor.get('correo')
            proveedor.telefono = datosProveedor.get('telefono')
            proveedor.celular = datosProveedor.get('celular')
            proveedor.direccion = datosProveedor.get('direccion')
            #ORM
            proveedor.save()

            #Producto
            producto = Producto()
            datosProducto = formProducto.cleaned_data
            producto.nombreProducto = datosProducto.get('nombreProducto')
            producto.cantidad = datosProducto.get('cantidad')
            producto.precio = datosProducto.get('precio')
            producto.proveedor = proveedor
            #ORM
            producto.save()
            return redirect(index)
    return render(request, "Proveedor/crearProveedor.html", locals())

def modificarProveedor(request, proveedor_id):
    proveedor = Proveedor.objects.get(proveedor_id = proveedor_id)
    data = {
        "formProveedor" : FormularioProveedor(instance = proveedor)
    }

    if request.method == 'POST':
        formProveedor = FormularioProveedor(data = request.POST, instance=proveedor)
        if formProveedor.is_valid():
            formProveedor.save()
            data["formProveedor"] = formProveedor
        return redirect(index)
    return render(request,'Proveedor/modificarProveedor.html', data)

def eliminarProveedor (request, proveedor_id):
    proveedor = Proveedor.objects.get(proveedor_id = proveedor_id)
    proveedor.delete()
    return redirect(index)

#Metodos del Producto
def crearProducto(request, cedula):
    formProducto = FormularioProducto(request.POST or None)
    proveedor = Proveedor.objects.get(cedula = cedula)
    if request.method =="POST":
        if formProducto.is_valid():
            producto = Producto()
            datosProducto = formProducto.cleaned_data
            producto.nombreProducto = datosProducto.get('nombreProducto')
            producto.cantidad = datosProducto.get('cantidad')
            producto.precio = datosProducto.get('precio')
            producto.proveedor = proveedor
            producto.save()
            return redirect(index)
    return render(request ,"Producto/crearProducto.html", locals())


def modificarProducto(request, producto_id):
    producto = Producto.objects.get(producto_id = producto_id)
    data = {
        "formProducto" : FormularioProducto(instance = producto)
    }
    if request.method == "POST":
        formProducto = FormularioProducto(data = request.POST, instance = producto)
        if formProducto.is_valid():
            formProducto.save()
            data["formProducto"] = formProducto
        return redirect(index)
    return render(request,'Producto/modificarProducto.html', data)

def eliminarProducto(request, producto_id):
    producto = Producto.objects.get(producto_id = producto_id)
    producto.delete()
    return redirect(index)
   
def listarProductos(request, cedula):
    proveedor = Proveedor.objects.get(cedula=cedula)
    listProductos = Producto.objects.filter(proveedor=proveedor)
    return render(request, 'Producto/listaProductos.html', locals())
