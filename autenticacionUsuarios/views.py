from django.shortcuts import render
from .models import Usuario 

# Create your views here.
def user_detail(request,id):
   user = Usuario.objects.get(id=id)

   return render(request, 'profile.html', {'user':user} )
