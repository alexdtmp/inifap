from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from gestion_publicaciones.models import Revision
from publicaciones.models import Publicacion

# Create your views here.
class PublicacionesList(ListView):

    model = Publicacion
    template_name = 'publicaciones_list.html'

def detalle_publicacion(request, pk):
    
    publicacion_seleccionada = get_object_or_404(Publicacion,id=pk)
    revisiones = Revision.objects.filter(publicacion=publicacion_seleccionada)
    if revisiones.count()!=0:
        
        context = {'publicacion': publicacion_seleccionada,
                   'revisiones': revisiones}
    else:

        context = {'publicacion': publicacion_seleccionada}
    return render(request, 'publicacion_detail.html',context)    
