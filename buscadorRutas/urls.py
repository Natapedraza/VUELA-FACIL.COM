from django.urls import path
from .views import holamundo

urlpatterns = [
    path('saludo/',holamundo)
]
