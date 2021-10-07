from django.shortcuts import render

# Create your views here.
def holamundo (request):
    nombre = 'ivan'
    return render(request, 'holamundo.html',{'nombre_ivan':nombre})