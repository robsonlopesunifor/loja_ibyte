from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Componentes
from clientes.models import Cliente
from produtos.models import Processadore
from produtos.models import Memoria_ram
from produtos.models import Disco_rigido
from produtos.models import Placa_de_video
from produtos.models import Gabinete
from produtos.models import Placa_mae
from produtos.models import Fone
from .form import PedidosForm
from trello import TrelloClient

def pedidos(request, cliente):
    dados = {}
    componente = {}
    componente['componentes'] = []
    trello = conectar_trello()

    dados = Componentes.objects.filter(cliente=cliente)
    for dado in dados:
        card = trello.get_card(dado.cartao_id)
        nome_lista = trello.get_list(card.list_id).name
        componente['componentes'].append({'pedido':dado.id,'status':nome_lista})
    return render(request, 'listagem.html', componente)

def pedir(request):
    form = PedidosForm(request.POST, None)
    if form.is_valid():
        instancia = form.save()
        cartao = criar_e_escrever_cartao(form)
        update(cartao,instancia.pk)
        return redirect('pedidos',form.data['cliente'])
    return render(request, 'pedir.html', {'form': form})

def criar_e_escrever_cartao(dados):
    cliente = Cliente.objects.get(id=dados.data['cliente'])
    processador = Processadore.objects.get(id=dados.data['processadore'])
    memoria_ram = Memoria_ram.objects.get(id=dados.data['memoria_ram'])
    disco_rigido = Disco_rigido.objects.get(id=dados.data['disco_rigido'])
    placa_de_video = Placa_de_video.objects.get(id=dados.data['placa_de_video'])
    gabinete = Gabinete.objects.get(id=dados.data['gabinete'])
    placa_mae = Placa_mae.objects.get(id=dados.data['placa_mae'])
    fone = Fone.objects.get(id=dados.data['fone'])

    descricao_cliente = "".join(['Cliente: ',cliente.nome,'\n',
                                 'Email:', cliente.email,'\n','\n'])

    descricao_componentes = "".join(['Processador:',processador.nome,', R$:',str(processador.valor), '\n',
                                    'Memoria ram: ',memoria_ram.nome,', R$:',str(memoria_ram.valor), '\n',
                                    'Disco rigido: ',disco_rigido.nome,', R$:',str(disco_rigido.valor), '\n',
                                    'Placa_de_video: ',placa_de_video.nome,', R$:',str(placa_de_video.valor), '\n',
                                    'Gabinete: ',gabinete.nome,', R$:',str(gabinete.valor), '\n',
                                    'Placa mae: ',placa_mae.nome,', R$:',str(placa_mae.valor), '\n',
                                    'Fone: ',fone.nome,', R$:',str(fone.valor), '\n','\n'])

    descricao = "".join([descricao_cliente,descricao_componentes])

    return retornar_cartao('pedido: ', descricao)


def update(cartao,pk):
    componente = Componentes.objects.get(pk=pk)
    componente.cartao_id = cartao.id
    componente.save()

def retornar_cartao(nome,descricao):
    lista = retornar_lista_trello('Pedido Realizado')
    card = lista.add_card(nome, descricao)
    return card

def retornar_lista_trello(lista_):
    board = retornar_board_trello('loja')
    for l in board.list_lists():
        if l.name == lista_:
            lista = l
    return lista

def retornar_board_trello(board_):
    trello = conectar_trello()
    for b in trello.list_boards():
        if b.name == board_:
            board = b
    return board

def conectar_trello():
    trello = TrelloClient(api_key='4093c7958ea36ac55dfd35a80483455a',
                          token='892be97acff91398faff3dbdb9fc8e754e93ec6bdac3418af1fab775d9a66487')
    return trello
