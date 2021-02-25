from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name="proveedor"),
    path('crearProveedor', views.crearProveedor , name="crearProveedor"),
    path('modificarProveedor/<proveedor_id>/', views.modificarProveedor, name = "modificarProveedor"),
    path('eliminarProveedor/<proveedor_id>/', views.eliminarProveedor, name = "eliminarProveedor"),
    path('crearProductos/<int:cedula>/', views.crearProducto , name="crearProductos"),
    path('modificarProducto/<producto_id>/', views.modificarProducto, name = "modificarProducto"),
    path('eliminarProducto/<producto_id>/', views.eliminarProducto, name = "eliminarProducto"),
    path('productos/<int:cedula>/', views.listarProductos, name = "productos"),
]
