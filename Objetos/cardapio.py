class Cardapio:
    def __init__(self, restaurante_nome: str):
        self.__restaurante_nome = None
        self.itens = []  

        if isinstance(restaurante_nome, str):
            self.__restaurante_nome = restaurante_nome
    
    @property
    def restaurante_nome(self):
        return self.__restaurante_nome
    
    @restaurante_nome.setter
    def restaurante_nome(self, restaurante_nome):
        self.__restaurante_nome = restaurante_nome
    
    def adicionar_item(self, item):
        self.itens.append(item)
    
    def listar_itens(self):
        return self.itens
    
    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
        else:
            raise ValueError("Item não encontrado no cardápio.")
