from django.forms import ModelForm
from .models import Componentes

class PedidosForm(ModelForm):
    class Meta:
        model = Componentes
        fields = ['cliente',
                  'processadore',
                  'memoria_ram',
                  'disco_rigido',
                  'placa_de_video',
                  'gabinete',
                  'placa_mae',
                  'fone',
                  'cartao_id',
                  'estatos']