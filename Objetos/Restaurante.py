class Restaurante:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.cardapio = None
        self.mesas = []

    def set_cardapio(self, cardapio):
        self.cardapio = cardapio

    def adicionar_mesa(self, mesa):
        self.mesas.append(mesa)

    def listar_mesas(self):
        return self.mesas
