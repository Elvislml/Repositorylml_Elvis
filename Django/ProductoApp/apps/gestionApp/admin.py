from django.contrib import admin
from apps.modelo.models import Proveedor
from apps.modelo.models import Producto
from apps.modelo.models import Ventas
# Register your models here.

class AdminProveedor(admin.ModelAdmin):
    list_display = ["cedula","nombre","apellido","correo","celular"]
    list_editable = ["correo","nombre","apellido","celular"]
    class Meta :
        model = Proveedor
admin.site.register(Proveedor, AdminProveedor)

class AdminProducto(admin.ModelAdmin):
    list_display = ["nombreProducto","precio","cantidad"]
    search_fields = ["nombreProducto"]
    class Meta :
        model = Producto
admin.site.register(Producto, AdminProducto)

class AdminVentas(admin.ModelAdmin):
    list_display = ["fecha","cantidad","total"]
    list_filter = ["fecha"]
    class Meta :
        model = Ventas
admin.site.register(Ventas, AdminVentas)