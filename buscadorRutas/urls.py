from django.urls import path
from .views import RutasEncontradas, holamundo

urlpatterns = [
    path('saludo/',holamundo),
    path("Encontradas/",RutasEncontradas.as_view()),
    
]
