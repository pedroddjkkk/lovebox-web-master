from rest_framework import viewsets
from cadastros.api import serializers
from cadastros import models

class CadastrosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CadastrosSerializer
    queryset = models.DosesTratamento.objects.all()