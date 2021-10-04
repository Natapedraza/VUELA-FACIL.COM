from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Agencia(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    nombre_usuario = models.CharField(max_length=45)
    contraseña= models.CharField(max_length=45, null=True)
    descripcion = models.TextField()
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)
    correo = models.EmailField(max_length=80)
    terminos_condiciones = models.BooleanField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)


class Usuario(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    nombre_usuario = models.CharField(max_length=45)
    contraseña= models.CharField(max_length=45, null=True)
    descripcion = models.TextField()
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)
    correo = models.EmailField(max_length=80)
    terminos_condiciones = models.BooleanField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)