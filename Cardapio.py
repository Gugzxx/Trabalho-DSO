class Cardapio:
    def __init__(self, entradas: list, principais: list, sobremesas: list, bebidas: list):
        self.__entradas = entradas
        self.__principais = principais
        self.__sobremesas = sobremesas
        self.__bebidas = bebidas

    if isinstance(entradas, list):
        self.__entradas = entradas
    if isinstance(principais, list):
        self.__principais = principais
    if isinstance(sobremesas, list):
        self.__sobremesas = sobremesas
    if isinstance(bebidas, list):
        self.__bebidas = bebidas

    @property
    def entradas(self):
        return self.__entradas

    @entradas.setter
    def entradas(self, entradas: list):
        if isinstance(entradas, list):
            self.__entradas = entradas

    @property
    def principais(self):
        return self.__principais

    @principais.setter
    def principais(self, principais: list):
        if isinstance(principais, list):
            self.__principais = principais

    @property
    def sobremesas(self):
        return self.__sobremesas

    @sobremesas.setter
    def sobremesas(self, sobremesas: list):
        if isinstance(sobremesas, list):
            self.__sobremesas = sobremesas

    @property
    def bebidas(self):
        return self.__bebidas

    @bebidas.setter
    def bebidas(self, bebidas: list):
        if isinstance(bebidas, list):
