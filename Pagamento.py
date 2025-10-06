class Pagamento:
    def __init__(self, forma_pagamento: str, valor: float, data_pagamento: str, status: str):
        self.__forma_pagamento = None
        self.__valor = None
        self.__data_pagamento = None
        self.__status = None

    if isinstance(forma_pagamento, str):
        self.__forma_pagamento = forma_pagamento
    if isinstance(valor, float):
        self.__valor = valor
    if isinstance(data_pagamento, str):
        self.__data_pagamento = data_pagamento
    if isinstance(status, str):
        self.__status = status

    @property
    def forma_pagamento(self):
        return self.__forma_pagamento

    @forma_pagamento.setter
    def forma_pagamento(self, forma_pagamento: str):
        if isinstance(forma_pagamento, str) and len(forma_pagamento) > 0:
            self.__forma_pagamento = forma_pagamento

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        if isinstance(valor, (int, float)) and valor >= 0:
            self.__valor = valor

    @property
    def data_pagamento(self):
        return self.__data_pagamento

    @data_pagamento.setter
    def data_pagamento(self, data_pagamento: str):
        if isinstance(data_pagamento, str) and len(data_pagamento) > 0:
            self.__data_pagamento = data_pagamento

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        if isinstance(status, str) and len(status) > 0:
            self.__status = status
