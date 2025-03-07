from django.db import models
from django.contrib.auth.models import User

class RegistroPonto(models.Model):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    entrada = models.TimeField()
    saida = models.TimeField()

    def horas_trabalhadas(self):
        if self.entrada and self.saida:
            diferenca = (self.saida.hour * 60 + self.saida.minute) - (self.entrada.hour * 60 + self.entrada.minute)
            return f"{diferenca // 60}h {diferenca % 60}m"
        return "Não registrado"

    def __str__(self):
        return f"{self.funcionario.username} - {self.data}"
