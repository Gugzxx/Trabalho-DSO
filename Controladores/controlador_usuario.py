class ControladorUsuario:
    def __init__(self, tela_usuario):
        self.tela_usuario = tela_usuario

    def pegar_dados_novo_funcionario(self):
        login, senha, nome, email = self.tela_usuario.pedir_dados_usuario()
        is_admin = self.tela_usuario.pedir_is_admin()
        return login, senha, nome, email, is_admin
