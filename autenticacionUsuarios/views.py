from django.shortcuts import redirect, render, get_object_or_404
from .models import Usuario, Agencia
from autenticacionUsuarios.forms import EditProfileForm

# Create your views here.
"""
def user_detail(request,id):
   user = Usuario.objects.get(id=id)

   return render(request, 'profile.html', {'user':user} )
"""


def agency_detail_edit(request, id):

    agency = get_object_or_404(Agencia, pk=id)

    dataAgency = {}

    for key, value in vars(agency).items():
        if key in ['descripcion', 'telefono', 'direccion', 'correo']:
            dataAgency[key] = value

    if request.method == 'POST':

        form = EditProfileForm(request.POST)

        if form.is_valid():

            dataForm = form.cleaned_data

            if dataForm['descripcion']:
                agency.descripcion = dataForm['descripcion']
            if dataForm['telefono']:
                agency.descripcion = dataForm['telefono']
            if dataForm['direccion']:
                agency.descripcion = dataForm['direccion']
            if dataForm['correo']:
                agency.descripcion = dataForm['correo']

            agency.save()

            return redirect('/accounts/agencia/1/edit/')

    else:

        form = EditProfileForm()

    return render(request, 'profile_edit.html', {'agencia': agency, 'agencia_formulario': zip(list(dataAgency.values()), form)})
