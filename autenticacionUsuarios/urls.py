from django.urls import path
from .views import user_detail

urlpatterns = [
    path('<int:id>/', user_detail)
]