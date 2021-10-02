from django.db import models

# Create your models here.

class Agencia(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=140)
    telefono=models.CharField(max_length=30)
    direccion=models.CharField(max_length=60)
    correo=models.CharField(max_length=80)
    
class Usuario(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)