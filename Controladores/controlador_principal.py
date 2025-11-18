from Telas.abstract_tela import AbstractTela
from Telas.tela_principal import TelaPrincipal
from Telas.tela_cliente import TelaCliente
from Telas.tela_funcionario import TelaFuncionario
from Telas.tela_usuario import TelaUsuario
from Telas.tela_reserva import TelaReserva
from Telas.tela_restaurante import TelaRestaurante
from Objetos.sistema import Sistema
from Controladores.controlador_usuario import ControladorUsuario
from Controladores.controlador_reserva import ControladorReserva
from Controladores.controlador_cliente import ControladorCliente
from Controladores.controlador_funcionario import ControladorFuncionario
from Controladores.controlador_restaurante import ControladorRestaurante
from Controladores.controlador_sistema import ControladorSistema

class ControladorPrincipal:
    def __init__(self):
        self.sistema = Sistema()
        self.tela_principal = TelaPrincipal()
        self.tela_cliente = TelaCliente()
        self.tela_funcionario = TelaFuncionario()
        self.tela_usuario = TelaUsuario()
        self.tela_reserva = TelaReserva()
        self.tela_restaurante = TelaRestaurante()

        self.controlador_usuario = ControladorUsuario(self.tela_usuario)
        self.controlador_reserva = ControladorReserva(self.tela_reserva)
        self.controlador_cliente = ControladorCliente(self.sistema, self.tela_cliente)
        self.controlador_restaurante = ControladorRestaurante(self.sistema, self.tela_restaurante)
        self.controlador_funcionario = ControladorFuncionario(self.sistema,
                                                             self.tela_funcionario,
                                                             self.controlador_usuario,
                                                             self.controlador_reserva,
                                                             self.controlador_restaurante,
                                                             self.controlador_cliente)
        self.controlador_sistema = ControladorSistema(self.sistema, self)

    def executar(self):
        self.controlador_sistema.executar(self.tela_principal)

    def menu_cliente(self):
        self.controlador_cliente.menu_cliente()

    def menu_funcionario(self):
        funcionario = self.sistema.logado
        self.controlador_funcionario.menu_funcionario(funcionario)
