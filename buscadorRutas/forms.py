
from django import forms

class Buscador(forms.Form):
    ciudadOrigen = forms.CharField(max_length=40,required=False)
    ciudadDestino = forms.CharField(max_length=40,required=False)
    fechaIda = forms.DateField(required=False) 
    fechaVuelta = forms.DateField(required=False) 


