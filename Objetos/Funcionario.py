class Funcionario:
    def __init__(self, login, nome, email, is_admin=False):
        self.login = login
        self.nome = nome
        self.email = email
        self.is_admin = is_admin
