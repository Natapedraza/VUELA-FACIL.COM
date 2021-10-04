from django.urls import path
from .views import agency_detail_edit

urlpatterns = [
    #path('usuario/<int:id>/', user_detail),
    path('agencia/<int:id>/edit/', agency_detail_edit ),
]