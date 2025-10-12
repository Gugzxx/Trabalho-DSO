from Telas.AbstractTela import AbstractTela


class TelaRestaurante(AbstractTela):
    def mostrar_menu(self):
        print("\nMenu Restaurante:")
        print("1 - Listar Restaurantes")
        print("2 - Adicionar Restaurante")
        print("0 - Voltar")
        return input("Escolha: ")

    def mostrar_restaurantes(self, restaurantes):
        if not restaurantes:
            print("Nenhum restaurante cadastrado.")
        else:
            for r in restaurantes:
                print(f"Nome: {r.nome} | Endereço: {r.endereco}")
