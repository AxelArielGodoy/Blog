from email.message import Message
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from MensajeriaApp.forms import FormularioMensaje
from MensajeriaApp.models import Mensaje
from django.contrib.auth.models import User


def buzon(request):

    recibidos = Mensaje.objects.filter(destinatario=request.user).order_by("-id")
    enviados = Mensaje.objects.filter(remitente=request.user).order_by("-id")
    

    cantidad_mensajes= Mensaje.objects.filter(leido=False).filter(destinatario=request.user).count()


    return render(request, 'buzon.html',{"recibidos":recibidos,'cantidad_mensajes':cantidad_mensajes,'enviados':enviados})

def ver_mensaje(request, id):

    mensaje = Mensaje.objects.get(id=id)

    if mensaje.leido == False:
        mensaje.leido = True
    mensaje.save()
    

    return render(request, "ver_mensaje.html", {"mensaje":mensaje})

def enviar_mensaje(request,id):

    destinatario = User.objects.get(id=id)

    if request.method == "POST":

        formulario_mensaje = FormularioMensaje(request.POST, request.FILES)

        if formulario_mensaje.is_valid():

            informacion = formulario_mensaje.cleaned_data
            contenido = Mensaje(
                contenido=informacion['contenido'])
            contenido.remitente = request.user
            contenido.destinatario = destinatario

            contenido.save()

            return redirect('buzon')

    else:
        formulario_mensaje = FormularioMensaje()

    return render(request, "enviar_mensaje.html",{"destinatario":destinatario,"formulario_mensaje":formulario_mensaje})


@ login_required
def eliminar_mensaje(request, id):

    mensaje = Mensaje.objects.get(id=id)
    mensaje.delete()

    return redirect('buzon')
