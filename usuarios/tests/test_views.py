from django.test import TestCase
from django.urls import reverse
from usuarios.models import Usuario


# Create your tests here.
class TestViews(TestCase):

# Test crear usuario y lista usuario
    def setUp(self):

        self.data_usuario = {
            'nombre': 'Germán',
            'primer_apellido': 'González',
            'segundo_apellido': '',
            'correo_electronico': '38192814@uaz.edu.mx',
            'username': 'germanglez',
            'password': 'german$123',
        }

    def test_url_usuarios_lista(self):

        response = self.client.get('/usuarios/lista')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_usuarios_lista(self):

        response = self.client.get(reverse('usuarios:lista'))
        self.assertEqual(response.status_code, 200)

    def test_template_correcto_nuevo_usuario(self):

        response = self.client.get('/usuarios/lista')
        self.assertTemplateUsed(response, 'usuarios/usuario_list.html')

    def test_envio_datos_url_usuarios_lista(self):

        response = self.client.get(reverse('usuarios:lista'))
        self.assertIn('object_list', response.context)

    def test_url_usuarios_crear(self):

        response = self.client.get('/usuarios/nuevo')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_usuarios_crear(self):

        response = self.client.get(reverse('usuarios: nuevo'))
        self.assertEqual(response.status_code, 200)

    def test_template_correcto_nuevo_usuario(self):

        response = self.client.get('/usuarios/nuevo')
        self.assertTemplateUsed(response, 'usuarios/usuario_form.html')

    def test_agrega_usuario_form(self):

        self.client.post('/usuarios/nuevo', data=self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(), 1)

    def test_no_agrega_sin_username(self):

        self.data_usuario['username'] = ''
        self.client.post('/usuarios/nuevo', data=self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(), 0)

    def test_no_agrega_con_username_con_espacios(self):

        self.data_usuario['username'] = 'german glez'
        self.client.post('/usuarios/nuevo', data=self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(), 0)

    def test_no_agrega_usuario_sin_correo(self):

        self.data_usuario['correo_electronico'] = ''
        self.client.post('/usuarios/nuevo', data=self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(), 0)

    def test_no_agrega_usuario_correo_con_espacios(self):

        self.data_usuario['correo_electronico'] = '38192814 @uaz.edu.mx'
        self.client.post('/usuarios/nuevo', data=self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(), 0)

    def test_no_agrega_usuario_correo_min_caracteres(self):
        self.data_usuario['correo_electronico'] = '3@'
        self.client.post('/usuarios/nuevo', data=self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(), 0)

    def test_no_agrega_usuario_correo_max_caracteres(self):

        self.data_usuario['correo_electronico'] = '38192814@uaz.edu.mx' * 2
        self.client.post('/usuarios/nuevo', data=self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(), 0)

    def test_no_agrega_usuario_sin_password(self):

        self.data_usuario['password'] = ''
        self.client.post('/usuarios/nuevo', data=self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(), 0)

    def test_no_agrega_usuario_sin_nombre(self):

        self.data_usuario['nombre'] = ''
        self.client.post('/usuarios/nuevo', data=self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(), 0)

    def test_no_agrega_usuario_nombre_max_caracteres(self):

        self.data_usuario['nombre'] = 'Germán'*20
        self.client.post('/usuarios/nuevo', data=self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(), 0)

    def test_no_agrega_usuario_sin_primer_apellido(self):

        self.data_usuario['primer_apellido'] = ''
        self.client.post('/usuarios/nuevo', data=self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(), 0)

    def test_no_agrega_usuario_primer_apellido_max_caracteres(self):

        self.data_usuario['primer_apellido'] = 'González' * 15
        self.client.post('/usuarios/nuevo', data=self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(), 0)

    def test_agrega_usuario_con_segundo_apellido(self):

        self.data_usuario['segundo_apellido'] = 'Rodarte'
        self.client.post('/usuarios/nuevo', data=self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(), 1)

    def test_no_agrega_usuario_segundo_apellido_max_caracteres(self):

        self.data_usuario['segundo_apellido'] = 'Rodarte' * 20
        self.client.post('/usuarios/nuevo', data=self.data_usuario)
        self.assertEqual(Usuario.objects.all().count(), 0)

    def test_redirige_despues_de_agregar_usuario(self):

        response = self.client.post('/usuarios/nuevo', data=self.data_usuario)
        self.assertEqual(response.url, '/usuarios/lista')

#Login
    def test_url_usuarios_login(self):

        response = self.client.get('/usuarios/login')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_usuarios_login(self):

        response = self.client.get(reverse('usuarios:login'))
        self.assertEqual(response.status_code, 200)

    def test_template_correcto_usuarios_login(self):

        response = self.client.get('/usuarios/login')
        self.assertTemplateUsed(response, 'login.html')
