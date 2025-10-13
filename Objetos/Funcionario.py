class Funcionario:
    def __init__(self, login: str, nome: str, email: str, is_admin=False):
        self.__login = None
        self.__nome = None
        self.__email = None
        self.is_admin = is_admin

        if isinstance(login, str):
            self.__login = login
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(email, str) and "@" in email:
            self.__email = email

    @property
    def login(self):
        return self.__login
    
    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email: str):
        if "@" in email:
            self.__email = email
        else:
            raise ValueError("Email inválido.")
