from DAOs.dao import DAO
from Objetos.reserva import Reserva

class ReservaDAO(DAO):
    def __init__(self):
        super().__init__('reservas.pkl')

    def add(self, reserva: Reserva):
        if (isinstance(reserva.id, int)) and (reserva is not None) and isinstance(reserva, Reserva):
            super().add(reserva.id, reserva)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
