from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms


class FormularioInicioSesion(AuthenticationForm):

    username = UsernameField(label=False, widget=forms.TextInput(attrs={
                             "autofocus": True, 'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(label=False, strip=False, widget=forms.PasswordInput(
        attrs={"autocomplete": "current-password", 'class': 'form-control', 'placeholder': 'Contraseña'}),)

    def __init__(self, *args, **kwargs):

        super(FormularioInicioSesion, self).__init__(*args, **kwargs)


class FormularioRegistro(UserCreationForm):

    username = forms.CharField(label=False, max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nombres de usuario'}))
    email = forms.EmailField(label=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}), required=False)
    password1 = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}


class FormularioEditarPerfil(forms.Form):

    email = forms.EmailField(label=False, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(label=False, max_length=30, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    last_name = forms.CharField(label=False, max_length=30, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Apellido'}))
    descripcion = forms.CharField(label=False, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Descripción'}))
    web = forms.URLField(required=False, widget=forms.URLInput(
        attrs={'class': 'form-control', 'placeholder': 'Sitio web'}))
    facebook = forms.URLField(required=False, widget=forms.URLInput(
        attrs={'class': 'form-control', 'placeholder': 'Facebook'}))
    twitter = forms.URLField(required=False, widget=forms.URLInput(
        attrs={'class': 'form-control', 'placeholder': 'Twitter'}))
    instagram = forms.URLField(required=False, widget=forms.URLInput(
        attrs={'class': 'form-control', 'placeholder': 'Instagram'}))
    avatar = forms.ImageField(label=False, required=False)
