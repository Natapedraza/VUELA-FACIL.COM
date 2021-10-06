import abc
from django import forms

class EditProfileForm(forms.Form):
    descripcion= forms.CharField(widget=forms.Textarea, required=False)
    telefono = forms.CharField(required=False)
    direccion = forms.CharField(required=False)
    correo = forms.EmailField(required=False)

class RegisterUserForm(forms.Form):
    nombre=forms.CharField()
    correo=forms.EmailField()
    contraseña=forms.CharField(widget=forms.PasswordInput)
    confirmacion_contraseña= forms.CharField(widget=forms.PasswordInput)
    agencia= forms.BooleanField(required=False)
    usuario= forms.BooleanField(required=False)
