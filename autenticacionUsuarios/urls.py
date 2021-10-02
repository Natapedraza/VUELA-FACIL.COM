from django.urls import path
from .views import agency_detail#, user_detail

urlpatterns = [
    #path('usuario/<int:id>/', user_detail),
    path('agencia/<int:id>/', agency_detail),
]