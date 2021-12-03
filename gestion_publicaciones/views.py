from django.contrib.auth.models import Group
from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from gestion_publicaciones.models import Revision
from publicaciones.models import Publicacion
from usuarios.models import Usuario

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

def mostrar_lista_revisores(request, pk):

    publicacion_seleccionada = get_object_or_404(Publicacion,id=pk)
    usuarios = Usuario.objects.filter().all()
    revisores = []
    for usuario in usuarios:

        if es_revisor(usuario):

            revisores.append(usuario)
    context = {'publicacion': publicacion_seleccionada,
               'revisores': revisores}
    return render(request, 'revisores_list.html',context)
        
def es_revisor(user):

    return user.groups.filter(name='Revisor').exists()

def asignar_revisores(request):

    if request.method=='POST':
        
        
    