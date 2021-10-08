from django.urls import path
from .views import RutasEncontradas, holamundo

urlpatterns = [
    path("Encontradas/",RutasEncontradas.as_view()),
    
]
