from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from pedidos.models import Computador
from pedidos.models import Peca

class PedidosViewSet(ModelViewSet):

    # pontoturistico/1/denunciar
    @action(methods=['get'], detail=True)
    def add_cartao_trello(self, request, pk=None):
        print(Peca.objects.filter(computador=pk))
