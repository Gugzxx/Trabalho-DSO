from Funcionario import Funcionario
from ControladorReserva import ControladorReserva

class ControladorFuncionario:
    def __init__(self, controlador_reserva):
        self.__controlador_reserva = controlador_reserva
        self.__funcionarios = []
        self.__tela_funcionario = TelaFuncionario(self)

    def cadastrar_funcionario(self, nome, cargo):
        funcionario = Funcionario(nome, cargo)
        self.__funcionarios.append(funcionario)
        return funcionario

    def anotar_reserva(self, funcionario, dados_reserva):
        return self.__controlador_reserva.solicitar_reserva(funcionario, dados_reserva)

    def alterar_reserva(self, funcionario, id_reserva, novos_dados):
        return self.__controlador_reserva.alterar_reserva(funcionario, id_reserva, novos_dados)

    def listar_funcionarios(self):
        return self.__funcionarios
