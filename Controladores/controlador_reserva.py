from Objetos.reserva import Reserva

class ControladorReserva:
    def __init__(self, tela_reserva, sistema=None):
        self.tela_reserva = tela_reserva
        self.sistema = sistema  # Receber o sistema para acessar as reservas

    def adicionar_reserva(self, reserva):
        if self.sistema:
            self.sistema.adicionar_reserva(reserva)
        else:
            # Fallback se não tiver sistema (para compatibilidade)
            if not hasattr(self, 'reservas'):
                self.reservas = []
            self.reservas.append(reserva)

    def buscar_reserva(self, id_reserva):
        if self.sistema:
            return self.sistema.buscar_reserva(id_reserva)
        else:
            # Fallback
            for r in self.reservas:
                if r.id == id_reserva:
                    return r
            return None

    def listar_todas_reservas(self):
        if self.sistema:
            reservas = self.sistema.listar_todas_reservas()
        else:
            reservas = self.reservas
        self.tela_reserva.mostrar_reservas(reservas)

    def listar_reservas_por_cliente(self, login_cliente):
        if self.sistema:
            return self.sistema.listar_reservas_cliente(login_cliente)
        else:
            lista_filtrada = [r for r in self.reservas if r.cliente_login == login_cliente]
            return lista_filtrada

    def remover_reserva(self, id_reserva, cliente_login=None):
        if self.sistema:
            return self.sistema.remover_reserva(id_reserva)
        else:
            reserva = self.buscar_reserva(id_reserva)
            if reserva and (cliente_login is None or reserva.cliente_login == cliente_login):
                self.reservas.remove(reserva)
                return True
            return False
