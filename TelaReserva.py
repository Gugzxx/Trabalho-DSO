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
                 data = input("Data da reserva (DD/MM/AAAA): ")
                 hora = input("Hora da reserva (HH:MM): ")
                 while True:
                     try:
                         qtd_pessoas = int(input("Quantidade de pessoas: "))
                         break
                     except ValueError:
                         print("Digite um número inteiro válido.")
                 while True:
                     try:
                         mesa = int(input("Número da mesa: "))
                         break
                     except ValueError:
                         print("Digite um número inteiro válido.")
                 dados = {
                     "data": data,
                     "hora": hora,
                     "qtd_pessoas": qtd_pessoas,
                     "mesa": mesa
                 }
                 
                 self.__controlador.solicitar_reserva(dados)
                 print("Reserva solicitada com sucesso!")

        elif opcao == "2":
                  id_reserva = input("Informe o ID da reserva a ser confirmada: ")
                  self.__controlador.confirmar_reserva(id_reserva)
                  print("Reserva confirmada com sucesso!")

        elif opcao == "3":
                  id_reserva = input("Informe o ID da reserva a ser cancelada: ")
                  self.__controlador.cancelar_reserva(id_reserva)
                  print("Reserva cancelada com sucesso!")

        elif opcao == "4":
                  id_reserva = input("Informe o ID da reserva a ser consultada: ")
                  self.__controlador.consultar_reserva(id_reserva)
                  print("Consulta realizada com sucesso!")
        
        elif opcao == "5":
                  self.__controlador.lista_reservas()
                  print("Lista exibida com sucesso!")
        
        elif opcao == "0":
                  self.__controlador.finalizar()
        
        else:
            print("Opção inválida!")
