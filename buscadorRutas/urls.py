from django.urls import path
from .views import RutasEncontradas, buscarRutas

urlpatterns = [
    path("Encontradas/",RutasEncontradas.as_view()),
    path('Buscador/',buscarRutas),
]
