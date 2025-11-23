import FreeSimpleGUI as sg
from Telas.abstract_tela import AbstractTela

class TelaUsuario(AbstractTela):
    def __init__(self):
        self.__window = None

    def pedir_dados_usuario(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS DO USUÁRIO ----------', font=("Helvica", 25))],
            [sg.Text('Login:', size=(15, 1)), sg.InputText('', key='login')],
            [sg.Text('Senha:', size=(15, 1)), sg.InputText('', password_char='*', key='senha')],
            [sg.Text('Nome Completo:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro de Usuário').Layout(layout)

        button, values = self.__window.Read()
        
        if button in (None, 'Cancelar'):
            self.__window.Close()
            return None

        login = values['login']
        senha = values['senha']
        nome = values['nome']
        email = values['email']
        
        self.__window.Close()
        return login, senha, nome, email

    def pedir_is_admin(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- TIPO DE USUÁRIO ----------', font=("Helvica", 25))],
            [sg.Text('É administrador?', font=("Helvica", 15))],
            [sg.Radio('Sim', "RD1", key='sim'), sg.Radio('Não', "RD1", key='nao')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Tipo de Usuário').Layout(layout)

        button, values = self.__window.Read()
        
        if button in (None, 'Cancelar'):
            self.__window.Close()
            return None

        is_admin = values['sim']
        self.__window.Close()
        return is_admin

    def close(self):
        if self.__window:
            self.__window.Close()

    def open(self):
        if self.__window:
            button, values = self.__window.Read()
            return button, values
        return None, None
