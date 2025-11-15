from abc import ABC

class AbstractTela(ABC):
    def mostrar_mensagem(self, mensagem):
        print(mensagem)
