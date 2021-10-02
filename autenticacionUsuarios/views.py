from django.shortcuts import render
from .models import Usuario, Agencia 


# Create your views here.
"""
def user_detail(request,id):
   user = Usuario.objects.get(id=id)

   return render(request, 'profile.html', {'user':user} )
"""
def agency_detail(request,id):
   agency = Agencia.objects.get(id=id)

   return render(request, 'profile.html', {'agencia':agency} ) 