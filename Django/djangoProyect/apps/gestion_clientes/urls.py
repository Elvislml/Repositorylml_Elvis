from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "cliente"),
    path('crearClientes', views.crearCliente, name = "crearClientes"),
]
