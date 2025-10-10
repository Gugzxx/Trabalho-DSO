def main():
    from ControladorReserva import ControladorReserva
    from ControladorCliente import ControladorCliente
    from ControladorFuncionario import ControladorFuncionario

    controlador_reserva = ControladorReserva()
    controlador_cliente = ControladorCliente(controlador_reserva)
    controlador_funcionario = ControladorFuncionario(controlador_reserva)
    
    while True:
        print("\n=== Menu Principal ===")
        print("1 - Menu Cliente")
        print("2 - Menu Funcionário")
        print("3 - Menu Reserva")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            controlador_cliente._ControladorCliente__tela_cliente.mostrar_tela_opcoes()
        elif opcao == "2":
            controlador_funcionario._ControladorFuncionario__tela_funcionario.mostrar_tela_opcoes()
        elif opcao == "3":
            controlador_reserva.inicia()
        elif opcao == "0":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
