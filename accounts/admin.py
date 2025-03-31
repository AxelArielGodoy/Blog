from .models import MasDatosUsuarios
from django.contrib import admin


class MasDatosUsuariosAdmin(admin.ModelAdmin):

    reaonly_fields = ('user', 'descripcion', 'first_name', 'last_name')
    list_display = ( 'user', 'descripcion',
                    'first_name', 'last_name')

    def __str__(self):

        return "user"
    

admin.site.register(MasDatosUsuarios, MasDatosUsuariosAdmin)
