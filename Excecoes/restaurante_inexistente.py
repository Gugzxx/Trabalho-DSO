class RestauranteInexistenteException(Exception):
    def __init__(self):
        super().__init__("O restaurante informado não existe no sistema.")
