from AbstractTela import AbstractTela

class TelaReserva:
  def __init__(self, controlador):
    self.__controlador = controlador
    
  #def solicita_id_reserva(self):
    #return self.le_num_inteiro(input("Informe o ID da reserva: "))
   
  def mostra_tela_opcoes(self):
      while True:
        print("-------- Realizar Reserva --------")
        print("1 - Solicitar Reserva")
        print("2 - Confirmar Reserva")
        print("3 - Cancelar Reserva")
        print("4 - Consultar Status da Reserva")
        print("5 - Lista das Reservas")
        print("0 - Finalizar")
        opcao = input("Escolha uma opção: ")
        
      
        if opcao == "1":
                 self.__controlador.solicitar_reserva()
                 print("Reserva solicitada com sucesso!")

        elif opcao == "2":
                  self.__controlador.confirmar_reserva()
                  print("Reserva confirmada com sucesso!")

        elif opcao == "3":
                  self.__controlador.cancelar_reserva()
                  print("Reserva cancelada com sucesso!")

        elif opcao == "4":
                  self.__controlador.consultar_reserva()
                  print("Consulta realizada com sucesso!")
        
        elif opcao == "5":
                  self.__controlador.lista_reservas()
                  print("Lista exibida com sucesso!")
        
        elif opcao == "0":
                  self.__controlador.finalizar()
        
        else:
            print("Opção inválida!")
