import unittest
from datetime import datetime, timedelta
from trello import TrelloClient

"""
client = TrelloClient(
    api_key='4093c7958ea36ac55dfd35a80483455a',
    api_secret='8465b847bf9a3b421ec7e2b8940359520a0e008064cc6a5188156fbbbe87bbd4',
    token='892be97acff91398faff3dbdb9fc8e754e93ec6bdac3418af1fab775d9a66487',
    token_secret='your-oauth-token-secret'
)
"""

#all_boards = client.list_boards()
#last_board = all_boards[-1]
#print(last_board.name)

#all_boards = client.list_boards()
#last_board = all_boards[-1]
#last_board.list_lists()

#card = last_board.get_cards()
#print(last_board.name)
#print(len(card))

#_list = last_board.add_list('nova_lista1')
#card = _list.add_card('nome_card','descricao_card')

#card.set_closed(True)
#last_board.fetch_actions(action_filter='all', action_limit=2)

#card.add_checklist("Test Checklist", items=["item1","item2"], itemstates = [True, False])

#cards = last_board.open_cards()
#print(len(cards))

#cards[-1].delete()

#print(len(last_board.all_members()))

"""
for b in all_boards:
    print(b)

my_list = last_board.get_list(1)

for card in my_list.list_cards():
    print(card.name)
"""



class TrelloTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # conectar ao trello
        cls._trello = TrelloClient(api_key='4093c7958ea36ac55dfd35a80483455a',
                                   token='892be97acff91398faff3dbdb9fc8e754e93ec6bdac3418af1fab775d9a66487')
        # escolher um board
        for b in cls._trello.list_boards():
            if b.name == 'loja':
                cls._board = b
        # adicionar lista
        cls._list = cls._board.add_list(str(datetime.now()))

    def _add_card(self, name, description=None):
        try:
            card = self._list.add_card(name, description)
            return card
        except Exception as e:
            print(str(e))
            self.fail("Caught Exception adding card")

    def test01_add_card(self):
        name = "Teste para o python - no desc"
        #self.card = self._add_card(name)
        #print(self.card.id)

    def test02_pegar_info(self):
        card2 = self._trello.get_card('5b5b245aedb0c13778a02fbf')

        card2.fetch()
        print('description',card2.description)
        print('name',card2.name)
        print('member_id',card2.member_id)
        print('short_id',card2.short_id)
        print('list_id',card2.list_id)
        print('comment',card2.comment)
        print('checklists',card2.checklists)

        print('lista nome',self._trello.get_list(card2.list_id).name)

    def test03_comentario(self):
        card2 = self._trello.get_card('5b5b245aedb0c13778a02fbf')
        comment = "Hello World!"
        card2.comment(comment)
        card2.fetch(True)

        print(len(card2.comments))
        print(card2.comments)
        print(card2.comments[0]['data']['text'])

    def test04_anexa_url(self):
        print('anexa url')
        card2 = self._trello.get_card('5b5b245aedb0c13778a02fbf')
        card2.attach(name='lwn', url='http://lwn.net/')
        card2.fetch()
        print(card2.badges['attachments'])

    def test05_data_de_entrega(self):
        print('data de entraga')
        card2 = self._trello.get_card('5b5b245aedb0c13778a02fbf')
        today = datetime.today()
        day_detla = timedelta(3)
        due_date = today + day_detla
        card2.set_due(due_date)
        card2.fetch()
        print(card2.due)

    def test06_setar_nome(self):
        print('alterar nome')
        card2 = self._trello.get_card('5b5b245aedb0c13778a02fbf')
        card2.set_name('novo nome do cartao')
        print(card2.set_name)

    def test07_setar_descricao(self):
        pass

if __name__ == "__main__":
    unittest.main()