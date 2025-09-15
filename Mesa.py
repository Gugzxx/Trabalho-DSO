class Mesa:
    def __init__(self, numero: int, qtd_lugares: int):
        self.__numero = numero
        self.__qtd_lugares = qtd_lugares
        self.__status = "Disponível"

    @property
    def numero(self):
        return self.__numero

    @property
    def qtd_lugares(self):
        return self.__qtd_lugares

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        if status in ["Disponível", "Reservada", "Ocupada"]:
            self.__status = status
