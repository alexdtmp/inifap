from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls.base import reverse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib import messages
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

def login(request):

    if request.method == 'POST':

        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(username=username, password=password)

        if usuario is not None:

            if usuario.is_active:

                auth_login(request, usuario)
                return redirect('usuarios:lista')
        else:

            messages.error(request, 'El usuario o la contraseña no son correctos')
            return redirect('usuarios:login')
    else:

        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
