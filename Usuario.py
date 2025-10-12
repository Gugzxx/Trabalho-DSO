class Usuario:
    def __init__(self, login, senha, tipo):
        self.login = login
        self.senha = senha
        self.tipo = tipo

class Funcionario(Usuario):
    def __init__(self, login, senha, nome, email, is_admin=False):
        super().__init__(login, senha, "funcionario")
        self.nome = nome
        self.email = email
        self.is_admin = is_admin

class Cliente(Usuario):
    def __init__(self, login, senha, nome, email):
        super().__init__(login, senha, "cliente")
        self.nome = nome
        self.email = email
