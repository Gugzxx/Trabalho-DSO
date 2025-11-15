class ControladorSistema:
    def __init__(self, sistema, controlador_principal):
        self.sistema = sistema
        self.controlador_principal = controlador_principal

    def executar(self, tela_principal):
        while True:
            login, senha, tipo = tela_principal.mostrar_login()
            if self.sistema.autenticar(login, senha, tipo):
                tela_principal.mostrar_mensagem(f"Bem-vindo, {login}!")
                if tipo == "cliente":
                    self.controlador_principal.menu_cliente()
                else:
                    self.controlador_principal.menu_funcionario()
            else:
                tela_principal.mostrar_mensagem("Login ou senha incorretos. Tente novamente.")
