from django.shortcuts import render

# Create your views here.

def registro_usuario(request):
    if request.method == "POST":
        return render(request, "gracias.html")
    return render(request, "registrar.html")

