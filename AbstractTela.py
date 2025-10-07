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

  def mostra_tela_opcoes(self):
    print("-------- Realizar Reserva --------")
    print("1 - Solicitar Reserva")
    print("2 - Confirmar Reserva")
    print("3 - Cancelar Reserva")
    print("4 - Consultar Status da Reserva")
    print("5 - Lista das Reservas")
    print("0 - Finalizar")
    opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 5, 0])
    return opcao
