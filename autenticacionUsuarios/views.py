from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from .models import Usuario, Agencia
from autenticacionUsuarios.forms import EditProfileForm, RegisterUserForm

# create users

def registro_usuario(request):

    if request.method == "POST":

        registerForm = RegisterUserForm(request.POST)

        if registerForm.is_valid():

            user = None
            userData = registerForm.cleaned_data

            #validation if exist data in the fields
            
            if userData['contraseña'] and userData['correo'] and userData['nombre'] and userData['confirmacion_contraseña']:
                
                if userData['contraseña'] == userData['confirmacion_contraseña']:

                    contraseña = userData['contraseña']
                else:
                    return redirect('/accounts/register/')

                nombre = userData['nombre']
                correo = userData['correo']

                if userData['agencia']:

                    user = Agencia(nombre=nombre, correo=correo, contraseña=contraseña)
                elif userData['usuario']:

                    user = Usuario(nombre=nombre, correo=correo, contraseña=contraseña)
                else:

                    return redirect('/accounts/register/')
                    
                user.save()

                return redirect('/accounts/register/success/')
            else:
                return redirect('/accounts/register/')
                

        return render(request, "gracias.html")
    else:
         registerForm = RegisterUserForm()
    
    context = {
        'formulario':registerForm
    }
    
    return render(request, "registrar.html", context)


# read and update users

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
                agency.telefono = dataForm['telefono']

            if dataForm['direccion']:
                agency.direccion = dataForm['direccion']

            if dataForm['correo']:
                agency.correo = dataForm['correo']

            agency.save()

            return redirect(f'/accounts/agencia/{id}/edit/')

    else:

        form = EditProfileForm()

    return render(request, 'profile_edit.html', {'agencia': agency, 'agencia_formulario': zip(list(dataAgency.values()), form)})

def agency_delete(request, id):

    agencia = get_object_or_404(Agencia, pk=id)

    nombre = agencia.nombre
    correo = agencia.correo

    agencia.delete()
    
    contexto={
        'nombre':nombre,
        'correo':correo,
    }

    return render(request,'delete.html',contexto)
