from django.test import TestCase
from django.urls import reverse
from publicaciones.models import Publicacion
from usuarios.models import Usuario
from catalogos.models import Estatus
from gestion_publicaciones.models import Revision

# Create your tests here.
class TestViews(TestCase):

    def test_insercion_revision_bd(self):

        estatus_nuevo = Estatus.objects.create(descripcion='en espera')
        estatus_nuevo.save()
        usuario = Usuario.objects.create(nombre='Germán',
                                         primer_apellido='González',
                                         segundo_apellido='Rodarte',
                                         correo_electronico='38192814@uaz.edu.mx',
                                         username='germanglez',
                                         password='german$123',)
        usuario.save()
        publicacion_nueva = Publicacion.objects.create(archivo='archivo_prueba.txt',
                                                 estatus=estatus_nuevo,
                                                 autor=usuario,
                                                 titulo="Prueba")
        revision = Revision.objects.create(publicacion=publicacion_nueva,
                                           usuario_revisor=usuario,
                                           archivo='archivo_prueba.txt')
        self.assertEquals(revision,
                          Revision.objects.filter(id=revision.id).first())

    def test_insercion_revision_sin_usuario_revisor(self):

        estatus_nuevo = Estatus.objects.create(descripcion='en espera')
        estatus_nuevo.save()
        usuario = Usuario.objects.create(nombre='Germán',
                                         primer_apellido='González',
                                         segundo_apellido='Rodarte',
                                         correo_electronico='38192814@uaz.edu.mx',
                                         username='germanglez',
                                         password='german$123',)
        usuario.save()
        publicacion_nueva = Publicacion.objects.create(archivo='archivo_prueba.txt',
                                                 estatus=estatus_nuevo,
                                                 autor=usuario,
                                                 titulo="Prueba")
        revision = Revision.objects.create(publicacion=publicacion_nueva,
                                           usuario_revisor=None,
                                           archivo='archivo_prueba.txt')
        self.assertEquals(revision,
                          Revision.objects.filter(id=revision.id).first())
    
    def test_insercion_revision_sin_archivo_revision(self):
    
        estatus_nuevo = Estatus.objects.create(descripcion='en espera')
        estatus_nuevo.save()
        usuario = Usuario.objects.create(nombre='Germán',
                                         primer_apellido='González',
                                         segundo_apellido='Rodarte',
                                         correo_electronico='38192814@uaz.edu.mx',
                                         username='germanglez',
                                         password='german$123',)
        usuario.save()
        publicacion_nueva = Publicacion.objects.create(archivo='archivo_prueba.txt',
                                                 estatus=estatus_nuevo,
                                                 autor=usuario,
                                                 titulo="Prueba")
        revision = Revision.objects.create(publicacion=publicacion_nueva,
                                           usuario_revisor=None,
                                           archivo=None)
        self.assertEquals(revision,
                          Revision.objects.filter(id=revision.id).first())