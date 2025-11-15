from Telas.AbstractTela import AbstractTela
from Telas.TelaPrincipal import TelaPrincipal
from Telas.TelaCliente import TelaCliente
from Telas.TelaFuncionario import TelaFuncionario
from Telas.TelaUsuario import TelaUsuario
from Telas.TelaReserva import TelaReserva
from Telas.TelaRestaurante import TelaRestaurante
from Objetos.Sistema import Sistema
from Controladores.ControladorUsuario import ControladorUsuario
from Controladores.ControladorReserva import ControladorReserva
from Controladores.ControladorCliente import ControladorCliente
from Controladores.ControladorFuncionario import ControladorFuncionario
from Controladores.ControladorRestaurante import ControladorRestaurante
from Controladores.ControladorSistema import ControladorSistema

class ControladorPrincipal:
    def __init__(self):
        self.sistema = Sistema()
        self.tela_principal = TelaPrincipal()
        self.tela_cliente = TelaCliente()
        self.tela_funcionario = TelaFuncionario()
        self.tela_usuario = TelaUsuario()
        self.tela_reserva = TelaReserva()
        self.tela_restaurante = TelaRestaurante()

        self.controlador_usuario = ControladorUsuario(self.sistema, self.tela_usuario)
        self.controlador_reserva = ControladorReserva(self.sistema, self.tela_reserva)
        self.controlador_cliente = ControladorCliente(self.sistema, self.tela_cliente)
        self.controlador_restaurante = ControladorRestaurante(self.sistema, self.tela_restaurante)
        self.controlador_funcionario = ControladorFuncionario(self.sistema, self.tela_funcionario,
                                                             self.controlador_usuario,
                                                             self.controlador_reserva,
                                                             self.controlador_restaurante)
        self.controlador_restaurante = ControladorRestaurante(self.sistema, self.tela_restaurante)
        self.controlador_sistema = ControladorSistema(self.sistema, self)

    def executar(self):
        self.controlador_sistema.executar(self.tela_principal)

    def menu_cliente(self):
        self.controlador_cliente.menu_cliente()

    def menu_funcionario(self):
        self.controlador_funcionario.menu_funcionario()
