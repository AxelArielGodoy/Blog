from email.policy import default
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.db import models


class MasDatosUsuarios(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(User, max_length=280, null=True, blank=True)
    last_name = models.CharField(User, max_length=280, null=True, blank=True)
    descripcion = models.CharField(
        default="No hay descripción", max_length=280, null=True, blank=True)
    web = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)


    class Meta:

        verbose_name = "usuario"
        verbose_name_plural = "usuarios"


    def __str__(self):

        return f"""
            {self.user}
            {self.descripcion}
            {self.web}
            {self.facebook}
            {self.twitter}
            {self.instagram}
            {self.avatar}"""


    def avatarAdmin(self):
        if self.avatarAdmin:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.avatar.url)
        else:
            return 'Sin avatar'
    avatarAdmin.short_description = 'Avatar'
