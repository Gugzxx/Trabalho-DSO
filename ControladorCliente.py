from Cliente import Cliente
from TelaCliente import TelaCliente


class ControladorCliente:
    def __init__(self, controlador_reserva):
        self.__controlador_reserva = controlador_reserva
        self.__clientes = []
        self.__tela_cliente = TelaCliente(self)

    def cadastrar_cliente(self, nome):
        cliente = Cliente(nome)
        self.__clientes.append(cliente)
        return cliente

    def anotar_reserva(self, cliente, dados_reserva):
        return self.__controlador_reserva.solicitar_reserva(cliente, dados_reserva)

    def alterar_reserva(self, cliente, id_reserva, novos_dados):
        return self.__controlador_reserva.alterar_reserva(cliente, id_reserva, novos_dados)

    def listar_clientes(self):
        return self.__clientes
