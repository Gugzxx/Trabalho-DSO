class AbstractTela:
  def __init__(self, controlador):
    self.__controlador = controlador

  def le_num_inteiro(self, mensagem: str = '', inteiros_validos: [] = None):
    while True:
      valor_lido = input(mensagem)
      try:
          inteiro = int(valor_lido)
          if inteiros_validos and inteiro not in inteiros_validos:
              raise ValueError
          return inteiro
      except ValueError:
          print("Valor incorreto: Digite um numero inteiro valido")
          if inteiros_validos:
            print("Valores validos: ", inteiros_validos)
