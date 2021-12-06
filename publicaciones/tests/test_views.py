import datetime
from django.test import TestCase
from publicaciones.models import Publicacion
from catalogos.models import Estatus
from django.contrib.auth.models import Permission

from usuarios.models import Usuario


# Create your tests here.
class TestViews(TestCase):

    def setUp(self):
        self.user = Usuario.objects.create(username='user', password='pass')
        self.user.save()

    # Probar que hay una página en la url raíz
    def test_url_inicio(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    # Probar que la página en la url raíz utiliza el template 'inicio.html'
    def test_template_inicio(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'inicio.html')

    # Probar que existe una página web en la direccion mis-publicaciones
    def test_url_mis_publicaciones(self):
        # login con usuario recién creado
        self.client.login(username='user', password='pass')
        # asignar permisos al user
        id_permiso = Permission.objects.filter(
            codename='add_publicacion').first()
        self.user.user_permissions.add(id_permiso)
        response = self.client.get('/mis-publicaciones/')
        self.assertEqual(response.status_code, 200)

    # Probar que la página en la dirección de mis 
    # publicaciones utiliza el template 'mis_publicaciones_list.html'
    def test_template_mis_publicaciones(self):
        # login con usuario recién creado
        self.client.login(username='user', password='pass')
        # asignar permisos al user
        id_permiso = Permission.objects.filter(
            codename='view_publicacion').first()
        self.user.user_permissions.add(id_permiso)
        response = self.client.get('/mis-publicaciones/')
        self.assertTemplateUsed(response, 'mis_publicaciones_list.html')

    # Probar que existe una página web en la direccion mis-publicaciones/nueva
    def test_url_nueva_publicacion(self):
        # login con usuario recién creado
        self.client.login(username='user', password='pass')
        # asignar permisos al user
        id_permiso = Permission.objects.filter(
            codename='add_publicacion').first()
        self.user.user_permissions.add(id_permiso)
        response = self.client.get('/mis-publicaciones/nueva/')
        self.assertEqual(response.status_code, 200)

     # Probar que la página en la dirección '/mis-publicaciones/nueva' 
     # utiliza el template 'publicacion_create.html'
    def test_template_nueva_publicacion(self):
        # login con usuario recién creado
        self.client.login(username='user', password='pass')
        # asignar permisos al user
        id_permiso = Permission.objects.filter(
            codename='add_publicacion').first()
        self.user.user_permissions.add(id_permiso)
        response = self.client.get('/mis-publicaciones/nueva/')
        self.assertTemplateUsed(response, 'publicacion_create.html')

    # Probar envío de datos consultando 
    # desde el ListView del modelo 'Publicacion'
    def test_envio_datos_publicacion(self):
        # login con usuario recién creado
        self.client.login(username='user', password='pass')
        # asignar permisos al user
        id_permiso = Permission.objects.filter(
            codename='view_publicacion').first()
        self.user.user_permissions.add(id_permiso)
        response = self.client.get('/mis-publicaciones/')
        self.assertIn('object_list', response.context)

    # Probar envío del título de la publicación 
    # desde el ListView del modelo 'Publicacion'
    def test_envio_nombre_publicacion(self):
        # login con usuario recién creado
        self.client.login(username='user', password='pass')
        # asignar permisos al user
        id_permiso = Permission.objects.filter(
            codename='view_publicacion').first()
        self.user.user_permissions.add(id_permiso)
        self.agrega_publicacion()
        response = self.client.get('/mis-publicaciones/')
        self.assertEquals('Prueba', response.context['object_list'][0].titulo)

    # Probar envío del estatus de la publicación 
    # desde el ListView del modelo 'Publicacion'
    def test_envio_estatus_publicacion(self):
        # login con usuario recién creado
        self.client.login(username='user', password='pass')
        # asignar permisos al user
        id_permiso = Permission.objects.filter(
            codename='view_publicacion').first()
        self.user.user_permissions.add(id_permiso)
        self.agrega_publicacion()
        response = self.client.get('/mis-publicaciones/')
        self.assertEquals(
            'en espera', response.context['object_list'][0].estatus.descripcion)

    # Probar envío de la fecha de la publicación 
    # desde el ListView del modelo 'Publicacion'
    def test_envio_fecha_publicacion(self):
        # login con usuario recién creado
        self.client.login(username='user', password='pass')
        # asignar permisos al user
        id_permiso = Permission.objects.filter(
            codename='view_publicacion').first()
        self.user.user_permissions.add(id_permiso)
        self.agrega_publicacion()
        response = self.client.get('/mis-publicaciones/')
        fecha = response.context['object_list'][0].fecha_publicacion
        self.assertEquals(datetime.date.today().strftime(
            '%d/%m/%Y'), fecha.strftime('%d/%m/%Y'))

    # Probar envío del autor de la publicación 
    # desde el ListView del modelo 'Publicacion'
    def test_envio_autor_publicacion(self):
        # login con usuario recién creado
        self.client.login(username='user', password='pass')
        # asignar permisos al user
        id_permiso = Permission.objects.filter(
            codename='view_publicacion').first()
        self.user.user_permissions.add(id_permiso)
        self.agrega_publicacion()
        response = self.client.get('/mis-publicaciones/')
        self.assertEquals(
            'autor_prueba', response.context['object_list'][0].autor.username)

    # Probar acceso restringido a la creación de 
    # publicaciones para usuarios que no tienen el permiso
    def test_nueva_publicacion_403(self):
        # login con usuario recién creado
        self.client.login(username='user', password='pass')
        response = self.client.get('/mis-publicaciones/nueva/')
        self.assertEqual(response.status_code, 403)

    # Probar acceso restringido a la view de 
    # MisPublicacionesList para usuarios que no tienen el permiso
    def test_mis_publicacion_403(self):
        # login con usuario recién creado
        self.client.login(username='user', password='pass')
        response = self.client.get('/mis-publicaciones/')
        self.assertEqual(response.status_code, 403)

    # Agregar una nueva publicación
    def agrega_publicacion(self):
        Publicacion.objects.create(
            archivo='archivo_prueba.txt',
            estatus=Estatus.objects.create(
                descripcion='en espera'),  # Estatus pendiente
            autor=Usuario.objects.create(
                username='autor_prueba', password='contra123'),
            titulo="Prueba"
        )
