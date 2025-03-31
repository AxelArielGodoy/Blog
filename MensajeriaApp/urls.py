from .views import buzon, eliminar_mensaje, ver_mensaje,enviar_mensaje
from django.urls import path


urlpatterns = [
    path("buzon/", buzon, name='buzon'),
    path('<int:id>/', ver_mensaje, name='ver_mensaje'),
    path('eliminar/<int:id>/', eliminar_mensaje, name='eliminar_mensaje'),
    path('enviar_mensaje/<int:id>/', enviar_mensaje, name='enviar_mensaje'),

]
