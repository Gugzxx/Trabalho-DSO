class Pagamento:
    def __init__(self, reserva_id, valor, metodo):
        self.reserva_id = reserva_id
        self.valor = valor
        self.metodo = metodo  # ex: "cartao", "dinheiro"
        self.status = "pendente"

    def confirmar_pagamento(self):
        self.status = "confirmado"
