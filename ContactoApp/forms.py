from django import forms


class FormularioContacto(forms.Form):

    nombre=forms.CharField(label=False,required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre'}))
    email=forms.CharField(label=False,required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email'}))
    contenido=forms.CharField(label=False,widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Contenido'}))