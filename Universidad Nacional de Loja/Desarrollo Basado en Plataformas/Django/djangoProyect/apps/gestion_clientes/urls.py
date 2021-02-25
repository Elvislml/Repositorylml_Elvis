from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "clientes"),
    path('crearClientes', views.crearCliente, name = "crearClientes"),
    path('modificarClientes/<cliente_id>/', views.modificarCliente, name = "modificarClientes"),
    path('eliminarClientes/<cliente_id>/', views.eliminarCliente, name = "eliminarClientes"),
    path('cuentas/<int:cedula>/', views.listarCuentas, name = "cuentas"),
    path('crearCuentas/<int:cedula>/', views.crearCuenta, name = "crearCuentas"),
    path('modificarCuenta/<int:numero>/', views.modificarCuenta, name = "modificarCuenta"),
    path('eliminarCuenta/<int:numero>/', views.eliminarCuenta, name = "eliminarCuenta"),
]
