from Cliente import Cliente
from Funcionario import Funcionario
from Usuario import Usuario
from Mesa import Mesa
from Pagamento import Pagamento
from StatusReserva import StatusReserva

class ControladorReserva:
  def __init__(self):
    self.__tela_reserva : TelaReserva(self)
    reservas : []

def inicia(self):
  self.abre_tela_inicial()

def solicitar_reserva(self):
  ...

def confirmar_reserva(self):
  ...

def cancelar_reserva(self):
  ...

def consultar_reserva(self):
  ...

def lista_reserva(self):
  ...

def finalizar(self):
  exit(0)

def abre_tela_inicial(self):
  switcher = (0: finalizar, 1: self.solicitar_reserva, 2: self.confirmar_reserva, 3: self.cancelar_reserva, 4: self.consultar_status, 5: self.lista_reservas)

  while True:
    opcao = self.__tela_reserva.mostra_tela_opcoes()
    funcao_escolhida = switcher[opcao]
    funcao_escolhida()
