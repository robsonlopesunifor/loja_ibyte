# permite fazer create(), retrive(), uodate(), partial_update(), destroy(), list()
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from pedidos.models import Componentes
from .serializers import PedidosSerializer
from pedidos.api import Trello
from clientes.models import Cliente
from produtos.models import Processadore
from produtos.models import Memoria_ram
from produtos.models import Disco_rigido
from produtos.models import Placa_de_video
from produtos.models import Gabinete
from produtos.models import Placa_mae
from produtos.models import Fone

class PedidosViewSet(ModelViewSet):

    trello = Trello.Trello('4093c7958ea36ac55dfd35a80483455a','892be97acff91398faff3dbdb9fc8e754e93ec6bdac3418af1fab775d9a66487')
    serializer_class = PedidosSerializer
    queryset = Componentes.objects.all()

    def get_queryset(self):
        cliente = self.request.query_params.get('cliente', None)
        queryset = Componentes.objects.all()
        if cliente:
            queryset = Componentes.objects.filter(cliente=cliente)
        for idx,item in enumerate(queryset):
            queryset[idx].estatos = self.trello.lista_do_cartao(queryset[idx].cartao_id)
        return queryset

    def create(self, request, *args, **kwargs):
        resposta = super(PedidosViewSet, self).create(request, *args, **kwargs)
        # return Response({'Hello':request.data['nome']}) #POST
        descricao_txt = self.descricao(request)
        nome_txt = "".join(['Pedido: ',str(resposta.data['id'])])
        board = 'loja'
        list = 'Pedido Realizado'
        self.trello.criar_cartao(board, list, nome_txt, descricao_txt)
        resposta.data['cartao_id'] = self.trello.card.id
        componente = Componentes.objects.get(pk=resposta.data['id'])
        componente.cartao_id = resposta.data['cartao_id']
        componente.save()
        return resposta

    def destroy(self, request, *args, **kwargs): #DELET
        return super(PedidosViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs): # GET/id/
        resposta = super(PedidosViewSet, self).retrieve(request, *args, **kwargs)
        resposta.data['estatos'] = self.trello.lista_do_cartao(resposta.data['cartao_id'])
        return resposta

    def update(self, request, *args, **kwargs): #PUT
        return super(PedidosViewSet, self).update(request, *args, **kwargs)

    def nome(self):
        pass

    def descricao(self,dados):
        cliente = Cliente.objects.get(id=dados.data['cliente'])
        processador = Processadore.objects.get(id=dados.data['processadore'])
        memoria_ram = Memoria_ram.objects.get(id=dados.data['memoria_ram'])
        disco_rigido = Disco_rigido.objects.get(id=dados.data['disco_rigido'])
        placa_de_video = Placa_de_video.objects.get(id=dados.data['placa_de_video'])
        gabinete = Gabinete.objects.get(id=dados.data['gabinete'])
        placa_mae = Placa_mae.objects.get(id=dados.data['placa_mae'])
        fone = Fone.objects.get(id=dados.data['fone'])

        descricao_cliente = "".join(['Cliente: ', cliente.nome, '\n',
                                     'Email:', cliente.email, '\n', '\n'])

        descricao_componentes = "".join(['Processador:', processador.nome, ', R$:', str(processador.valor), '\n',
                                         'Memoria ram: ', memoria_ram.nome, ', R$:', str(memoria_ram.valor), '\n',
                                         'Disco rigido: ', disco_rigido.nome, ', R$:', str(disco_rigido.valor), '\n',
                                         'Placa_de_video: ', placa_de_video.nome, ', R$:', str(placa_de_video.valor),
                                         '\n',
                                         'Gabinete: ', gabinete.nome, ', R$:', str(gabinete.valor), '\n',
                                         'Placa mae: ', placa_mae.nome, ', R$:', str(placa_mae.valor), '\n',
                                         'Fone: ', fone.nome, ', R$:', str(fone.valor), '\n', '\n'])

        descricao = "".join([descricao_cliente, descricao_componentes])
        return descricao


