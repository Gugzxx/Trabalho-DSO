from DAOs.dao import DAO
from Objetos.cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        if (isinstance(cliente.login, str)) and (cliente is not None) and isinstance(cliente, Cliente):
            super().add(cliente.login, cliente)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
