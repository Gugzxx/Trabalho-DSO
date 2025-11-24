import FreeSimpleGUI as sg

class TelaPrincipal:
    def __init__(self):
        self.__window = None

    def mostrar_menu_inicial(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('=== SISTEMA DE RESERVAS ===', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Login', "RD1", key='1')],
            [sg.Radio('Sair', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Reservas').Layout(layout)

        button, values = self.__window.Read()
        if values['1']:
            opcao = 1
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        else:
            opcao = 0
        self.__window.Close()
        return opcao

    def mostrar_login(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('--- LOGIN ---', font=("Helvica", 25))],
            [sg.Text('Login:', size=(15, 1)), sg.InputText('', key='login')],
            [sg.Text('Senha:', size=(15, 1)), sg.InputText('', password_char='*', key='senha')],
            [sg.Text('Entrar como:', font=("Helvica", 15))],
            [sg.Radio('Cliente', "RD1", key='cliente')],
            [sg.Radio('Funcionário', "RD1", key='funcionario')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Login').Layout(layout)

        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            self.__window.Close()
            return None

        login = values['login']
        senha = values['senha']
        tipo = "cliente" if values['cliente'] else "funcionario"
        
        self.__window.Close()
        return login, senha, tipo

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
