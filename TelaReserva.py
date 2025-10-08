from AbstractTela import AbstractTela

class TelaReserva:
  def __init__(self, controlador):
    self.__controlador = controlador
  def solicita_id_reserva(self):
    return self.le_num_inteiro("Informe o ID da reserva: ")
   
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
