from .forms import FormularioInicioSesion, FormularioRegistro, FormularioEditarPerfil
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import MasDatosUsuarios
from BlogApp.models import Post
from MensajeriaApp.models import Mensaje


def iniciar_sesion(request):

    if request.method == 'POST':

        form_login = FormularioInicioSesion(request, data=request.POST)

        if form_login.is_valid():

            username = form_login.cleaned_data.get('username')
            password = form_login.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:

                django_login(request, user)
                return redirect('inicio')

            else:

                return render(request, 'accounts/iniciar_sesion.html', {'form_login': form_login})
        else:

            return render(request, 'accounts/iniciar_sesion.html', {'form_login': form_login})

    form_login = FormularioInicioSesion()

    return render(request, 'accounts/iniciar_sesion.html', {'form_login': form_login})


def registro(request):

    if request.method == 'POST':

        formulario_registro = FormularioRegistro(request.POST)

        if formulario_registro.is_valid():

            formulario_registro.save()
            return redirect('iniciar_sesion')

        else:

            return render(request, 'accounts/registro.html', {'formulario_registro': formulario_registro})

    formulario_registro = FormularioRegistro()

    return render(request, 'accounts/registro.html', {'formulario_registro': formulario_registro})


@login_required
def perfil(request):

    posts = Post.objects.filter(autor_id=request.user.id)
    masdatosusuarios = MasDatosUsuarios.objects.filter(id=request.user.id)
    cantidad_mensajes= Mensaje.objects.filter(leido=False).filter(destinatario=request.user).count()

    return render(request, 'accounts/perfil.html', {'posts': posts, 'masdatosusuarios': masdatosusuarios,'cantidad_mensajes':cantidad_mensajes})


@login_required
def editar_perfil(request):

    user = request.user
    mas_datos_usuarios, _ = MasDatosUsuarios.objects.get_or_create(user=user)

    if request.method == 'POST':

        form_edit = FormularioEditarPerfil(request.POST, request.FILES)

        if form_edit.is_valid():

            data = form_edit.cleaned_data
            mas_datos_usuarios.first_name = data.get('first_name') if data.get(
                'first_name') else mas_datos_usuarios.first_name
            mas_datos_usuarios.last_name = data.get('last_name') if data.get(
                'last_name') else mas_datos_usuarios.last_name
            user.email = data.get('email') if data.get('email') else user.email
            mas_datos_usuarios.descripcion = data.get('descripcion') if data.get(
                'descripcion') else mas_datos_usuarios.descripcion
            mas_datos_usuarios.web = data.get('web') if data.get(
                'web') else mas_datos_usuarios.web
            mas_datos_usuarios.facebook = data.get('facebook') if data.get(
                'facebook') else mas_datos_usuarios.facebook
            mas_datos_usuarios.twitter = data.get('twitter') if data.get(
                'twitter') else mas_datos_usuarios.twitter
            mas_datos_usuarios.instagram = data.get('instagram') if data.get(
                'instagram') else mas_datos_usuarios.instagram
            mas_datos_usuarios.avatar = data.get('avatar') if data.get(
                'avatar') else mas_datos_usuarios.avatar

            user.save()
            mas_datos_usuarios.save()

            return redirect('perfil')

        else:

            return render(request, 'accounts/editar_perfil.html', {'form_edit': form_edit})

    form_edit = FormularioEditarPerfil(
        initial={
            'email': user.email,
            'nombre': mas_datos_usuarios.first_name,
            'apellido': mas_datos_usuarios.last_name,
            'descripcion': mas_datos_usuarios.descripcion,
            'web': mas_datos_usuarios.web,
            'facebook': mas_datos_usuarios.facebook,
            'twitter': mas_datos_usuarios.twitter,
            'instagram': mas_datos_usuarios.instagram,
            'avatar': mas_datos_usuarios.avatar, })

    return render(request, 'accounts/editar_perfil.html', {'form_edit': form_edit})


def perfil_usuario(request, id):

    posts = Post.objects.filter(autor=id)
    masdatosusuarios = MasDatosUsuarios.objects.get(user=id)

    cantidad_mensajes= Mensaje.objects.filter(leido=False).filter(destinatario=request.user).count()
    return render(request, 'accounts/perfil_usuario.html', {"posts": posts, "masdatosusuarios": masdatosusuarios,"cantidad_mensajes":cantidad_mensajes})


class ChangePasswordView(PasswordChangeView, PasswordChangeDoneView):

    template_name = 'accounts/cambiar_contrasegna.html'
