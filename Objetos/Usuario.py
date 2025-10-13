from abc import ABC

class Usuario(ABC):
    def __init__(self, login: str, senha: str, tipo: str):
        self.__login = None
        self.__senha = None
        self.__tipo = None

        if isinstance(login, str):
            self.__login = login
        if isinstance(senha, str):
            self.__senha = senha
        if tipo in ["cliente", "funcionario"]:
            self.__tipo = tipo
        else:
            raise ValueError("Tipo de usuário inválido. Deve ser 'cliente' ou 'funcionario'.")

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha: str):
        self.__senha = senha   

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        if tipo in ["cliente", "funcionario"]:
            self.__tipo = tipo
        else:
            raise ValueError("Tipo de usuário inválido. Deve ser 'cliente' ou 'funcionario'.")
