from Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nome: str, telefone: str, email: str):
        super().__init__(nome, telefone, email)
