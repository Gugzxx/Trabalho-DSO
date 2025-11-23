import FreeSimpleGUI as sg
from Telas.abstract_tela import AbstractTela

class TelaReserva(AbstractTela):
    def __init__(self):
        self.__window = None

    def mostrar_reservas(self, reservas):
        if not reservas:
            sg.popup("Nenhuma reserva encontrada.")
        else:
            string_reservas = ""
            for r in reservas:
                string_reservas += f"ID: {r.id} | Cliente: {r.cliente_login}\n"
                string_reservas += f"   Local: {r.restaurante} - Mesa {r.mesa_numero}\n"
                string_reservas += f"   Data: {r.data_hora}\n"
                string_reservas += f"   Status: {r.status}\n"
                string_reservas += "-" * 30 + "\n"
            
            sg.Popup('--- LISTAGEM DE RESERVAS ---', string_reservas)

    def close(self):
        if self.__window:
            self.__window.Close()

    def open(self):
        if self.__window:
            button, values = self.__window.Read()
            return button, values
        return None, None
