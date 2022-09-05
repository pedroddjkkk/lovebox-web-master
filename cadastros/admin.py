from django.contrib import admin
from .models import Cidade, Compartimento, Cuidador, DosesTratamento, Estado, Medicamento, Paciente, Pais, Lovebox, Tratamento, ProfissionalSaude

# Register your models here.
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Pais)
admin.site.register(Paciente)
admin.site.register(Cuidador)
admin.site.register(Lovebox)
admin.site.register(Compartimento)
admin.site.register(Tratamento)
admin.site.register(ProfissionalSaude)
admin.site.register(Medicamento)
admin.site.register(DosesTratamento)