from django.db import models
from clientes.models import Cliente
from produtos.models import Processadore
from produtos.models import Memoria_ram
from produtos.models import Disco_rigido
from produtos.models import Placa_de_video
from produtos.models import Gabinete
from produtos.models import Placa_mae
from produtos.models import Fone

class Componentes(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    processadore = models.ForeignKey(Processadore, on_delete=models.CASCADE)
    memoria_ram = models.ForeignKey(Memoria_ram, on_delete=models.CASCADE)
    disco_rigido = models.ForeignKey(Disco_rigido, on_delete=models.CASCADE)
    placa_de_video = models.ForeignKey(Placa_de_video, on_delete=models.CASCADE)
    gabinete = models.ForeignKey(Gabinete, on_delete=models.CASCADE)
    placa_mae = models.ForeignKey(Placa_mae, on_delete=models.CASCADE)
    fone = models.ForeignKey(Fone, on_delete=models.CASCADE)
    cartao_id = models.CharField(max_length=200,default=0)
    estatos = models.CharField(max_length=200,default='null')

    class Meta:
        verbose_name_plural = 'Componentes'


