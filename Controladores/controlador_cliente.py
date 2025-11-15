from Objetos.Reserva import Reserva
from Objetos.Pagamento import Pagamento

class ControladorCliente:
    def __init__(self, sistema, tela_cliente):
        self.sistema = sistema
        self.tela_cliente = tela_cliente
    
    def consultar_cardapio(self):
        nome_restaurante = input("Nome do restaurante: ")
        restaurante = next((r for r in self.sistema.restaurantes if r.nome == nome_restaurante), None)
        if restaurante and restaurante.cardapio:
            print("Itens do Cardápio:")
            for item in restaurante.cardapio.listar_itens():
                print(item)
        else:
            print("Restaurante não encontrado ou sem cardápio.")

    def efetuar_pagamento(self, cliente):
        reservas = self.sistema.listar_reservas_cliente(cliente.login)
        if not reservas:
            print("Nenhuma reserva encontrada.")
            return
        for r in reservas:
            print(f"ID: {r.id} - Detalhes: {r.detalhes} - Status: {r.status}")
        id_reserva = int(input("ID da reserva para pagar: "))
        reserva = self.sistema.buscar_reserva(id_reserva)
        if reserva and reserva.cliente_login == cliente.login:
            valor = float(input("Valor do pagamento(Ex: 20.00): "))
            metodo = input("Método de pagamento: ")
            pagamento = Pagamento(reserva.id, valor, metodo)
            pagamento.confirmar_pagamento()
            self.sistema.pagamentos.append(pagamento)
            print("Pagamento confirmado!")
        else:
            print("Reserva não encontrada ou não pertence a você.")


    def menu_cliente(self):
        cliente = self.sistema.buscar_cliente(self.sistema.logado.login)
        while True:
            escolha = self.tela_cliente.mostrar_menu()
            if escolha == '1':
                reservas = self.sistema.listar_reservas_cliente(cliente.login)
                self.tela_cliente.mostrar_reservas(reservas)
            elif escolha == '2':
                mesa_input, restaurante_nome, detalhes, data_hora = self.tela_cliente.pedir_dados_reserva()
                restaurante_obj = next((r for r in self.sistema.restaurantes if r.nome == restaurante_nome), None)
                if not restaurante_obj:
                    self.tela_cliente.mostrar_mensagem("Restaurante não encontrado.")
                    continue
                try:
                    mesa_numero = int(mesa_input)
                except (ValueError, TypeError):
                    self.tela_cliente.mostrar_mensagem("Número da mesa inválido.")
                    continue
                # Armazenamos como tipos primitivos (int para mesa, str para nome do restaurante)
                reserva = Reserva(cliente.login, mesa_numero, restaurante_obj.nome, detalhes, data_hora)
                self.sistema.adicionar_reserva(reserva)
                self.tela_cliente.mostrar_mensagem("Reserva criada com sucesso.")
            elif escolha == '3':
                id_reserva = self.tela_cliente.pedir_id_reserva()
                mesa_numero, restaurante, detalhes, data_hora = self.tela_cliente.pedir_dados_reserva()
                reserva = self.sistema.buscar_reserva(id_reserva)
                if reserva and reserva.cliente_login == cliente.login:
                    reserva.atualizar(detalhes, data_hora)
                    self.tela_cliente.mostrar_mensagem("Reserva atualizada.")
                else:
                    self.tela_cliente.mostrar_mensagem("Reserva não encontrada ou não pertence a você.")
            elif escolha == '4':
                id_reserva = self.tela_cliente.pedir_id_reserva()
                reserva = self.sistema.buscar_reserva(id_reserva)
                if reserva and reserva.cliente_login == cliente.login:
                    self.sistema.reservas.remove(reserva)
                    self.tela_cliente.mostrar_mensagem("Reserva excluída.")
                else:
                    self.tela_cliente.mostrar_mensagem("Reserva não encontrada ou não pertence a você.")
            elif escolha == '5':
                self.consultar_cardapio()
            elif escolha == '6':
                self.efetuar_pagamento(cliente)
            elif escolha == '0':
                self.sistema.logado = None
                break
            else:
                self.tela_cliente.mostrar_mensagem("Opção inválida.")
