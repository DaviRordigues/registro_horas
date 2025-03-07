from django.contrib import admin
from .models import RegistroPonto

@admin.register(RegistroPonto)
class RegistroPontoAdmin(admin.ModelAdmin):
    list_display = ("funcionario", "data", "entrada", "saida", "horas_trabalhadas")
    list_filter = ("funcionario", "data")
    search_fields = ("funcionario__username", "data")
