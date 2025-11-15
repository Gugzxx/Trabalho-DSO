class ControladorReserva:
    def __init__(self, sistema, tela_reserva):
        self.sistema = sistema
        self.tela_reserva = tela_reserva

    def mostrar_todas_reservas(self):
        reservas = self.sistema.listar_todas_reservas()
        self.tela_reserva.mostrar_reservas(reservas)
        input("Pressione Enter para continuar...")
