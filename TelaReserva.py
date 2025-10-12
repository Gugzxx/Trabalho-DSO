from Telas.AbstractTela import AbstractTela

class TelaReserva(AbstractTela):
    def mostrar_reservas(self, reservas):
        if not reservas:
            print("Nenhuma reserva cadastrada.")
        else:
            for r in reservas:
                print(f"Reserva #{r.id} - Cliente: {r.cliente_login} - Restaurante: {r.restaurante.nome} - Mesa {r.mesa_numero} - Data: {r.data_hora} - Status: {r.status}")
