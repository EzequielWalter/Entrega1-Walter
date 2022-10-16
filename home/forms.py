from django import forms


class AlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_inicio_curso = forms.DateField(required=False)
    
class BusquedaAlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
    apellido = forms.CharField(max_length=30, required=False)