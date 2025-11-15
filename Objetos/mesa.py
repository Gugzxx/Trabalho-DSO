class Mesa:
    def __init__(self, numero: int, capacidade: int):
        self.__numero = None
        self.__capacidade = None
        self.ocupada = False

        if isinstance(numero, int) and numero > 0:
            self.__numero = numero
        if isinstance(capacidade, int) and capacidade > 0:
            self.__capacidade = capacidade

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero: int):
        if isinstance(numero, int) and numero > 0:
            self.__numero = numero
        else:
            raise ValueError("Número da mesa deve ser um inteiro positivo.")
        
    @property
    def capacidade(self):
        return self.__capacidade
    
    @capacidade.setter
    def capacidade(self, capacidade: int):
        if isinstance(capacidade, int) and capacidade > 0:
            self.__capacidade = capacidade
        else:
            raise ValueError("Capacidade da mesa deve ser um inteiro positivo.")
