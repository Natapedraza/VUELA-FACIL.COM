from django import forms

class EditProfileForm(forms.Form):
    descripcion= forms.CharField(widget=forms.Textarea, required=False)
    telefono = forms.CharField(required=False)
    direccion = forms.CharField(required=False)
    correo = forms.EmailField(required=False)