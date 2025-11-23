import FreeSimpleGUI as sg
from Telas.abstract_tela import AbstractTela

class TelaCliente(AbstractTela):
    def __init__(self):
        self.__window = None

    def mostrar_menu(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('--- MENU CLIENTE ---', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Listar Reservas', "RD1", key='1')],
            [sg.Radio('Criar Reserva', "RD1", key='2')],
            [sg.Radio('Alterar Reserva', "RD1", key='3')],
            [sg.Radio('Excluir Reserva', "RD1", key='4')],
            [sg.Radio('Consultar Cardápio', "RD1", key='5')],
            [sg.Radio('Efetuar Pagamento', "RD1", key='6')],
            [sg.Radio('Logout', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Menu Cliente').Layout(layout)

        button, values = self.__window.Read()
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        elif values['5']:
            opcao = 5
        elif values['6']:
            opcao = 6
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        else:
            opcao = 0
        self.__window.Close()
        return opcao

    def mostrar_reservas(self, reservas):
        if not reservas:
            sg.popup("Nenhuma reserva encontrada.")
        else:
            string_reservas = ""
            for r in reservas:
                string_reservas += f"ID: {r.id} | Mesa: {r.mesa_numero} | Restaurante: {r.restaurante} | Data/Hora: {r.data_hora} | Detalhes: {r.detalhes} | Status: {r.status}\n"
            
            sg.Popup('--- MINHAS RESERVAS ---', string_reservas)

    def pedir_dados_reserva(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('--- DADOS DA RESERVA ---', font=("Helvica", 25))],
            [sg.Text('Número da mesa:', size=(15, 1)), sg.InputText('', key='mesa')],
            [sg.Text('Nome do restaurante:', size=(15, 1)), sg.InputText('', key='restaurante')],
            [sg.Text('Detalhes da reserva:', size=(15, 1)), sg.InputText('', key='detalhes')],
            [sg.Text('Data e hora (ex: 13/10/2025 18:00):', size=(25, 1)), sg.InputText('', key='data_hora')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Criar Reserva').Layout(layout)

        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            self.__window.Close()
            return None

        mesa = values['mesa']
        restaurante = values['restaurante']
        detalhes = values['detalhes']
        data_hora = values['data_hora']
        
        self.__window.Close()
        return mesa, restaurante, detalhes, data_hora

    def pedir_id_reserva(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('--- SELECIONAR RESERVA ---', font=("Helvica", 25))],
            [sg.Text('Digite o ID da reserva:', font=("Helvica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('ID da Reserva').Layout(layout)

        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            self.__window.Close()
            return None

        try:
            id_reserva = int(values['id'])
        except ValueError:
            id_reserva = 0
        
        self.__window.Close()
        return id_reserva

    def pedir_nome_restaurante(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('--- CONSULTAR CARDÁPIO ---', font=("Helvica", 25))],
            [sg.Text('Digite o nome do restaurante:', font=("Helvica", 15))],
            [sg.Text('Restaurante:', size=(15, 1)), sg.InputText('', key='restaurante')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Nome do Restaurante').Layout(layout)

        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            self.__window.Close()
            return None

        restaurante = values['restaurante']
        self.__window.Close()
        return restaurante

    def mostrar_cardapio(self, itens):
        if not itens:
            sg.popup("Nenhum item no cardápio.")
        else:
            string_itens = "--- ITENS DO CARDÁPIO ---\n"
            for item in itens:
                string_itens += f"- {item}\n"
            
            sg.Popup(string_itens)

    def mostrar_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        if self.__window:
            self.__window.Close()

    def open(self):
        if self.__window:
            button, values = self.__window.Read()
            return button, values
        return None, None
