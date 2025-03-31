from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acerca_de/', include('AcercaDeApp.urls')),
    path('blog/', include('BlogApp.urls')),
    path('contacto/', include('ContactoApp.urls')),
    path('accounts/', include('accounts.urls')),
    path('mensajes/', include('MensajeriaApp.urls')),
    path('', include('LibreriaCoderApp.urls')),
]