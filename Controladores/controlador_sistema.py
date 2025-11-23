class ControladorSistema:
    def __init__(self, sistema, controlador_principal):
        self.sistema = sistema
        self.controlador_principal = controlador_principal

    def executar(self, tela_principal):
        while True:
            # Primeiro mostra o menu inicial, não o login direto
            opcao = tela_principal.mostrar_menu_inicial()
            
            if opcao == 1:  # Login
                dados_login = tela_principal.mostrar_login()
                if dados_login is None:  # Usuário clicou Cancelar
                    continue
                    
                login, senha, tipo = dados_login
                if self.sistema.autenticar(login, senha, tipo):
                    tela_principal.mostrar_mensagem(f"Bem-vindo, {login}!")
                    if tipo == "cliente":
                        self.controlador_principal.menu_cliente()
                    else:
                        self.controlador_principal.menu_funcionario()
                else:
                    tela_principal.mostrar_mensagem("Login ou senha incorretos. Tente novamente.")
                    
            elif opcao == 2:  # Cadastrar Cliente
                # Aqui você precisa implementar o cadastro de cliente
                tela_principal.mostrar_mensagem("Funcionalidade de cadastro em desenvolvimento")
                
            elif opcao == 0:  # Sair
                tela_principal.mostrar_mensagem("Saindo do sistema...")
                break
