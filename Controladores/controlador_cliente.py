from Objetos.reserva import Reserva
from Objetos.pagamento import Pagamento
import FreeSimpleGUI as sg

class ControladorCliente:
    def __init__(self, sistema, tela_cliente):
        self.sistema = sistema
        self.tela_cliente = tela_cliente
    
    def consultar_cardapio(self):
        nome_restaurante = self.tela_cliente.pedir_nome_restaurante()
        if nome_restaurante is None:  # Usuário clicou Cancelar
            return
            
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
        if id_reserva is None:  # Usuário clicou Cancelar
            return
            
        reserva = self.sistema.buscar_reserva(id_reserva)
        if reserva and reserva.cliente_login == cliente.login:
            # CORREÇÃO: Tela gráfica para pagamento
            sg.ChangeLookAndFeel('DarkTeal4')
            layout = [
                [sg.Text('--- EFETUAR PAGAMENTO ---', font=("Helvica", 25))],
                [sg.Text(f'Reserva ID: {reserva.id}', font=("Helvica", 12))],
                [sg.Text(f'Restaurante: {reserva.restaurante}', font=("Helvica", 12))],
                [sg.Text(f'Mesa: {reserva.mesa_numero}', font=("Helvica", 12))],
                [sg.Text('Valor do pagamento (Ex: 20.00):', size=(25, 1)), sg.InputText('', key='valor')],
                [sg.Text('Método de pagamento:', size=(25, 1)), sg.InputText('', key='metodo')],
                [sg.Button('Confirmar Pagamento'), sg.Cancel('Cancelar')]
            ]
            window = sg.Window('Pagamento', layout)
            button, values = window.read()
            window.close()
            
            if button in (None, 'Cancelar'):
                return
                
            try:
                valor = float(values['valor'])
                metodo = values['metodo']
                pagamento = Pagamento(reserva.id, valor, metodo)
                pagamento.confirmar_pagamento()
                self.sistema.pagamentos.append(pagamento)
                self.tela_cliente.mostrar_mensagem("Pagamento confirmado!")
            except ValueError:
                self.tela_cliente.mostrar_mensagem("Valor inválido! Use formato: 20.00")
        else:
            self.tela_cliente.mostrar_mensagem("Reserva não encontrada ou não pertence a você.")

    def menu_cliente(self):
        cliente = self.sistema.buscar_cliente(self.sistema.logado.login)
        while True:
            escolha = self.tela_cliente.mostrar_menu()
            
            if escolha == 1:  # Listar Reservas
                reservas = self.sistema.listar_reservas_cliente(cliente.login)
                self.tela_cliente.mostrar_reservas(reservas)
                
            elif escolha == 2:  # Criar Reserva
                dados = self.tela_cliente.pedir_dados_reserva()
                if dados is None:  # Usuário clicou Cancelar
                    continue
                    
                mesa_input, restaurante_nome, detalhes, data_hora = dados
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
                
            elif escolha == 3:  # Alterar Reserva
                id_reserva = self.tela_cliente.pedir_id_reserva()
                if id_reserva is None:  # Usuário clicou Cancelar
                    continue
                    
                dados = self.tela_cliente.pedir_dados_reserva()
                if dados is None:  # Usuário clicou Cancelar
                    continue
                    
                mesa_input, restaurante, detalhes, data_hora = dados
                reserva = self.sistema.buscar_reserva(id_reserva)
                if reserva and reserva.cliente_login == cliente.login:
                    try:
                        mesa_numero = int(mesa_input)
                    except (ValueError, TypeError):
                        self.tela_cliente.mostrar_mensagem("Número da mesa inválido. Alteração cancelada.")
                        continue
                    reserva.atualizar(mesa_numero=mesa_numero, restaurante=restaurante, detalhes=detalhes, data_hora=data_hora)
                    self.sistema.atualizar_reserva(reserva)
                    self.tela_cliente.mostrar_mensagem("Reserva atualizada.")
                else:
                    self.tela_cliente.mostrar_mensagem("Reserva não encontrada ou não pertence a você.")
                    
            elif escolha == 4:  # Excluir Reserva
                id_reserva = self.tela_cliente.pedir_id_reserva()
                if id_reserva is None:  # Usuário clicou Cancelar
                    continue
                    
                reserva = self.sistema.buscar_reserva(id_reserva)
                if reserva and reserva.cliente_login == cliente.login:
                    self.sistema.remover_reserva(id_reserva)
                    self.tela_cliente.mostrar_mensagem("Reserva excluída.")
                else:
                    self.tela_cliente.mostrar_mensagem("Reserva não encontrada ou não pertence a você.")
                    
            elif escolha == 5:  # Consultar Cardápio
                self.consultar_cardapio()
                
            elif escolha == 6:  # Efetuar Pagamento
                self.efetuar_pagamento(cliente)
                
            elif escolha == 0:  # Logout
                self.sistema.logado = None
                break
                
            else:
                self.tela_cliente.mostrar_mensagem("Opção inválida.")
