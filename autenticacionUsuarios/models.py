from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Agencia(models.Model):

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    nombre_usuario = models.CharField(max_length=45,null=True)
    contraseña= models.CharField(max_length=45)
    descripcion = models.TextField(null=True)
    telefono = models.CharField(max_length=30,null=True)
    direccion = models.CharField(max_length=60,null=True)
    correo = models.EmailField(max_length=80)
    terminos_condiciones = models.BooleanField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"nombre:{self.nombre}, correo:{self.correo}"


class Usuario(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    nombre_usuario = models.CharField(max_length=45,null=True)
    contraseña= models.CharField(max_length=45)
    descripcion = models.TextField(null=True)
    telefono = models.CharField(max_length=30,null=True)
    direccion = models.CharField(max_length=60,null=True)
    correo = models.EmailField(max_length=80)
    terminos_condiciones = models.BooleanField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"nombre:{self.nombre}, correo:{self.correo}"

