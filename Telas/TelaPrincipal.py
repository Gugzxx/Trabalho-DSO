class TelaPrincipal:
    def mostrar_login(self):
        print("\n=== Tela de Login ===")
        login = input("Login: ")
        senha = input("Senha: ")
        tipo = input("Tipo (cliente/funcionario): ").lower()
        return login, senha, tipo

    def mostrar_menu_cliente(self):
        print("\nMenu Cliente:")
        print("1. Listar reservas")
        print("2. Criar reserva")
        print("3. Alterar reserva")
        print("4. Excluir reserva")
        print("0. Logout")
        escolha = input("Escolha: ")
        return escolha

    def mostrar_menu_funcionario(self):
        print("\nMenu Funcionário:")
        print("1. Gerenciar clientes")
        print("2. Gerenciar funcionários")
        print("3. Ver todas as reservas")
        print("0. Logout")
        escolha = input("Escolha: ")
        return escolha

    def mostrar_mensagem(self, texto):
        print(texto)
