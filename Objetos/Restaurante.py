class Restaurante:
    def __init__(self, nome: str, endereco: str):
        self.__nome = None
        self.__endereco = None
        self.cardapio = None
        self.mesas = []

        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(endereco, str):
            self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco

    def set_cardapio(self, cardapio):
        self.cardapio = cardapio

    def adicionar_mesa(self, mesa):
        self.mesas.append(mesa)

    def listar_mesas(self):
        return self.mesas
