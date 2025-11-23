import FreeSimpleGUI as sg
from Telas.abstract_tela import AbstractTela

class TelaRestaurante(AbstractTela):
    def __init__(self):
        self.__window = None

    def mostrar_menu(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('--- GESTÃO DE RESTAURANTES ---', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Listar Restaurantes', "RD1", key='1')],
            [sg.Radio('Adicionar Restaurante', "RD1", key='2')],
            [sg.Radio('Gerenciar Cardápio', "RD1", key='3')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Gestão de Restaurantes').Layout(layout)

        button, values = self.__window.Read()
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        else:
            opcao = 0
        self.__window.Close()
        return opcao

    def mostrar_restaurantes(self, restaurantes):
        if not restaurantes:
            sg.popup("Nenhum restaurante cadastrado.")
        else:
            string_restaurantes = ""
            for r in restaurantes:
                string_restaurantes += f"Nome: {r.nome} | Endereço: {r.endereco}\n"
            sg.popup('--- LISTA DE RESTAURANTES ---', string_restaurantes)

    def pedir_dados_restaurante(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('--- DADOS DO RESTAURANTE ---', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Endereço:', size=(15, 1)), sg.InputText('', key='endereco')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro de Restaurante').Layout(layout)

        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            self.__window.Close()
            return None

        nome = values['nome']
        endereco = values['endereco']
        self.__window.Close()
        return nome, endereco

    def pedir_nome_restaurante(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('--- SELECIONAR RESTAURANTE ---', font=("Helvica", 25))],
            [sg.Text('Digite o nome do restaurante:', font=("Helvica", 15))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Restaurante').Layout(layout)

        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            self.__window.Close()
            return None

        nome = values['nome']
        self.__window.Close()
        return nome

    def mostrar_menu_cardapio(self, nome_restaurante):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text(f'--- CARDÁPIO: {nome_restaurante} ---', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Adicionar Item', "RD1", key='1')],
            [sg.Radio('Remover Item', "RD1", key='2')],
            [sg.Radio('Listar Itens', "RD1", key='3')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Gerenciar Cardápio').Layout(layout)

        button, values = self.__window.Read()
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        else:
            opcao = 0
        self.__window.Close()
        return opcao

    def pedir_nome_item(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('--- ADICIONAR ITEM ---', font=("Helvica", 25))],
            [sg.Text('Digite o nome do item:', font=("Helvica", 15))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Nome do Item').Layout(layout)

        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            self.__window.Close()
            return None

        nome = values['nome']
        self.__window.Close()
        return nome

    def mostrar_itens_cardapio(self, itens):
        if not itens:
            sg.popup("Nenhum item no cardápio.")
        else:
            string_itens = "--- ITENS ---\n"
            for item in itens:
                string_itens += f"- {item}\n"
            sg.popup(string_itens)

    def close(self):
        if self.__window:
            self.__window.Close()

    def open(self):
        if self.__window:
            button, values = self.__window.Read()
            return button, values
        return None, None
