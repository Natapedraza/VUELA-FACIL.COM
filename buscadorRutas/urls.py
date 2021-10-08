from django.urls import path
from .views import RutasEncontradas

urlpatterns = [
    path("Encontradas/",RutasEncontradas.as_view()),
    
]
