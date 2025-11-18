from Telas.abstract_tela import AbstractTela

class TelaFuncionario(AbstractTela):
    def mostrar_menu(self):
        print("\n--- Painel Administrativo ---")
        print("1 - Gerenciar Clientes")
        print("2 - Gerenciar Funcionários")
        print("3 - Ver Todas Reservas")
        print("4 - Gerenciar Restaurantes e Cardápios")
        print("7 - Relatórios")
        print("0 - Logout")
        return input("Escolha: ")

    def mostrar_menu_gerenciar_clientes(self, clientes):
        print("\n--- Clientes Cadastrados ---")
        if not clientes:
            print("Nenhum cliente.")
        else:
            for c in clientes:
                print(f"- {c.login} ({c.nome})")
        print("\nl - Listar Clientes")
        print("a - Adicionar Cliente")
        print("r - Remover Cliente")
        print("0 - Voltar")
        return input("Escolha: ").lower()

    def mostrar_menu_gerenciar_funcionarios(self, funcionarios):
        print("\n--- Funcionários ---")
        for f in funcionarios:
            tipo = "ADMIN" if f.is_admin else "Comum"
            print(f"- {f.login} [{tipo}]")
        print("a - Adicionar Funcionário")
        print("r - Remover Funcionário")
        print("0 - Voltar")
        return input("Escolha: ").lower()

    def pedir_login(self):
        return input("Digite o login alvo: ")

    def mostrar_reservas(self, reservas):
        print("\n--- Todas as Reservas ---")
        if not reservas:
            print("Nenhuma reserva encontrada.")
        else:
            for r in reservas:
                print(f"ID: {r.id} | Cliente: {r.cliente_login} | Mesa: {r.mesa_numero} | Restaurante: {r.restaurante} | Data/Hora: {r.data_hora} | Status: {r.status}")
        input("Enter para continuar...")

    def mostrar_menu_relatorios(self):
        print("\n--- Relatórios ---")
        print("1 - Mesas Mais Reservadas")
        print("2 - Meses com Maior Movimento")
        print("0 - Voltar")
        return input("Escolha: ")

    def mostrar_relatorio_mesas(self, dados):
        print("\n--- Ranking Mesas ---")
        print(f"{'Restaurante':<15} | {'Mesa':<5} | {'Qtd'}")
        for (rest, mesa), qtd in dados:
            print(f"{rest:<15} | {mesa:<5} | {qtd}")
        input("Enter para continuar...")

    def mostrar_relatorio_meses(self, dados):
        print("\n--- Movimento Mensal ---")
        for mes, qtd in dados:
            print(f"{mes}: {qtd} reservas")
        input("Enter para continuar...")
