from Objetos.funcionario import Funcionario
from Objetos.cliente import Cliente
from collections import Counter
from datetime import datetime

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

    def menu_funcionario(self, funcionario_logado):
        while True:
            escolha = self.tela_funcionario.mostrar_menu()
            
            if escolha == '1':
                lista_clientes = self.sistema.clientes
                opcao = self.tela_funcionario.mostrar_menu_gerenciar_clientes(lista_clientes)
                
                if opcao == 'l':
                    self.tela_funcionario.mostrar_mensagem("Lista de clientes exibida acima.")
                elif opcao == 'a':
                    login = self.tela_funcionario.pedir_login()
                    if self.sistema.buscar_usuario(login):
                        self.tela_funcionario.mostrar_mensagem("Login já existe.")
                    else:
                        senha = input("Digite a senha: ")
                        nome = input("Digite o nome: ")
                        email = input("Digite o email: ")
                        novo_cliente = Cliente(login, senha, nome, email)
                        self.sistema.clientes.append(novo_cliente)
                        self.sistema.usuarios.append(novo_cliente)
                        self.tela_funcionario.mostrar_mensagem("Cliente cadastrado.")
                elif opcao == 'r':
                    login = self.tela_funcionario.pedir_login()
                    cliente = self.sistema.buscar_cliente(login)
                    if cliente:
                        self.sistema.clientes.remove(cliente)
                        self.sistema.usuarios.remove(cliente)
                        self.tela_funcionario.mostrar_mensagem("Cliente removido.")
                    else:
                        self.tela_funcionario.mostrar_mensagem("Cliente não encontrado.")
                elif opcao == '0':
                    continue

            elif escolha == '2':
                if not funcionario_logado.is_admin:
                    self.tela_funcionario.mostrar_mensagem("Acesso negado.")
                    continue
                
                opcao = self.tela_funcionario.mostrar_menu_gerenciar_funcionarios(self.sistema.funcionarios)
                if opcao == 'a':
                    dados = self.controlador_usuario.pegar_dados_novo_funcionario()
                    if dados:
                        login, senha, nome, email, is_admin = dados
                        if self.sistema.buscar_funcionario(login):
                            self.tela_funcionario.mostrar_mensagem("Login já existe.")
                        else:
                            novo_func = Funcionario(login, senha, nome, email, is_admin)
                            self.sistema.funcionarios.append(novo_func)
                            self.sistema.usuarios.append(novo_func)
                            self.tela_funcionario.mostrar_mensagem("Funcionário cadastrado.")
                elif opcao == 'r':
                    login = self.tela_funcionario.pedir_login()
                    func = self.sistema.buscar_funcionario(login)
                    if func:
                        self.sistema.funcionarios.remove(func)
                        self.sistema.usuarios.remove(func)
                        self.tela_funcionario.mostrar_mensagem("Funcionário removido.")
            
            elif escolha == '3': 
                self.controlador_reserva.listar_todas_reservas()
            
            elif escolha == '4':
                self.controlador_restaurante.menu_restaurante()
            
            elif escolha == '7':
                self.menu_relatorios()
            
            elif escolha == '0':
                break

    def menu_relatorios(self):
        while True:
            escolha = self.tela_funcionario.mostrar_menu_relatorios()
            reservas = self.controlador_reserva.reservas
            
            if escolha == '1':
                contagem = Counter((r.restaurante, r.mesa_numero) for r in reservas)
                dados_relatorio = contagem.most_common(10)
                self.tela_funcionario.mostrar_relatorio_mesas(dados_relatorio)
            
            elif escolha == '2':
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
            
            elif escolha == '0':
                break
