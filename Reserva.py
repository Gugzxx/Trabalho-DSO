from Cliente import Cliente
from Funcionario import Funcionario
from Usuario import Usuario
from Mesa import Mesa
from Pagamento import Pagamento
from StatusReserva import StatusReserva

class Reserva:
    def __init__(self, id_reserva: int, data: str, hora: str, qtd_pessoas: int, status: StatusReserva):
        self.__id_reserva = id_reserva
        self.__data = data
        self.__hora = hora
        self.__qtd_pessoas = qtd_pessoas
        self.__status = status

        self.__cliente = None
        self.__mesa = None
        self.__usuario_responsavel = None
        self.__pagamento = None

    @property
    def id_reserva(self):
        return self.__id_reserva

    @id_reserva.setter
    def id_reserva(self, id_reserva: int):
        if isinstance(id_reserva, int) and id_reserva > 0:
            self.__id_reserva = id_reserva

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        if isinstance(data, str) and len(data) > 0:
            self.__data = data

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self, hora: str):
        if isinstance(hora, str) and len(hora) > 0:
            self.__hora = hora

    @property
    def qtd_pessoas(self):
        return self.__qtd_pessoas

    @qtd_pessoas.setter
    def qtd_pessoas(self, qtd_pessoas: int):
        if isinstance(qtd_pessoas, int) and qtd_pessoas > 0:
            self.__qtd_pessoas = qtd_pessoas

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        if isinstance(status, str) and len(status) > 0:
            self.__status = status

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
 
    @property
    def mesa(self):
        return self.__mesa

    @mesa.setter
    def mesa(self, mesa: Mesa):
        if isinstance(mesa, Mesa):
            self.__mesa = mesa

    @property
    def usuario_responsavel(self):
        return self.__usuario_responsavel

    @usuario_responsavel.setter
    def usuario_responsavel(self, usuario: Usuario):
        if isinstance(usuario, (Funcionario, Cliente)):
            self.__usuario_responsavel = usuario

    @property
    def pagamento(self):
        return self.__pagamento

    @pagamento.setter
    def pagamento(self, pagamento: Pagamento):
        if isinstance(pagamento, Pagamento):
            self.__pagamento = pagamento
