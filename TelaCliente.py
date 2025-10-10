from AbstractTela import AbstractTela
from Cliente import Cliente

class TelaCliente:
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostrar_tela_opcoes(self):
        while True:
            print("\n=== Menu Cliente ===")
            print("1 - Cadastrar Cliente")
            print("2 - Anotar Reserva")
            print("3 - Alterar Reserva")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Nome: ")
                telefone = input("Telefone (apenas números): ")
                email = input("Email: ")                
                self.__controlador.cadastrar_cliente(nome, telefone, email)
                print("Cliente cadastrado com sucesso!")

            elif opcao == "2":
                nome = input("Nome do cliente: ")
                cliente = next((f for f in self.__controlador.listar_clientes() if f.nome == nome), None)
                if not cliente:
                    print("Cliente não encontrado.")
                    continue
                dados_reserva = {}
                dados_reserva["data"] = input("Data da reserva: ")
                dados_reserva["hora"] = input("Hora da reserva: ")
                while True:
                    try:
                        dados_reserva["qtd_pessoas"] = int(input("Quantidade de pessoas: "))
                        break
                    except ValueError:
                        print("Digite um número inteiro válido.")
                while True:
                    try:
                        dados_reserva["mesa"] = int(input("Número da mesa: "))
                        break
                    except ValueError:
                        print("Digite um número inteiro válido.")
                self.__controlador.anotar_reserva(cliente, dados_reserva)
                print("Reserva feita com sucesso!")

            elif opcao == "3":
                nome = input("Nome do cliente: ")
                cliente = next((f for f in self.__controlador.listar_clientes() if f.nome == nome), None)
                if not cliente:
                    print("Cliente não encontrado.")
                    continue
                id_reserva = int(input("ID da reserva a alterar: "))
                novos_dados = {}
                novos_dados["data"] = input("Nova data da reserva: ")
                novos_dados["hora"] = input("Nova hora da reserva: ")
                while True:
                    try:
                        novos_dados["qtd_pessoas"] = int(input("Nova quantidade de pessoas: "))
                        break
                    except ValueError:
                        print("Digite um número inteiro válido.")
                while True:
                    try:
                        novos_dados["mesa"] = int(input("Novo número da mesa: "))
                        break
                    except ValueError:
                        print("Digite um número inteiro válido.")
                self.__controlador.alterar_reserva(cliente, id_reserva, novos_dados)
                print("Reserva alterada com sucesso!")

            elif opcao == "0":
                print("Saindo do menu Cliente.")
                break
            else:
                print("Opção inválida!")
