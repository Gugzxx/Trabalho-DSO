from Usuario import Usuario

class Funcionario(Usuario):
    def __init__(self, nome: str, telefone: str, email: str, cargo: str):
        super().__init__(nome, telefone, email)
        self.__cargo = cargo

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: str):
        if isinstance(cargo, str) and len(cargo) > 0:
            self.__cargo = cargo
