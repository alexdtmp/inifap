from django import forms
from .models import Publicacion


class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        exclude = ('estatus', 'autor', 'fecha_publicacion')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la publicación'}),
        }
