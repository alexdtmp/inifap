from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls.base import reverse
from django.contrib.messages.views import SuccessMessageMixin
from .models import Usuario
from .forms import UsuarioForm


# Create your views here.
class UsuarioList(ListView):

    model = Usuario


class UsuarioNuevo(SuccessMessageMixin, CreateView):

    model = Usuario
    form_class = UsuarioForm
    success_message = "Usuario creado correctamente"

    def get_success_url(self):

        return reverse('usuarios:lista')