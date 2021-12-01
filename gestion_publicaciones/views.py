from django.shortcuts import render
from django.views.generic import ListView
from publicaciones.models import Publicacion

# Create your views here.
class PublicacionesList(ListView):

    model = Publicacion
    template_name = 'publicaciones_list.html'