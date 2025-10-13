class Pagamento:
    def __init__(self, reserva_id: int, valor: float, metodo: str):
        self.__reserva_id = None
        self.__valor = None
        self.__metodo = None  # ex: "cartao", "dinheiro"
        self.status = "pendente"
    
        if isinstance(reserva_id, int) and reserva_id > 0:
            self.__reserva_id = reserva_id
        if isinstance(valor, (int, float)) and valor >= 0:
            self.__valor = valor
        if isinstance(metodo, str):
            self.__metodo = metodo
    
    @property
    def reserva_id(self):
        return self.__reserva_id
    
    @reserva_id.setter
    def reserva_id(self, reserva_id: int):
        if isinstance(reserva_id, int) and reserva_id > 0:
            self.__reserva_id = reserva_id
        else:
            raise ValueError("ID da reserva deve ser um inteiro positivo.")
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor: float):
        if isinstance(valor, (int, float)) and valor >= 0:
            self.__valor = valor
        else:
            raise ValueError("Valor deve ser um número não negativo.")
    
    @property
    def metodo(self):
        return self.__metodo
    
    @metodo.setter
    def metodo(self, metodo: str):
        if isinstance(metodo, str):
            self.__metodo = metodo

    def confirmar_pagamento(self):
        self.status = "confirmado"
