from Telas.abstract_tela import AbstractTela

class TelaReserva(AbstractTela):
    def mostrar_reservas(self, reservas):
        print("\n--- Listagem de Reservas ---")
        if not reservas:
            print("Nenhuma reserva encontrada.")
        else:
            for r in reservas:
                print(f"ID: {r.id} | Cliente: {r.cliente_login}")
                print(f"   Local: {r.restaurante} - Mesa {r.mesa_numero}")
                print(f"   Data: {r.data_hora}")
                print(f"   Status: {r.status}")
                print("-" * 30)
