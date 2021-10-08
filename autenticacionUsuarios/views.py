from django.http import request, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Usuario, Agencia
from autenticacionUsuarios.forms import EditProfileForm, LoginUserForm, RegisterUserForm

# create users

def registro_usuario(request):

    if request.method == "POST":

        registerForm = RegisterUserForm(request.POST)

        if registerForm.is_valid():

            user = None
            userData = registerForm.cleaned_data

            # validation if exist data in the fields

            if userData['contraseña'] and userData['correo'] and userData['nombre'] and userData['confirmacion_contraseña']:

                if userData['contraseña'] == userData['confirmacion_contraseña']:

                    contraseña = userData['contraseña']
                else:
                    return redirect('/accounts/register/')

                nombre = userData['nombre']
                correo = userData['correo']

                if userData['agencia']:

                    user = Agencia(nombre=nombre, correo=correo,
                                   contraseña=contraseña)
                elif userData['usuario']:

                    user = Usuario(nombre=nombre, correo=correo,
                                   contraseña=contraseña)
                else:

                    return redirect('/accounts/register/')

                user.save()

                return render(request,'registroExitoso.html')
            else:
                return redirect('/accounts/register/')

        return render(request, "gracias.html")
    else:
        registerForm = RegisterUserForm()

    context = {
        'formulario': registerForm
    }

    return render(request, "registrar.html", context)

# Iniciar Sesion User


def iniciar_usuario(request):
    if request.method == "POST":
        loginForm = LoginUserForm(request.POST)

        if loginForm.is_valid():

            user = None
            userData = loginForm.cleaned_data
            correo = userData["correo"]
            contraseña = userData["contraseña"]

            if correo and contraseña:
                user = get_object_or_404(Usuario, correo=correo)
                user_or_agency = user.__class__.__name__
                """
            userUnique = {}

            for key, value in vars(user).items():

                if key in ['correo', 'contraseña']:
                    userUnique[key] = value
                    """

                print(user)

                if user.contraseña == contraseña:

                    return render(request, 'inicioExitoso.html', {'user_or_agency':user_or_agency,'id': user.id})

            else:
                redirect("/accounts/login")

        else:
            redirect("/accounts/login")

    else:
        loginForm = LoginUserForm()

    context = {
        'formulario': loginForm
    }
    return render(request, "login.html", context)

# read and update users


def agency_detail_edit(request,user_or_agency, id):

    if user_or_agency.lower() == 'agencia':
        user_or_agency_logged = get_object_or_404(Agencia, pk=id)
    elif user_or_agency.lower() == 'usuario':
        user_or_agency_logged = get_object_or_404(Usuario, pk=id)
    else:
        return HttpResponse("No especificaste un usuario valido")

    dataAgency = {}

    for key, value in vars(user_or_agency_logged).items():

        if key in ['descripcion', 'telefono', 'direccion', 'correo']:
            dataAgency[key] = value

    if request.method == 'POST':

        form = EditProfileForm(request.POST)

        if form.is_valid():

            dataForm = form.cleaned_data

            if dataForm['descripcion']:
                user_or_agency_logged.descripcion = dataForm['descripcion']

            if dataForm['telefono']:
                user_or_agency_logged.telefono = dataForm['telefono']

            if dataForm['direccion']:
                user_or_agency_logged.direccion = dataForm['direccion']

            if dataForm['correo']:
                user_or_agency_logged.correo = dataForm['correo']

            user_or_agency_logged.save()

            return redirect(f'/accounts/{user_or_agency.lower()}/{id}/edit/')

    else:

        form = EditProfileForm()

    if user_or_agency.lower()  == "agencia":
        return render(request, 'profile_edit.html', {'agencia': user_or_agency_logged, 'agencia_formulario': zip(list(dataAgency.values()), form)})
        
    elif user_or_agency.lower() == "usuario":
        
        return render(request, 'profile_usuario.html', {'usuario': user_or_agency_logged, 'usuario_formulario': zip(list(dataAgency.values()), form)})


def agency_delete(request, id):

    agencia = get_object_or_404(Agencia, pk=id)

    nombre = agencia.nombre
    correo = agencia.correo

    agencia.delete()

    contexto = {
        'nombre': nombre,
        'correo': correo,
    }

    return render(request, 'delete.html', contexto)
