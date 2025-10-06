class Usuario:
    def __init__(self, nome: str, telefone: str, email: str):
        self.__nome = None
        self.__telefone = None
        self.__email = None

        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(telefone, str):
            self.__telefone = telefone
        if isinstance(email, str):
            self.__email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str) and len(nome) > 0:
            self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        if isinstance(telefone, str) and len(telefone) > 0:
            self.__telefone = telefone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        if isinstance(email, str) and "@" in email:
            self.__email = email
