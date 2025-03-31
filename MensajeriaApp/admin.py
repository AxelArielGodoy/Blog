from django.contrib import admin
from .models import Mensaje

class MensajeAdmin(admin.ModelAdmin):

    reaonly_fields = ('creado',)
    list_display = ( 'remitente', 'destinatario', 'contenido')

admin.site.register(Mensaje, MensajeAdmin)