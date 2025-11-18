from Telas.abstract_tela import AbstractTela

class TelaCliente(AbstractTela):
    def mostrar_menu(self):
        print("\nMenu Cliente:")
        print("1 - Listar Reservas")
        print("2 - Criar Reserva")
        print("3 - Alterar Reserva")
        print("4 - Excluir Reserva")
        print("5 - Consultar Cardápio")   
        print("6 - Efetuar Pagamento")
        print("0 - Logout")
        return input("Escolha: ")

    def mostrar_reservas(self, reservas):
        if not reservas:
            print("Nenhuma reserva encontrada.")
        else:
            for r in reservas:
                print(f"ID: {r.id} | Mesa: {r.mesa_numero} | Restaurante: {r.restaurante} | Data/Hora: {r.data_hora} | Detalhes: {r.detalhes} | Status: {r.status}")

    def pedir_dados_reserva(self):
        mesa = input("Número da mesa: ")
        restaurante = input("Nome do restaurante: ")
        detalhes = input("Detalhes da reserva: ")
        data_hora = input("Data e hora (ex: 13/10/2025 18:00): ")
        return mesa, restaurante, detalhes, data_hora

    def pedir_id_reserva(self):
        return int(input("ID da Reserva: "))

    def pedir_nome_restaurante(self):
        return input("Nome do restaurante: ")

    def mostrar_cardapio(self, itens):
        if not itens:
            self.mostrar_mensagem("Nenhum item no cardápio.")
            return
        print("--- Itens do Cardápio ---")
        for item in itens:
            print(f"- {item}")
