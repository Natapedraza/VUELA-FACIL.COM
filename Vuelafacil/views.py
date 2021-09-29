from django.http.response import HttpResponse
from django.shortcuts import render

def hola_mundo(request):

    return HttpResponse("Hola mundo")