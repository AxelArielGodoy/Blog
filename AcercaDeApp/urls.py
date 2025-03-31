from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import acerca_de


urlpatterns = [
    path("", acerca_de, name='acerca_de'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  