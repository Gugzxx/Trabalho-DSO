from Telas.abstract_tela import AbstractTela

class TelaUsuario(AbstractTela):
    def pedir_dados_usuario(self):
        print("--- Dados do Usuário ---")
        login = input("Login: ")
        senha = input("Senha: ")
        nome = input("Nome Completo: ")
        email = input("Email: ")
        return login, senha, nome, email
    
    def pedir_is_admin(self):
        resp = input("É administrador? (s/n): ").lower()
        return resp == 's'
