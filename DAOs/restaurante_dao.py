from DAOs.dao import DAO
from Objetos.restaurante import Restaurante

class RestauranteDAO(DAO):
    def __init__(self):
        super().__init__('restaurantes.pkl')

    def add(self, restaurante: Restaurante):
        if (isinstance(restaurante.nome, str)) and (restaurante is not None) and isinstance(restaurante, Restaurante):
            super().add(restaurante.nome, restaurante)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
