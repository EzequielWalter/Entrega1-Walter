from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_inicio_curso = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'