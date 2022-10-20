from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UsuarioForm
# Create your views here.


class UsuarioCreate(CreateView):
    template_name = "usuarios/form_registrar.html"
    form_class = UsuarioForm
    sucess_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Usuário'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'success'
        return context 