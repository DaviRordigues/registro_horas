from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import RegistroPonto
from .serializers import RegistroPontoSerializer

class RegistroPontoViewSet(viewsets.ModelViewSet):
    queryset = RegistroPonto.objects.all()
    serializer_class = RegistroPontoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Para exibir apenas os registros do usuário autenticado
        if self.request.user.is_superuser:
            return RegistroPonto.objects.all()
        return RegistroPonto.objects.filter(funcionario=self.request.user)
