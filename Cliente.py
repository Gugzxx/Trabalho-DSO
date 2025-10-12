class Cliente:
    def __init__(self, login, nome, email):
        self.login = login
        self.nome = nome
        self.email = email
        self.reservas = []

    def adicionar_reserva(self, reserva):
        self.reservas.append(reserva)

    def listar_reservas(self):
        return self.reservas
