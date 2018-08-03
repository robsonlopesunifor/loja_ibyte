from trello import TrelloClient


class Trello(object):

    def __init__(self,api_key,token):
        self.api_key = api_key
        self.token = token
        self.board = None
        self.list = None
        self.trello = None

        self.__conectar_trello()

    def criar_cartao(self,board, list, nome, descricao):
        self.__retornar_board_trello(board)
        self.__retornar_lista_trello(list)
        self.card = self.list.add_card(nome, descricao)

    def lista_do_cartao(self,cartao_id):
        try:
            card = self.trello.get_card(cartao_id)
            nome_list = self.trello.get_list(card.list_id).name
        except Exception as e:
            nome_list = 'null'
        return nome_list

    def __retornar_lista_trello(self,lista_):
        for l in self.board.list_lists():
            if l.name == lista_:
                lista = l
        self.list = lista

    def __retornar_board_trello(self,board_):
        for b in self.trello.list_boards():
            if b.name == board_:
                board = b
        self.board = board

    def __conectar_trello(self):
        trello = TrelloClient(api_key=self.api_key,
                              token=self.token)
        self.trello = trello
