from unittest import loader

from datetime import datetime
from django.shortcuts import render, redirect
from home.forms import BusquedaAlumnoFormulario, AlumnoFormulario
from home.models import Alumno

# Create your views here.


def index(request):
    
    return render(request, 'home/index.html')

def about(request):
    
    return render(request, 'home/about.html')

def contact(request):
    
    return render(request, 'home/contacto.html')

def crear_alumno(request):
    
    if request.method == 'POST':
        
        formulario = AlumnoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_inicio_curso = data.get('fecha_inicio_curso', datetime.now())
            
            alumno = Alumno(nombre=nombre, apellido=apellido, edad=edad, fecha_inicio_curso=fecha_inicio_curso)
            alumno.save()
        
        return redirect('ver_alumnos')
    
    formulario = AlumnoFormulario()
    
    return render(request, 'home/crear_alumno.html', {'formulario': formulario})

def ver_alumnos(request):
    
    nombre = request.GET.get('nombre')
    apellido = request.GET.get('apellido')
    
    if nombre:
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
    elif apellido:
        alumnos = Alumno.objects.filter(apellido__icontains=apellido)
    else:
        alumnos = Alumno.objects.all()
    
    formulario = BusquedaAlumnoFormulario()
    
    return render(request, 'home/ver_alumnos.html', {'alumnos': alumnos, 'formulario': formulario})