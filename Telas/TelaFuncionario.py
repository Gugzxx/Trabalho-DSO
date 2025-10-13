from Telas.AbstractTela import AbstractTela

class TelaFuncionario(AbstractTela):
    def mostrar_menu(self):
        print("\nMenu Funcionário:")
        print("1 - Gerenciar Clientes")
        print("2 - Gerenciar Funcionários")
        print("3 - Ver Todas Reservas")
        print("4 - Gerenciar Restaurantes")
        print("5 - Gerenciar Pagamentos")  
        print("6 - Gerenciar Cardápios")
        print("7 - Gerar Relatórios")
        print("0 - Logout")
        return input("Escolha: ")

    def mostrar_clientes(self, clientes):
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for c in clientes:
                print(f"Login: {c.login} | Nome: {c.nome} | Email: {c.email}")

    def mostrar_funcionarios(self, funcionarios):
        if not funcionarios:
            print("Nenhum funcionário cadastrado.")
        else:
            for f in funcionarios:
                admin_str = "Administrador" if f.is_admin else "Funcionário"
                print(f"Login: {f.login} | Nome: {f.nome} | Email: {f.email} | Tipo: {admin_str}")
