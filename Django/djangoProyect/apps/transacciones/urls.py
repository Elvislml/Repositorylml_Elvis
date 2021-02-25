from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="transacciones"),
    path('cuentaCliente/<int:numero>', views.getCuentaCliente, name="cuentaCliente"),
    path('depositar/<int:numero>', views.depositar, name="depositar"),
]
