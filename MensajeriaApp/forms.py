from ckeditor.fields import RichTextFormField
from django import forms


class FormularioMensaje(forms.Form):


    contenido = RichTextFormField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'contenido'}), label="")