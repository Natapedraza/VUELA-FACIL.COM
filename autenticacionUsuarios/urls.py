from django.urls import path
from .views import agency_delete, agency_detail_edit, registro_usuario, iniciar_usuario

urlpatterns = [
    path('<str:user_or_agency>/<int:id>/edit/', agency_detail_edit, name="agencyProfile"),
    path('register/', registro_usuario),
    path('delete/<int:id>/', agency_delete),
    path('login/', iniciar_usuario), 
    
]