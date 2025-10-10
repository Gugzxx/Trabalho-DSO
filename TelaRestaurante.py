from AbstractTela import AbstractTela
from Restaurante import Restaurante

class TelaRestaurante:
  def __init__(self, controlador):
    self.__controlador = controlador

  def mostra_tela_opcoes(self):
    while True:
      print("/n=== Menu Restaurante ===")
      print("1 - Incluir Mesa")
      print("2 - Excluir Mesa")
      print("3 - Listar Mesas")
      print("0 - Sair")
      opcao = input("Escolha: ")

      if opcao == "1":
        while True:
          try:
            numero = int(input("Número da mesa: "))
            break
          except ValueError:
            print("Digite um número inteiro válido.")
        while True:
          try:
            qtd_lugares = int(input("Quantidade de lugares: "))
            break
          except ValueError:
            print("Digite um número inteiro válido.")
        self.__controlador.incluir_mesa(numero, qtd_lugares)
        print("Mesa incluída com suceesso!")

      elif opcao == "2":
        while True:
          try:
              numero = int(input("Número da mesa a excluir: "))
              break
          except ValueError:
              print("Digite um número inteiro válido.")
        if self.__controlador.excluir_mesa(numero):
          print("Mesa exclúida com sucesso!")
        else:
          print("Mesa não encontrada!")
          
      elif opcao == "3":
        mesas = self.__controlador.listar_mesas()
        print("Mesas cadasttradas: ")
        for mesa in mesas:
          print(f"Mesa {mesa.numero} - Lugares: {mesa.qtd_lugares}")

      elif opcao == "0":
        print("Saindo do Menu.")
        break
     
      else:
        print("Opção Inválida.")
