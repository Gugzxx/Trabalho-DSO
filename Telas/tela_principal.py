class TelaPrincipal:
    def mostrar_menu_inicial(self):
        print("\n=== SISTEMA DE RESERVAS ===")
        print("1 - Login")
        print("2 - Cadastrar Cliente")
        print("0 - Sair")
        return input("Escolha: ")

    def mostrar_login(self):
        print("\n--- Login ---")
        login = input("Login: ")
        senha = input("Senha: ")
        print("Entrar como:")
        print("1 - Cliente")
        print("2 - Funcionário")
        tipo_opt = input("Opção: ")
        tipo = "cliente" if tipo_opt == '1' else "funcionario"
        return login, senha, tipo

    def mostrar_mensagem(self, msg):
        print(f"\n>>> {msg} <<<\n")
