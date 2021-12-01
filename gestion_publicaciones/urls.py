from django.urls import path
from . import views

app_name = 'gestion_publicaciones'

urlpatterns = [
    path('lista-publicaciones', views.PublicacionesList.as_view(),
         name='lista_publicaciones'),
]