from django import forms
from .models import Paciente, Medicamento, ProfissionalSaude, Cuidador


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
        'nome': forms.TextInput(attrs={'class': 'form-control'}),
        'telefone': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ex:(11) 23456-7890'}),
        'data_nascimento': forms.DateInput(attrs={'type': 'date','class': 'data_nascimentoClass','placeholder':'dd/mm/aaaa'},format='%Y-%m-%d'),
        'anamnese': forms.FileInput(attrs={'class': 'form-control'}),
        'redes_sociais': forms.TextInput(attrs={'class': 'form-control'}),
        'cidade': forms.Select(attrs={'class': 'form-control'}),
        }   

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'
        widgets = {

        }

class ProfissionalSaudeForm(forms.ModelForm):
    class Meta:
        model = ProfissionalSaude
        fields = '__all__'
        widgets = {
            'telefone': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ex:(11) 23456-7890'})
        }

class CuidadorForm(forms.ModelForm):
    class Meta:
        model = Cuidador
        fields = '__all__'
        widgets = {
            'telefone': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ex:(11) 23456-7890'})
        }