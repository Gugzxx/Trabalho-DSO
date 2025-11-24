from Objetos.funcionario import Funcionario
from Objetos.cliente import Cliente
from collections import Counter
from datetime import datetime
import FreeSimpleGUI as sg
from Excecoes.cliente_inexistente import ClienteInexistenteException

class ControladorFuncionario:
    def __init__(self, sistema, tela_funcionario, controlador_usuario, controlador_reserva, controlador_restaurante, controlador_cliente):
        self.sistema = sistema
        self.tela_funcionario = tela_funcionario
        self.controlador_usuario = controlador_usuario
        self.controlador_reserva = controlador_reserva
        self.controlador_restaurante = controlador_restaurante
        self.controlador_cliente = controlador_cliente

    def buscar_funcionario(self, login):
        return self.sistema.buscar_funcionario(login)

    def listar_clientes_detalhado(self):
        clientes = self.sistema.clientes
        if not clientes:
            sg.popup("Nenhum cliente cadastrado.")
        else:
            lista_texto = "--- LISTA COMPLETA DE CLIENTES ---\n\n"
            for cliente in clientes:
                lista_texto += f"Login: {cliente.login}\n"
                lista_texto += f"Nome: {cliente.nome}\n"
                lista_texto += f"Email: {cliente.email}\n"
                lista_texto += "─" * 40 + "\n\n"
            
            sg.PopupScrolled(lista_texto, title="Lista de Clientes", size=(60, 20))

    def menu_funcionario(self, funcionario_logado):
        while True:
            escolha = self.tela_funcionario.mostrar_menu()
            if escolha is None:  # Usuário fechou a janela
                break
                
            if escolha == 1:  # Gerenciar Clientes
                lista_clientes = self.sistema.clientes
                opcao = self.tela_funcionario.mostrar_menu_gerenciar_clientes(lista_clientes)
                if opcao is None:  # Usuário fechou a janela
                    continue
                
                if opcao == 'l':  # Listar Clientes
                    self.listar_clientes_detalhado()
                    
                elif opcao == 'a':  # Adicionar Cliente
                    login = self.tela_funcionario.pedir_login()
                    if login is None:  # Usuário clicou Cancelar
                        continue
                        
                    if self.sistema.buscar_usuario(login):
                        self.tela_funcionario.mostrar_mensagem("Login já existe.")
                    else:
                        # Tela para cadastrar cliente
                        sg.ChangeLookAndFeel('DarkTeal4')
                        layout = [
                            [sg.Text('--- CADASTRAR CLIENTE ---', font=("Helvica", 25))],
                            [sg.Text('Senha:', size=(15, 1)), sg.InputText('', password_char='*', key='senha')],
                            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
                            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
                            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                        ]
                        window = sg.Window('Cadastrar Cliente', layout)
                        button, values = window.read()
                        window.close()
                        
                        if button in (None, 'Cancelar'):
                            continue
                            
                        senha = values['senha']
                        nome = values['nome']
                        email = values['email']
                        self.sistema.cadastrar_cliente(login, senha, nome, email)
                        self.tela_funcionario.mostrar_mensagem("Cliente cadastrado.")
                        
                elif opcao == 'r':  # Remover Cliente
                    login = self.tela_funcionario.pedir_login()
                    if login is None:  # Usuário clicou Cancelar
                        continue
                        
                    try:
                        self.sistema.remover_cliente(login)
                        self.tela_funcionario.mostrar_mensagem("Cliente removido.")
                    except ClienteInexistenteException as e:
                        self.tela_funcionario.mostrar_mensagem(str(e))
                        
                elif opcao == '0':  # Voltar
                    continue

            elif escolha == 2:  # Gerenciar Funcionários
                if not funcionario_logado.is_admin:
                    self.tela_funcionario.mostrar_mensagem("Acesso negado.")
                    continue
                
                opcao = self.tela_funcionario.mostrar_menu_gerenciar_funcionarios(self.sistema.funcionarios)
                if opcao is None:  # Usuário fechou a janela
                    continue
                
                if opcao == 'a':  # Adicionar Funcionário
                    dados = self.controlador_usuario.pegar_dados_novo_funcionario()
                    if dados is None:  # Usuário clicou Cancelar
                        continue
                        
                    login, senha, nome, email, is_admin = dados
                    if self.sistema.cadastrar_funcionario(login, senha, nome, email, is_admin):
                        self.tela_funcionario.mostrar_mensagem("Funcionário cadastrado.")
                    else:
                        self.tela_funcionario.mostrar_mensagem("Login já existe.")
                        
                elif opcao == 'r':  # Remover Funcionário
                    login = self.tela_funcionario.pedir_login()
                    if login is None:  # Usuário clicou Cancelar
                        continue
                        
                    func = self.sistema.buscar_funcionario(login)
                    if func:
                        self.sistema.remover_funcionario(login)
                        self.tela_funcionario.mostrar_mensagem("Funcionário removido.")
                    else:
                        self.tela_funcionario.mostrar_mensagem("Funcionário não encontrado.")
            
            elif escolha == 3:  # Ver Todas Reservas
                reservas = self.sistema.listar_todas_reservas()
                self.tela_funcionario.mostrar_reservas(reservas)
            
            elif escolha == 4:  # Gerenciar Restaurantes
                self.controlador_restaurante.menu_restaurante()
            
            elif escolha == 7:  # Relatórios
                self.menu_relatorios()
            
            elif escolha == 0:  # Logout
                break
            else:
                self.tela_funcionario.mostrar_mensagem("Opção inválida.")

    def menu_relatorios(self):
        while True:
            escolha = self.tela_funcionario.mostrar_menu_relatorios()
            if escolha is None:  # Usuário clicou Cancelar
                break
                
            reservas = self.sistema.listar_todas_reservas()
            
            if escolha == '1':  # Mesas Mais Reservadas
                contagem = Counter((r.restaurante, r.mesa_numero) for r in reservas)
                dados_relatorio = contagem.most_common(10)
                self.tela_funcionario.mostrar_relatorio_mesas(dados_relatorio)
            
            elif escolha == '2':  # Meses com Maior Movimento
                contagem_meses = Counter()
                for r in reservas:
                    try:
                        mes_ano = r.data_hora.split()[0].split('/')[1:]
                        chave = f"{mes_ano[0]}/{mes_ano[1]}"
                        contagem_meses[chave] += 1
                    except:
                        continue
                dados_relatorio = contagem_meses.most_common()
                self.tela_funcionario.mostrar_relatorio_meses(dados_relatorio)
            
            elif escolha == '0':  # Voltar
                break
