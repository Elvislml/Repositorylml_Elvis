from django.db import models

# Create your models here.
class Calificaciones(models.Model):
    name = models.CharField('Alumno', max_length=50)
    subject = models.CharField('Materia', max_length=50)
    grade1 = models.IntegerField('Calificación 1')
    grade2 = models.IntegerField('Calificación 2')
    grade3 = models.IntegerField('Calificación 3')
    averag = models.IntegerField('Promedio') #, max_digits=3, decimal_places=2)