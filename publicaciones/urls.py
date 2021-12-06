from django.urls import path
from . import views

app_name = 'publicaciones'

urlpatterns = [
     path("", views.InicioView.as_view(), name="inicio"),
     path('mis-publicaciones/', views.MisPublicacionesList.as_view(),
         name='mis_publicaciones'),
     path('mis-publicaciones/nueva/',
         views.PublicacionNueva.as_view(), name='nueva_publicacion'),
     path('revisar-publicaciones/', views.RevisionesList.as_view(),
          name='revisar_publicaciones'),
     path("revisar-publicaciones/detalle/<int:pk>/", views.RevisionDetail.as_view(), name="detalle_revision"),
     
]
