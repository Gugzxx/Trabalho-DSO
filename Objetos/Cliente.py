from Objetos.Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, login: str, senha: str, nome: str, email: str):
        super().__init__(login, senha, "cliente")
        self.__nome = None
        self.__email = None
        self.reservas = []

        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(email, str) and "@" in email:
            self.__email = email

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

    def adicionar_reserva(self, reserva):
        self.reservas.append(reserva)

    def listar_reservas(self):
        return self.reservas
