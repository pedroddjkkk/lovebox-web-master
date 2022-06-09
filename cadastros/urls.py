from django.urls import path

from .views import CidadeDelete, CidadeList, CidadeUpdate, EstadoCreate, CidadeCreate, EstadoUpdate, EstadoDelete, EstadoList
from .views import PacienteCreate,PacienteDelete, PacienteList, PacienteUpdate, MedicamentoCreate, MedicamentoUpdate, MedicamentoDelete, MedicamentoList
from .views import ProfissionalSaudeCreate, ProfissionalSaudeUpdate, ProfissionalSaudeList, ProfissionalSaudeDelete
from .views import CuidadorCreate, CuidadorUpdate, CuidadorList, CuidadorDelete, TratamentoCreate, TratamentoUpdate, TratamentoList, TratamentoDelete



urlpatterns = [
    path('inserir/estado/', EstadoCreate.as_view(), name='cadastrar-estado'),
    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name='editar-estado'),
    path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name='excluir-estado'),
    path('listar/estado/', EstadoList.as_view(), name='listar-estado'),

    path('inserir/cidade/', CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name='excluir-cidade'),
    path('listar/cidade/', CidadeList.as_view(), name='listar-cidade'),

    path('inserir/paciente/', PacienteCreate.as_view(), name='cadastrar-paciente'),
    path('editar/paciente/<int:pk>/', PacienteUpdate.as_view(), name='editar-paciente'),
    path('excluir/paciente/<int:pk>/', PacienteDelete.as_view(), name='excluir-paciente'),
    path('listar/paciente/', PacienteList.as_view(), name='listar-paciente'),

    path('inserir/medicamento/', MedicamentoCreate.as_view(), name='cadastrar-medicamento'),
    path('editar/medicamento/<int:pk>/', MedicamentoUpdate.as_view(), name='editar-medicamento'),
    path('excluir/medicamento/<int:pk>/', MedicamentoDelete.as_view(), name='excluir-medicamento'),
    path('listar/medicamento/', MedicamentoList.as_view(), name='listar-medicamento'),
    
    path('inserir/profissional_saude/', ProfissionalSaudeCreate.as_view(), name='cadastrar-profissional_saude'),
    path('editar/profissional_saude/<int:pk>/', ProfissionalSaudeUpdate.as_view(), name='editar-profissional_saude'),
    path('excluir/profissional_saude/<int:pk>/', ProfissionalSaudeDelete.as_view(), name='excluir-profissional_saude'),
    path('listar/profissional_saude/', ProfissionalSaudeList.as_view(), name='listar-profissional_saude'),

    path('inserir/cuidador/', CuidadorCreate.as_view(), name='cadastrar-cuidador'),
    path('editar/cuidador/<int:pk>/', CuidadorUpdate.as_view(), name='editar-cuidador'),
    path('excluir/cuidador/<int:pk>/', CuidadorDelete.as_view(), name='excluir-cuidador'),
    path('listar/cuidador/', CuidadorList.as_view(), name='listar-cuidador'),

    path('inserir/tratamento/', TratamentoCreate.as_view(), name='cadastrar-tratamento'),
    path('editar/tratamento/<int:pk>/', TratamentoUpdate.as_view(), name='editar-tratamento'),
    path('excluir/tratamento/<int:pk>/', TratamentoDelete.as_view(), name='excluir-tratamento'),
    path('listar/tratamento/', TratamentoList.as_view(), name='listar-tratamento'),
]
