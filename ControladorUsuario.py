class ControladorUsuario:
    def __init__(self, sistema, tela_usuario):
        self.sistema = sistema
        self.tela_usuario = tela_usuario

    def criar_cliente(self):
        login, senha, nome, email = self.tela_usuario.pedir_dados_usuario()
        if self.sistema.cadastrar_cliente(login, senha, nome, email):
            self.tela_usuario.mostrar_mensagem("Cliente cadastrado com sucesso!")
        else:
            self.tela_usuario.mostrar_mensagem("Erro: Login já existe.")

    def criar_funcionario(self):
        login, senha, nome, email = self.tela_usuario.pedir_dados_usuario()
        is_admin = input("É administrador? (s/n): ").lower() == 's'
        if self.sistema.cadastrar_funcionario(login, senha, nome, email, is_admin):
            self.tela_usuario.mostrar_mensagem("Funcionário cadastrado com sucesso!")
        else:
            self.tela_usuario.mostrar_mensagem("Erro: Login já existe.")
