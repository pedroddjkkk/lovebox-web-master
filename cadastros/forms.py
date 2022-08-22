from django import forms
from .models import Paciente, Medicamento, ProfissionalSaude, Cuidador, Tratamento
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Fieldset, ButtonHolder, Div, HTML


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nome_comercial', css_class='form-group col-lg mb-0'),
                Column('laboratorio', css_class='form-group col-lg mb-0'),
                Column('principio_ativo', css_class='form-group col-lg mb-0'),
            ),
            Row(
                Column('dose_diaria_maxima',
                        css_class='form-group col-lg mb-0'),
                Column('forma_farmaceutica',
                        css_class='form-group col-lg mb-0'),
                Column('concentracao', css_class='form-group col-lg mb-0'),
            ),
            Row(
                Column('via_administracao',
                        css_class='form-group col-lg mb-0'),
                Column('grupo_etario',
                        css_class='form-group col-lg mb-0'),
                Column('tarja', css_class='form-group col-lg mb-0'),
            ),
        )  # Fim do layout

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

class TratamentoForm(forms.ModelForm):
    class Meta:
        model = Tratamento
        fields = '__all__'
        widgets = {
            'data_prescricao': forms.DateInput(attrs={'type': 'date','class': 'data_prescricaoClass','placeholder':'dd/mm/aaaa'},format='%Y-%m-%d'),
            'validade': forms.DateInput(attrs={'type': 'date','class': 'validadeClass','placeholder':'dd/mm/aaaa'},format='%Y-%m-%d'),
            'data_inicio': forms.DateTimeInput(attrs={'type': 'date','class': 'data_inicio_dataClass'},format='%Y-%m-%d %H:%M'),
            'data_fim': forms.DateTimeInput(attrs={'type': 'date','class': 'data_fim_dataClass'},format='%Y-%m-%d %H:%M'),
            'status_tratamento_data': forms.DateTimeInput(attrs={'type': 'date','class': 'status_tratamento_dataClass'},format='%Y-%m-%d %H:%M'),
            'cadastrado_em': forms.DateTimeInput(attrs={'type': 'date','class': 'cadastrado_emClass'},format='%Y-%m-%d %H:%M'),
            'cadastrado_em': forms.DateTimeInput(attrs={'type': 'date','class': 'cadastrado_emClass'},format='%Y-%m-%d %H:%M'),
            'atualizado_em': forms.DateTimeInput(attrs={'type': 'date','class': 'atualizado_emClass'},format='%Y-%m-%d %H:%M')
        }

    