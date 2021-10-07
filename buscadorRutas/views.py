from django.shortcuts import render
from django.views.generic.list import ListView
import os
from buscadorRutas.models import Ruta

# Create your views here.
def holamundo (request):
    nombre = 'ivan'
    return render(request, 'holamundo.html',{'nombre_ivan':nombre})

class RutasEncontradas(ListView):
   model = Ruta
   template_name = "home_login_rutas.html"