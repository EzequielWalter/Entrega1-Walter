from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('ver-alumnos/', views.ver_alumnos, name='ver_alumnos'),
    path('crear-alumno/', views.crear_alumno, name='crear_alumno'),
]
