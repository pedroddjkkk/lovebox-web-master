from rest_framework import serializers
from cadastros import models

class CadastrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DosesTratamento
        fields = '__all__'