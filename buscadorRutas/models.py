from django.db import models

# Create your models here.

class Ruta(models.Model):
    codigoRuta = models.BigAutoField(primary_key=True)
    ciudadOrigen = models.CharField(max_length=40)
    ciudadDestino= models.CharField(max_length=40)
    precio = models.FloatField()
    fechaIda = models.DateField()
    fechaVuelta = models.DateField()
    descuento = models.FloatField()