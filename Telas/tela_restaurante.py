from Telas.abstract_tela import AbstractTela

class TelaRestaurante(AbstractTela):
    def mostrar_menu(self):
        print("\n--- Gestão de Restaurantes ---")
        print("1 - Listar Restaurantes")
        print("2 - Adicionar Restaurante")
        print("3 - Gerenciar Cardápio")
        print("0 - Voltar")
        return input("Escolha: ")

    def mostrar_restaurantes(self, restaurantes):
        if not restaurantes:
            print("Nenhum restaurante cadastrado.")
        else:
            for r in restaurantes:
                print(f"Nome: {r.nome} | Endereço: {r.endereco}")

    def pedir_dados_restaurante(self):
        nome = input("Nome do restaurante: ")
        endereco = input("Endereço: ")
        return nome, endereco

    def pedir_nome_restaurante(self):
        return input("Digite o nome do restaurante alvo: ")

    def mostrar_menu_cardapio(self, nome_restaurante):
        print(f"\n--- Cardápio: {nome_restaurante} ---")
        print("1 - Adicionar Item")
        print("2 - Remover Item")
        print("3 - Listar Itens")
        print("0 - Voltar")
        return input("Escolha: ")

    def pedir_nome_item(self):
        return input("Nome do item: ")

    def mostrar_itens_cardapio(self, itens):
        print("--- Itens ---")
        for item in itens:
            print(f"- {item}")
