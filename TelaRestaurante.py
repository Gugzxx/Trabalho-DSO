from ControladorRestaurante import ControladorReestaurante
from Restaurante import Restaurante

class TelaRestaurante:
  def __init__(self, controlador):
    self.__controlador = controlador

  def mostrs_tela_opcoes(self):
    while True:
      print("/n=== Menu Restaurante ===")
      print("1 - Incluir Mesa")
      print("2 - Excluir Mesa")
      print("3 - Listar Mesas")
      print("0 - Sair")
      opcao = input("Escolha: ")

      if opcao == "1":
        numero = int(input("Número da mesa: ")
        qtd_lugares = int(input("Quantidade de lugares: ")
        self.__controlador.incluir_mesa(numero, qtd_lugares)
        print("Mesa incluída com suceesso!")

      elif opcao == "2":
        numero = int(input("Número da mesa: ")
        if self.__controlador.excluir_mesa(numero):
          print("Mesa exclúida com sucesso!")
        else:
          print("Mesa não encontrada!")
          
      elif opcao == "3":
        mesas = self.__controlador.listar_mesas()
        print
                       
