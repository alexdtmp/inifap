from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class TestViews(TestCase):

    def test_url_publicaciones_lista(self):
    
        response = self.client.get('/gestion-publicaciones/lista-publicaciones')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_publicaciones_lista(self):

        response = self.client.get(reverse('gestion_publicaciones:lista_publicaciones'))
        self.assertEqual(response.status_code, 200)

    def test_template_correcto_publicaciones_lista(self):
    
        response = self.client.get('/gestion-publicaciones/lista-publicaciones')
        self.assertTemplateUsed(response, 'publicaciones_list.html')

    def test_envio_datos_url_publicaciones_lista(self):

        response = self.client.get(reverse('gestion_publicaciones:lista_publicaciones'))
        self.assertIn('object_list', response.context)