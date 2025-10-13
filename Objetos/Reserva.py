class Reserva:
    _contador_id = 1
    
    def __init__(self, cliente_login: str, mesa_numero: int, restaurante: str, detalhes: str, data_hora: str, status=None):
        self.id = Reserva._contador_id
        Reserva._contador_id += 1
        self.__cliente_login = None
        self.__mesa_numero = None
        self.__restaurante = None
        self.__detalhes = None
        self.__data_hora = None
        self.status = status or "pendente"  # Usar StatusReserva

        if isinstance(cliente_login, str):
            self.cliente_login = cliente_login
        if isinstance(mesa_numero, int) and mesa_numero > 0:
            self.mesa_numero = mesa_numero
        if isinstance(restaurante, str):
            self.restaurante = restaurante
        if isinstance(detalhes, str):
            self.detalhes = detalhes
        if isinstance(data_hora, str):
            self.data_hora = data_hora

    @property
    def cliente_login(self):
        return self.__cliente_login
    
    @cliente_login.setter
    def cliente_login(self, cliente_login: str):
        self.__cliente_login = cliente_login

    @property
    def mesa_numero(self):
        return self.__mesa_numero
    
    @mesa_numero.setter
    def mesa_numero(self, mesa_numero: int):
        if isinstance(mesa_numero, int) and mesa_numero > 0:
            self.__mesa_numero = mesa_numero
        else:
            raise ValueError("Número da mesa deve ser um inteiro positivo.")
        
    @property
    def restaurante(self):
        return self.__restaurante
    
    @restaurante.setter
    def restaurante(self, restaurante: str):
        self.__restaurante = restaurante

    @property
    def detalhes(self):
        return self.__detalhes
    
    @detalhes.setter
    def detalhes(self, detalhes: str):
        self.__detalhes = detalhes

    @property
    def data_hora(self):
        return self.__data_hora
    
    @data_hora.setter
    def data_hora(self, data_hora: str):
        self.__data_hora = data_hora

    def atualizar(self, detalhes=None, data_hora=None, status=None):
        if detalhes:
            self.detalhes = detalhes
        if data_hora:
            self.data_hora = data_hora
        if status:
            self.status = status
