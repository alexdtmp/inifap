from django.urls import path
from . import views

app_name = 'publicaciones'

urlpatterns = [
    path("", views.InicioView.as_view(), name="inicio"),
    path('mis-publicaciones/', views.MisPublicacionesList.as_view(),
         name='mis-publicaciones'),
    path('mis-publicaciones/nueva',
         views.PublicacionNueva.as_view(), name='nueva_publicacion'),
]
