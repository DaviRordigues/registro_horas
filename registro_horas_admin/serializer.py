from rest_framework import serializers
from .models import RegistroPonto

class RegistroPontoSerializer(serializers.ModelSerializer):
    horas_trabalhadas = serializers.ReadOnlyField()

    class Meta:
        model = RegistroPonto
        fields = ["funcionario", "data", "entrada", "saida", "horas_trabalhadas"]
