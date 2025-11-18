from Objetos.reserva import Reserva

class ControladorReserva:
    def __init__(self, tela_reserva):
        self.tela_reserva = tela_reserva
        self.reservas = [] 

    def adicionar_reserva(self, reserva):
        self.reservas.append(reserva)

    def buscar_reserva(self, id_reserva):
        for r in self.reservas:
            if r.id == id_reserva:
                return r
        return None

    def listar_todas_reservas(self):
        self.tela_reserva.mostrar_reservas(self.reservas)

    def listar_reservas_por_cliente(self, login_cliente):
        lista_filtrada = [r for r in self.reservas if r.cliente_login == login_cliente]
        return lista_filtrada

    def remover_reserva(self, id_reserva, cliente_login):
        reserva = self.buscar_reserva(id_reserva)
        if reserva and reserva.cliente_login == cliente_login:
            self.reservas.remove(reserva)
            return True
        return False
