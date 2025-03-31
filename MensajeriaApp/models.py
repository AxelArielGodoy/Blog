from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Mensaje(models.Model):
     remitente = models.ForeignKey(User, on_delete=models.CASCADE,related_name="remitente")
     destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="destinatario")
     contenido = RichTextField(blank=True, null=True)
     creado = models.DateTimeField(auto_now_add=True)
     leido = models.BooleanField(default=False)