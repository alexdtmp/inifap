from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Postulante(User):
    segundo_apellido = models.CharField('Segundo apellido', max_length=50)


class Revisor(User):
    segundo_apellido = models.CharField('Segundo apellido', max_length=50)
