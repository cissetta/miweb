from django.shortcuts import render
from .models import Alumno

# Crear las vistas del Sitio.
def index(request):
    alumnos = Alumno.objects.all()
    print(alumnos)
    return render(request,'index.html',{'alumnos':alumnos})

def pagina1(request):
    return render(request,'pagina1.html')

def pagina2(request):
    return render(request,'pagina2.html')