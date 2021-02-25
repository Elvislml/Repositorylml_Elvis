from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ventas"),
    path('listaCompras', views.listaCompras, name="listaCompras"),
    path('comprar/<producto_id>', views.comprar, name="comprar"),
]
