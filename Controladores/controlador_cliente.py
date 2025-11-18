from Objetos.reserva import Reserva
from Objetos.pagamento import Pagamento

class ControladorCliente:
    def __init__(self, sistema, tela_cliente):
        self.sistema = sistema
        self.tela_cliente = tela_cliente
    
    def consultar_cardapio(self):
        nome_restaurante = self.tela_cliente.pedir_nome_restaurante()
        restaurante = next((r for r in self.sistema.restaurantes if r.nome == nome_restaurante), None)
        if restaurante and restaurante.cardapio:
            itens = restaurante.cardapio.listar_itens()
            self.tela_cliente.mostrar_cardapio(itens)
        else:
            self.tela_cliente.mostrar_mensagem("Restaurante não encontrado ou sem cardápio.")

    def efetuar_pagamento(self, cliente):
        reservas = self.sistema.listar_reservas_cliente(cliente.login)
        if not reservas:
            self.tela_cliente.mostrar_mensagem("Nenhuma reserva encontrada.")
            return
        self.tela_cliente.mostrar_reservas(reservas)
        id_reserva = self.tela_cliente.pedir_id_reserva()
        reserva = self.sistema.buscar_reserva(id_reserva)
        if reserva and reserva.cliente_login == cliente.login:
            valor = float(input("Valor do pagamento(Ex: 20.00): "))
            metodo = input("Método de pagamento: ")
            pagamento = Pagamento(reserva.id, valor, metodo)
            pagamento.confirmar_pagamento()
            self.sistema.pagamentos.append(pagamento)
            self.tela_cliente.mostrar_mensagem("Pagamento confirmado!")
        else:
            self.tela_cliente.mostrar_mensagem("Reserva não encontrada ou não pertence a você.")


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
                reserva = Reserva(cliente.login, mesa_numero, restaurante_obj.nome, detalhes, data_hora)
                self.sistema.adicionar_reserva(reserva)
                self.tela_cliente.mostrar_mensagem("Reserva criada com sucesso.")
            elif escolha == '3':
                id_reserva = self.tela_cliente.pedir_id_reserva()
                mesa_input, restaurante, detalhes, data_hora = self.tela_cliente.pedir_dados_reserva()
                reserva = self.sistema.buscar_reserva(id_reserva)
                if reserva and reserva.cliente_login == cliente.login:
                    try:
                        mesa_numero = int(mesa_input)
                    except (ValueError, TypeError):
                        self.tela_cliente.mostrar_mensagem("Número da mesa inválido. Alteração cancelada.")
                        continue
                    reserva.atualizar(mesa_numero=mesa_numero, restaurante=restaurante, detalhes=detalhes, data_hora=data_hora)
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
