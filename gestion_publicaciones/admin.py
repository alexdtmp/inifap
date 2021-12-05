from django.contrib import admin
from .models import Revision, Estado

from gestion_publicaciones.models import Revision, Estado

# Register your models here.
admin.site.register(Revision)
admin.site.register(Estado)
