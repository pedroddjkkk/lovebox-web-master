
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Criar todas as classes de acordo com seu diagrama de Classes


class Pais(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return "{} ({})".format(self.nome, self.sigla)


class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.nome, self.sigla)


class Cidade(models.Model):
    nome = models.CharField(max_length=50)

    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.nome, self.estado.sigla)

class Cuidador(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100)
    telefone = PhoneNumberField(region='BR')
    crc = models.IntegerField(null=True, blank=True, verbose_name='CRC')
    redes_sociais = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Redes Sociais')
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.nome)


class Paciente(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100)
    telefone = PhoneNumberField(region='BR')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    documento = models.CharField(max_length=14)
    cep = models.CharField(max_length=9)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    bairro = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    numero = models.IntegerField()
    anamnese = models.FileField(blank=True, null=True)
    redes_sociais = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Redes Sociais')
    cuidadores = models.ManyToManyField(Cuidador)

    def __str__(self):
        return "{}".format(self.nome)


class Medicamento(models.Model):
    nome_comercial = models.CharField(max_length=100)
    laboratorio = models.CharField(
        max_length=100, verbose_name='Laboratório')
    principio_ativo = models.CharField(
        max_length=255, verbose_name='Princípio Ativo')
    dose_diaria_maxima = models.CharField(
        max_length=500, verbose_name='Dose Diária Máxima')
    forma_farmaceutica = models.CharField(
        max_length=255, verbose_name='Forma Farmacêutica')
    concentracao = models.CharField(
        max_length=255, verbose_name='Concetração')
    via_administracao = models.CharField(
        max_length=255, verbose_name='Via Administração')
    grupo_etario = models.CharField(
        max_length=255, verbose_name='Grupo Etário')
    tarja = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(
            self.nome_comercial, self.concentracao)


class ProfissionalSaude(models.Model):
    nome = models.CharField(max_length=100)
    telefone = PhoneNumberField(region='BR')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    consultorio = models.CharField(max_length=255, verbose_name='Consultório')
    email = models.EmailField(unique=True, null=True, blank=True)
    redes_sociais = models.CharField(max_length=255, null=True, blank=True)
    crc = models.IntegerField(unique=True)

    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.nome)


class CategoriaParceiro(models.Model):
    categoria = models.CharField(max_length=100)


class Parceiro(models.Model):
    cpfcnpj = models.IntegerField(verbose_name='CPF/CNPJ')
    descricao = models.CharField(max_length=255, verbose_name='Descrição')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    telefone = PhoneNumberField(region='BR')
    email = models.EmailField()
    redes_sociais = models.CharField(max_length=255)

    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    categoria_parceiro = models.ForeignKey(
        CategoriaParceiro, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.cpfcnpj)

class Lovebox(models.Model):
    status = models.BooleanField(
        choices=(
            (True, 'Ativo'),
            (False, 'Inativo')
        )
    )
    num_serie = models.IntegerField(verbose_name='Número de Série')
    modelo = models.CharField(max_length=100)
    num_compartimentos = models.CharField(max_length=500,verbose_name="Número de Compartimentos")
    tempo_alerta_geral = models.IntegerField(verbose_name="Tempo de Alerta Geral(min)")

    proprietario = models.ForeignKey(Paciente, on_delete=models.PROTECT,verbose_name="Proprietário")
    cuidador = models.ForeignKey(Cuidador, on_delete=models.PROTECT)
    parceiro = models.ForeignKey(Parceiro,blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.num_serie)


class Compartimento(models.Model):
    linha = models.IntegerField()
    ordem = models.IntegerField()
    descricao = models.CharField(max_length=255)
    lovebox = models.ForeignKey(Lovebox, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format("Lovebox "+ str(self.lovebox) +" - "+ self.descricao)


class Tratamento(models.Model):
    prescrito_por = models.ForeignKey(
        ProfissionalSaude, on_delete=models.PROTECT)
    data_prescricao = models.DateField(verbose_name="Data da Prescrição")
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT)
    concetracao = models.FloatField(verbose_name="Concentração")
    frequencia_diaria = models.IntegerField(verbose_name='Frequência Diária')
    horarios_diarios = models.CharField(
        max_length=255, verbose_name="Horários Diários")
    quantidade_ingerir = models.FloatField()
    unidade_medida = models.CharField(max_length=5,
                                      choices=(
                                          ('mg', 'mg'),
                                          ('ml', 'ml'),
                                          ('g', 'g'),
                                          ('gotas', 'gotas')
                                      ))
    data_inicio = models.DateField()
    tipo_tratamento = models.CharField(max_length=10,
                                       choices=(
                                           ('continuo', 'Contínuo'),
                                           ('temporario', 'Temporário')
                                       )
                                       )
    periodo_tratamento = models.IntegerField(
        verbose_name='Período de Tratamento(dias)', null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    tempo_alerta = models.IntegerField(verbose_name="Tempo de Alerta(min)",
                                       default=15,
                                       validators=[
                                           MaxValueValidator(100),
                                           MinValueValidator(1)
                                       ])
    observacao = models.TextField(
        max_length=255, verbose_name='Observação', null=True, blank=True)
    lote = models.IntegerField(null=True, blank=True)
    validade = models.DateField(null=True, blank=True)
    embalagem_fracionavel = models.BooleanField(
        choices=(
            (True, 'Sim'),
            (False, 'Não')
        )
    )
    quantidade_total_embalagem = models.IntegerField(
        verbose_name='Quantidade Total de Embalagem')
    amostraGratis = models.BooleanField(
        choices=(
            (True, 'Sim'),
            (False, 'Não')
        )
    )
    status_tratamento = models.BooleanField(
        choices=(
            (True, 'Ativo'),
            (False, 'Inativo')
        )
    )
    status_tratamento_data = models.DateTimeField(
        verbose_name="Data da Atualização de Status", null=True, blank=True)
    paciente = models.ForeignKey(
        User, related_name='paciente_tratemento', on_delete=models.PROTECT)
    compartimento = models.ForeignKey(Compartimento, on_delete=models.PROTECT)
    cadastrado_por = models.ForeignKey(
        User, related_name='cadastrado_por', on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True, blank=True)
    atualizado_em = models.DateTimeField()

class DosesTratamento(models.Model):  # Falta alguns atributos
    lovebox = models.CharField(max_length=100)
    compartimento = models.IntegerField()
    horario_dose = models.TimeField(null=True, blank=True)
    compartimento_caixa: models.CharField(max_length=25)
    tempo_alerta_especifico = models.IntegerField()
    status_ingestao = models.BooleanField(
                                       default=False,
                                       choices=(
                                           (True, 'S'),
                                           (False, 'N')
                                       )
                                       )
    status_sincronizacao_download = models.BooleanField(default=True)
    data_sincronizacao_download = models.DateTimeField(null=True, blank=True)
    status_sincronização_upload = models.BooleanField(default=False)
    data_sincronizacao_upload = models.DateTimeField(null=True, blank=True)
    status_tratamento = models.BooleanField(default=True,
                                         choices=(
                                             (True, 'Ativo'),
                                             (False, 'Inativo')
                                         )
                                         )
    tratamento = models.ForeignKey(Tratamento, on_delete=models.PROTECT)
    paciente = models.CharField(max_length=255)
    dosagem = models.CharField(max_length=255)
    medicamento = models.CharField(max_length=255)
    um = models.CharField(max_length=3, default = 'mg')