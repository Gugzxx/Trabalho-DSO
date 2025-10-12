from Telas.AbstractTela import AbstractTela

class TelaUsuario(AbstractTela):
    def pedir_dados_usuario(self):
        login = input("Login: ")
        senha = input("Senha: ")
        nome = input("Nome: ")
        email = input("Email: ")
        return login, senha, nome, email

    def mostrar_mensagem(self, msg):
        print(msg)
