from .views import blog, crear_post, buscar_post, post, editar_post, DeleteView
from django.urls import path


urlpatterns = [
    path("", blog, name='blog'),
    path('crear_post/', crear_post, name='crear_post'),
    path('buscar_post/', buscar_post, name='buscar_post'),
    path('post/<int:id>/', post, name='post'),
    path('editar_post/<int:id>/', editar_post, name='editar_post'),
    path('<pk>/eliminar/', DeleteView.as_view(), name='desea_eliminar'),
]
