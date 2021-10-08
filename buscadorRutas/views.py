from django.shortcuts import render
from django.views.generic.list import ListView
import os
from buscadorRutas.models import Ruta


class RutasEncontradas(ListView):
   model = Ruta
   template_name = "home_login_rutas.html"