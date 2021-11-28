from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('lista', views.UsuarioList.as_view(), name='lista'),
    path('nuevo', views.UsuarioNuevo.as_view(), name='nuevo'),
    path('eliminar/<int:pk>', views.UsuarioEliminar.as_view(), name='eliminar'),
    path('login', views.login, name='login'),
]
