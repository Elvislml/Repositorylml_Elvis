from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "clientes"),
    path('crearClientes', views.crearCliente, name = "crearClientes"),
    path('modificarClientes/<cliente_id>/', views.modificarCliente, name = "modificarClientes"),
    path('eliminarClientes/<cliente_id>/', views.eliminarCliente, name = "eliminarClientes"),
]
