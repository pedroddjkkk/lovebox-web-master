from .models import Cidade, Estado, Paciente, Medicamento, ProfissionalSaude, Cuidador, Tratamento, Lovebox, DosesTratamento

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin

from .forms import PacienteForm, MedicamentoForm, ProfissionalSaudeForm, CuidadorForm, TratamentoForm, LoveboxForm, DosesTratamentoForm

from django.shortcuts import get_object_or_404

class EstadoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u'Admin'
    model = Estado
    fields = ['sigla', 'nome', 'pais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Estados'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context 


class EstadoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u'Admin'
    model = Estado
    fields = ['sigla', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Estado'
        context['botao'] = 'Salvar'
        context['cor'] = 'success'
        return context  

class EstadoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u'Admin'
    model = Estado
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-estado')

class EstadoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u'Admin'
    model = Estado
    template_name = 'cadastros/listas/estados.html'


#######################################
# Criar as views daqui em diante
#######################################

class CidadeCreate(LoginRequiredMixin, CreateView):
    model= Cidade
    fields = ['nome','estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Cidades'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context 

class CidadeUpdate(LoginRequiredMixin, UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cidade'
        context['botao'] = 'Salvar'
        context['cor'] = 'success'
        return context 

class CidadeDelete(LoginRequiredMixin, DeleteView):
    model = Cidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidade')

class CidadeList(LoginRequiredMixin, ListView):
    model = Cidade
    template_name = 'cadastros/listas/cidades.html'

# Paciente

class PacienteCreate(LoginRequiredMixin, CreateView):
    model= Paciente
    form_class = PacienteForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-paciente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Pacientes'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context 

class PacienteUpdate(LoginRequiredMixin, UpdateView):
    model= Paciente
    form_class = PacienteForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-paciente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Paciente'
        context['botao'] = 'Salvar'
        context['cor'] = 'success'
        return context 

class PacienteDelete(LoginRequiredMixin, DeleteView):
    model = Paciente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-paciente')

class PacienteList(LoginRequiredMixin, ListView):
    model = Paciente
    template_name = 'cadastros/listas/pacientes.html'

# Medicamento

class MedicamentoCreate(LoginRequiredMixin, CreateView):
    model= Medicamento
    form_class = MedicamentoForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-medicamento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Medicamento'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context 

class MedicamentoUpdate(LoginRequiredMixin, UpdateView):
    model= Medicamento
    form_class = MedicamentoForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-medicamento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Medicamento'
        context['botao'] = 'Salvar'
        context['cor'] = 'success'
        return context 

class MedicamentoDelete(LoginRequiredMixin, DeleteView):
    model = Medicamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-medicamento')

class MedicamentoList(LoginRequiredMixin, ListView):
    model = Medicamento
    template_name = 'cadastros/listas/medicamento.html'

# ProfissionalSaude

class ProfissionalSaudeCreate(LoginRequiredMixin, CreateView):
    model= ProfissionalSaude
    form_class = ProfissionalSaudeForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-profissional_saude')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Profissional da Saúde'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context 

class ProfissionalSaudeUpdate(LoginRequiredMixin, UpdateView):
    model= ProfissionalSaude
    form_class = ProfissionalSaudeForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-profissional_saude')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Profissional da Saúde'
        context['botao'] = 'Salvar'
        context['cor'] = 'success'
        return context 

class ProfissionalSaudeDelete(LoginRequiredMixin, DeleteView):
    model = ProfissionalSaude
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-profissional_saude')

class ProfissionalSaudeList(LoginRequiredMixin, ListView):
    model = ProfissionalSaude
    template_name = 'cadastros/listas/profissional_saude.html'

#Cuidador

class CuidadorCreate(LoginRequiredMixin, CreateView):
    model= Cuidador
    form_class = CuidadorForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cuidador')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Cuidador'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context 

class CuidadorUpdate(LoginRequiredMixin, UpdateView):
    model= Cuidador
    form_class = CuidadorForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cuidador')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cuidador'
        context['botao'] = 'Salvar'
        context['cor'] = 'success'
        return context 

class CuidadorDelete(LoginRequiredMixin, DeleteView):
    model = Cuidador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cuidador')

class CuidadorList(LoginRequiredMixin, ListView):
    model = Cuidador
    template_name = 'cadastros/listas/cuidador.html'

# Tratamento

class TratamentoCreate(LoginRequiredMixin, CreateView):
    model= Tratamento
    form_class = TratamentoForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tratamento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Tratamento'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context 

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user

        url = super().form_valid(form)

        return url

class TratamentoUpdate(LoginRequiredMixin, UpdateView):
    model= Tratamento
    form_class = TratamentoForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tratamento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Tratamento'
        context['botao'] = 'Salvar'
        context['cor'] = 'success'
        return context
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Tratamento,pk=self.kwargs['pk'], cadastrado_por = self.request.user)
        return self.object

class TratamentoDelete(LoginRequiredMixin, DeleteView):
    model = Tratamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-tratamento')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Tratamento,pk=self.kwargs['pk'], cadastrado_por = self.request.user)
        return self.object

class TratamentoList(LoginRequiredMixin, ListView):
    model = Tratamento
    template_name = 'cadastros/listas/tratamento.html'

    def get_queryset(self):
        self.object_list = Tratamento.objects.filter(cadastrado_por = self.request.user)
        return self.object_list

#Lovebox

class LoveboxCreate(LoginRequiredMixin, CreateView):
    model= Lovebox
    form_class = LoveboxForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-lovebox')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Lovebox'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context 

class LoveboxUpdate(LoginRequiredMixin, UpdateView):
    model= Lovebox
    form_class = LoveboxForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-lovebox')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Lovebox'
        context['botao'] = 'Salvar'
        context['cor'] = 'success'
        return context 

class LoveboxDelete(LoginRequiredMixin, DeleteView):
    model = Lovebox
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-lovebox')

class LoveboxList(LoginRequiredMixin, ListView):
    model = Lovebox
    template_name = 'cadastros/listas/lovebox.html'

#DosesTratamento

class DosesTratamentoCreate(LoginRequiredMixin, CreateView):
    model= DosesTratamento
    form_class = DosesTratamentoForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-lovebox')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de DosesTratamento'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context 

class DosesTratamentoUpdate(LoginRequiredMixin, UpdateView):
    model= DosesTratamento
    form_class = DosesTratamentoForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-doses-tratamento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Doses do Tratamento'
        context['botao'] = 'Salvar'
        context['cor'] = 'success'
        return context 

class DosesTratamentoDelete(LoginRequiredMixin, DeleteView):
    model = DosesTratamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-doses-tratamento')

class DosesTratamentoList(LoginRequiredMixin, ListView):
    model = DosesTratamento
    template_name = 'cadastros/listas/doses-tratamento.html'