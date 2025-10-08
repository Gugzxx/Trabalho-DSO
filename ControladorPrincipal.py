from ControladorReserva import ControladorReserva
from ControladorUsuario import ControladorUsuario
from ControladorCliente import ControladorCliente
from ControladorFuncionario import ControladorFuncionario

def main():
    controlador_reserva = ControladorReserva()
    controlador_usuario = ControladorUsuario(controlador_reserva)
    controlador_cliente = ControladorCliente(controlador_reserva)
    controlador_funcionario = ControladorFuncionario(controlador_reserva)

    while True:
        print("\n=== Menu Principal ===")
        print("1 - Menu Usuário")
        print("2 - Menu Cliente")
        print("3 - Menu Funcionário")
        print("4 - Menu Reserva")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            controlador_usuario._ControladorUsuario__tela_usuario.mostrar_opcoes()
        elif opcao == "2":
            controlador_cliente._ControladorCliente__tela_cliente.mostrar_opcoes()
        elif opcao == "3":
            controlador_funcionario._ControladorFuncionario__tela_funcionario.mostrar_opcoes()
        elif opcao == "4":
            controlador_reserva.inicia()
        elif opcao == "0":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

