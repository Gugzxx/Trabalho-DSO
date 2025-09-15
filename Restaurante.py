from Mesa import Mesa

class Restaurante:
    def __init__(self, nome: str, telefone: str, endereco: str):
        self.__nome = nome
        self.__telefone = telefone
        self.__endereco = endereco
        self.__mesas = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def mesas(self):
        return self.__mesas

    def incluir_mesa(self, mesa):
        if isinstance(mesa, Mesa):
            self.__mesas.append(mesa)
