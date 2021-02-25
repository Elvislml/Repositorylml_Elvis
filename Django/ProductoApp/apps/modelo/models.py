from django.db import models

# Create your models here.

class Proveedor(models.Model):
    proveedor_id = models.AutoField(primary_key = True)
    cedula = models.CharField(max_length = 10, unique = True)
    nombre = models.CharField(max_length = 100, null = False)
    apellido = models.CharField(max_length = 100, null = False)
    correo = models.EmailField(max_length = 150, null = False)
    telefono = models.CharField(max_length = 7, null = False)
    celular = models.CharField(max_length = 10, null = False)
    direccion = models.TextField(max_length = 200, null = False)

    def __str__(self):
        return self.cedula


class Producto(models.Model):
    producto_id = models.AutoField(primary_key = True)
    nombreProducto = models.CharField(max_length = 100, null = False)
    precio = models.DecimalField(max_digits = 10, decimal_places = 2, null = False)
    cantidad = models.IntegerField(null=False)
    proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE)

    def __str__(self):
        cadena = str(self.precio) + ";" + str(self.producto_id)
        return cadena


class Ventas(models.Model):
    ventas_id =  models.AutoField(primary_key = True)
    fecha = models.DateTimeField(auto_now_add = True, null = False)
    cantidad = models.IntegerField(null=False)
    total = models.DecimalField(max_digits = 10, decimal_places = 2, null = False)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
