from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.views.generic.list import ListView
from .forms import Buscador
from buscadorRutas.models import Ruta


class RutasEncontradas(ListView):
   model = Ruta
   template_name = "home_login_rutas.html"

def buscarRutas(request): 

    if request.method == 'POST': 
        buscador = Buscador(request.POST)
        if buscador.is_valid:
            datosBuscador = buscador.cl 
            ciudad_origen = datosBuscador['ciudadOrigen']
            ruta = get_list_or_404(Ruta,ciudadOrigen=ciudad_origen)
            print(ruta)
            request.session['ruta'] = {'ruta': ruta} 
            return redirect('buscadorRuta/Encontradas/')
    else :
        buscador = Buscador()


    return render(request, 'buscadorRutas.html', {'buscador':Buscador})
