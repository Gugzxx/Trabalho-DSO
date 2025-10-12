class Reserva:
    _contador_id = 1
    
    def __init__(self, cliente_login, mesa_numero, restaurante, detalhes, data_hora, status=None):
        self.id = Reserva._contador_id
        Reserva._contador_id += 1
        self.cliente_login = cliente_login
        self.mesa_numero = mesa_numero
        self.restaurante = restaurante
        self.detalhes = detalhes
        self.data_hora = data_hora
        self.status = status or "pendente"  # Usar StatusReserva

    def atualizar(self, detalhes=None, data_hora=None, status=None):
        if detalhes:
            self.detalhes = detalhes
        if data_hora:
            self.data_hora = data_hora
        if status:
            self.status = status
