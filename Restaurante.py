from Mesa import Mesa

class Restaurante:
    def __init__(self, nome: str, telefone: str, endereco: str, mesas: list):
        self.__nome = None
        self.__telefone = None
        self.__endereco = None
        self.__mesas = []
        
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(telefone, str):
            self.__telefone = telefone
        if isinstance(endereco, str):
            self.__endereco = endereco
        if isinstance(mesa, Mesa):
            self.__mesas.append(mesa)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def nome(self, telefone: str):
        if isinstance(telefone, str):
            self.__telefone = telefone

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco = endereco

    @property
    def mesas(self):
        return self.__mesas

    def incluir_mesa():
        if isinstance(mesa, Mesa) and mesa is not in mesas:
            self.__mesas.append(mesa)
        return mesas

    def excluir_mesa():
        if isinstance(mesa, Mesa) and mesa is in mesas:
            self.__mesas.remove(mesa)
        return mesas
