from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from publicaciones.forms import PublicacionForm
from publicaciones.models import Publicacion
from gestion_publicaciones.models import Revision
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages

from usuarios.models import Usuario


# Lista de publicaciones
class MisPublicacionesList(PermissionRequiredMixin, ListView):
    permission_required = 'publicaciones.add_publicacion'
    template_name = "mis_publicaciones_list.html"
    model = Publicacion

# Página de inicio

# Lista de revisiones pendientes (publicaciones)
class RevisionesList(PermissionRequiredMixin, ListView):
    permission_required = 'publicaciones.view_publicacion'
    template_name = 'publicaciones_revisar_list.html'
    model = Revision
    
    def get_queryset(self):
        usuario_actual = self.request.user
        return Revision.objects.filter(usuario_revisor = usuario_actual.id)


class InicioView(TemplateView):
    template_name = "inicio.html"

# Nueva publicación


class PublicacionNueva(PermissionRequiredMixin, CreateView):
    permission_required = 'publicaciones.add_publicacion'
    template_name = "publicacion_create.html"
    model = Publicacion
    form_class = PublicacionForm
    success_url = reverse_lazy('publicaciones:mis-publicaciones')

    def post(self, request, *args, **kwargs):
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            nueva_publicacion = Publicacion(archivo=request.FILES['archivo'])
            nueva_publicacion.titulo = request.POST['titulo']
            nueva_publicacion.autor = Usuario.objects.filter(
                id=request.user.id).first()
            nueva_publicacion.save()
            messages.success(
                request, 'Tu publicación se ha cargado con éxito y pronto será revisada')
            return redirect('/mis-publicaciones/')
        else:
            return redirect('/mis-publicaciones/')


def handler403(request, *args, **argv):
    response = render('403.html', {},
                      context_instance=RequestContext(request))
    response.status_code = 403
    return response
