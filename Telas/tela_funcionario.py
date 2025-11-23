import FreeSimpleGUI as sg
from Telas.abstract_tela import AbstractTela

class TelaFuncionario(AbstractTela):
    def __init__(self):
        self.__window = None

    def mostrar_menu(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('--- PAINEL ADMINISTRATIVO ---', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Gerenciar Clientes', "RD1", key='1')],
            [sg.Radio('Gerenciar Funcionários', "RD1", key='2')],
            [sg.Radio('Ver Todas Reservas', "RD1", key='3')],
            [sg.Radio('Gerenciar Restaurantes e Cardápios', "RD1", key='4')],
            [sg.Radio('Relatórios', "RD1", key='7')],
            [sg.Radio('Logout', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Painel Administrativo').Layout(layout)

        button, values = self.__window.Read()
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        elif values['7']:
            opcao = 7
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        else:
            opcao = 0
        self.__window.Close()
        return opcao

    def mostrar_menu_gerenciar_clientes(self, clientes):
        sg.ChangeLookAndFeel('DarkTeal4')
        
        clientes_texto = "--- CLIENTES CADASTRADOS ---\n"
        if not clientes:
            clientes_texto += "Nenhum cliente.\n"
        else:
            for c in clientes:
                clientes_texto += f"- {c.login} ({c.nome})\n"
        
        layout = [
            [sg.Text(clientes_texto, font=("Helvica", 12))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Listar Clientes', "RD1", key='l')],
            [sg.Radio('Adicionar Cliente', "RD1", key='a')],
            [sg.Radio('Remover Cliente', "RD1", key='r')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Gerenciar Clientes').Layout(layout)

        button, values = self.__window.Read()
        if values['l']:
            opcao = 'l'
        elif values['a']:
            opcao = 'a'
        elif values['r']:
            opcao = 'r'
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = '0'
        else:
            opcao = '0'
        self.__window.Close()
        return opcao

    def mostrar_menu_gerenciar_funcionarios(self, funcionarios):
        sg.ChangeLookAndFeel('DarkTeal4')
        
        funcionarios_texto = "--- FUNCIONÁRIOS ---\n"
        for f in funcionarios:
            tipo = "ADMIN" if f.is_admin else "Comum"
            funcionarios_texto += f"- {f.login} [{tipo}]\n"
        
        layout = [
            [sg.Text(funcionarios_texto, font=("Helvica", 12))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Adicionar Funcionário', "RD1", key='a')],
            [sg.Radio('Remover Funcionário', "RD1", key='r')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Gerenciar Funcionários').Layout(layout)

        button, values = self.__window.Read()
        if values['a']:
            opcao = 'a'
        elif values['r']:
            opcao = 'r'
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = '0'
        else:
            opcao = '0'
        self.__window.Close()
        return opcao

    def pedir_login(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('--- SELECIONAR LOGIN ---', font=("Helvica", 25))],
            [sg.Text('Digite o login alvo:', font=("Helvica", 15))],
            [sg.Text('Login:', size=(15, 1)), sg.InputText('', key='login')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Login').Layout(layout)

        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            self.__window.Close()
            return None

        login = values['login']
        self.__window.Close()
        return login

    def mostrar_reservas(self, reservas):
        if not reservas:
            sg.popup("Nenhuma reserva encontrada.")
        else:
            string_reservas = "--- TODAS AS RESERVAS ---\n"
            for r in reservas:
                string_reservas += f"ID: {r.id} | Cliente: {r.cliente_login} | Mesa: {r.mesa_numero} | Restaurante: {r.restaurante} | Data/Hora: {r.data_hora} | Status: {r.status}\n"
            
            sg.Popup(string_reservas)

    def mostrar_menu_relatorios(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('--- RELATÓRIOS ---', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Mesas Mais Reservadas', "RD1", key='1')],
            [sg.Radio('Meses com Maior Movimento', "RD1", key='2')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Relatórios').Layout(layout)

        button, values = self.__window.Read()
        if values['1']:
            opcao = '1'
        elif values['2']:
            opcao = '2'
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = '0'
        else:
            opcao = '0'
        self.__window.Close()
        return opcao

    def mostrar_relatorio_mesas(self, dados):
        string_relatorio = "--- RANKING MESAS ---\n"
        string_relatorio += f"{'Restaurante':<15} | {'Mesa':<5} | {'Qtd'}\n"
        for (rest, mesa), qtd in dados:
            string_relatorio += f"{rest:<15} | {mesa:<5} | {qtd}\n"
        
        sg.Popup(string_relatorio)

    def mostrar_relatorio_meses(self, dados):
        string_relatorio = "--- MOVIMENTO MENSAL ---\n"
        for mes, qtd in dados:
            string_relatorio += f"{mes}: {qtd} reservas\n"
        
        sg.Popup(string_relatorio)

    def close(self):
        if self.__window:
            self.__window.Close()

    def open(self):
        if self.__window:
            button, values = self.__window.Read()
            return button, values
        return None, None
