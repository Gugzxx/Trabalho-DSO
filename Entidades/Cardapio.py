class Cardapio:
    def __init__(self, restaurante_nome):
        self.restaurante_nome = restaurante_nome
        self.itens = []  
    
    def adicionar_item(self, item):
        self.itens.append(item)
    
    def listar_itens(self):
        return self.itens
