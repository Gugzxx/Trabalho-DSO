from Restaurante import Restaurante
from Mesa import Mesa

class ControladorRestaurante:
  def __init__(self, restaurante):
    self.__restaurante = restaurante
    
  def incluir_mesa(self, numero, qtd_lugares):
    nova_mesa = Mesa(numero, qtd_lugares)
    self.__restaurante.incluir_mesa(nova_mesa)
    return nova_mesa
    
  def excluir_mesa(self, numero):
    for mesa in self.__restaurante.mesas:
      if mesa.numero == numero:
        self.__restaurante.excluir_mesa(mesa)
        return True
    return False
    
  def listar_mesas(self):
    return self.__restaurante.mesas
