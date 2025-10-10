from Funcionario import Funcionario

class TelaFuncionario:
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostrar_opcoes(self):
        while True:
            print("\n=== Menu Funcionário ===")
            print("1 - Cadastrar Funcionário")
            print("2 - Anotar Reserva")
            print("3 - Alterar Reserva")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Nome: ")
                cargo = input("Cargo: ")
                self.__controlador.cadastrar_funcionario(nome, cargo)
                print("Funcionário cadastrado com sucesso!")

            elif opcao == "2":
                nome = input("Nome do funcionário: ")
                funcionario = next((f for f in self.__controlador.listar_funcionarios() if f.nome == nome), None)
                if not funcionario:
                    print("Funcionário não encontrado.")
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
                self.__controlador.anotar_reserva(funcionario, dados_reserva)
                print("Reserva feita com sucesso!")

            elif opcao == "3":
                nome = input("Nome do funcionário: ")
                funcionario = next((f for f in self.__controlador.listar_funcionarios() if f.nome == nome), None)
                if not funcionario:
                    print("Funcionário não encontrado.")
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
                self.__controlador.alterar_reserva(funcionario, id_reserva, novos_dados)
                print("Reserva alterada com sucesso!")

            elif opcao == "0":
                print("Saindo do menu Funcionário.")
                break
            else:
                print("Opção inválida!")
