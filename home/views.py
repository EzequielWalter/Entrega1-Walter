from unittest import loader
from django.http import HttpResponse


from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
import random
from home.forms import BusquedaAlumnoFormulario, AlumnoFormulario

from home.models import Alumno

# Create your views here.


def index(request):
    
    return render(request, 'home/index.html')

def about(request):
    
    return render(request, 'home/about.html')

########################

def crear_alumno(request):
    
    if request.method == 'POST':        # Se asegura de que el formulario entre por POST
        
        formulario = AlumnoFormulario(request.POST)
        
        if formulario.is_valid():        # Chequea que el formulario esa correcto
            data = formulario.cleaned_data     #Le pide la información limpia al formulario
            
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_nacimiento = data.get('fecha_nacimiento', datetime.now())     #Si no hay fecha de nacimiento ingresada pone la de ahora
            
            alumno = Alumno(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
            alumno.save()
        
        return redirect('ver_alumnos')   # redirige a ver los familiares
    
    formulario = AlumnoFormulario()       # Hago la variable formulario traida de familiar
    
    return render(request, 'home/crear_alumno.html', {'formulario': formulario})  # Paso el formulario como contexto

def ver_alumnos(request):
    
    nombre = request.GET.get('nombre')  # Es para buscar por nombre
    
    if nombre:
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)     #Filtra todos los que tengan nombre aunque no esté escrita toda la palabra
    else:
        alumnos = Alumno.objects.all()     # Le pide a la base de datos todos los objetos de Familiares
    
    formulario = BusquedaAlumnoFormulario()
    
    return render(request, 'home/ver_alumnos.html', {'alumnos': alumnos, 'formulario': formulario})       #Se puede poner asi como forma simplificada
