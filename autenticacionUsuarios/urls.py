from django.urls import path
from .views import agency_delete, agency_detail_edit, registro_usuario

urlpatterns = [
    path('agencia/<int:id>/edit/', agency_detail_edit ),
    path('register/', registro_usuario),
    path('delete/<int:id>/', agency_delete)
]