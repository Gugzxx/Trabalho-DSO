class ClienteInexistenteException(Exception):
    def __init__(self):
        super().__init__("O cliente informado não existe no sistema.")
