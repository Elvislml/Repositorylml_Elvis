from django.shortcuts import render
from .models import Calificaciones

def index(request):
    calificaciones = Calificaciones.objects.all()
    return render(request, 'index.html', locals())
    
def agregar(request):
    nombre = request.POST["nombre"]
    nombre_materia = request.POST["materia"]
    cal1 = int(request.POST["cal1"])
    cal2 = int(request.POST["cal2"])
    cal3 = int(request.POST["cal3"])
    prom = ((cal1 + cal2 + cal3)/3)
    nuevo = Calificaciones.objects.create(
        name = nombre,
        subject = nombre_materia,
        grade1 = cal1,
        grade2 = cal2,
        grade3 = cal3,
        averag = prom
    )

    return render(request, "promedio.html", locals()) 