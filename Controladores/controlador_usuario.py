class ControladorUsuario:
    def __init__(self, tela_usuario):
        self.tela_usuario = tela_usuario

    def pegar_dados_novo_funcionario(self):
        dados = self.tela_usuario.pedir_dados_usuario()
        if dados is None:  # Usuário clicou Cancelar
            return None
            
        login, senha, nome, email = dados
        
        is_admin = self.tela_usuario.pedir_is_admin()
        if is_admin is None:  # Usuário clicou Cancelar
            return None
            
        return login, senha, nome, email, is_admin

    def pedir_dados_usuario(self):
        return self.tela_usuario.pedir_dados_usuario()
