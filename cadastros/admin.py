from django.contrib import admin
from .models import Cidade, Estado, Paciente, Pais

# Register your models here.
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Pais)
admin.site.register(Paciente)