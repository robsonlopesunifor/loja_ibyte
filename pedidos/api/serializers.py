from rest_framework.serializers import ModelSerializer
from pedidos.models import Componentes

class PedidosSerializer(ModelSerializer):
    class Meta:
        model = Componentes
        fields = ('id','cliente', 'processadore', 'memoria_ram','disco_rigido','placa_de_video','gabinete','placa_mae','fone','cartao_id','estatos')