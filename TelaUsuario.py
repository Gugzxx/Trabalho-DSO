from Usuario import Usuario

class TelaUsuario:
  def __init__(self, controlador):
    self.__controlador = controlador

  def mostra_tela_opcoes(self):
    while True:
      print("/n=== Menu Usuário ===")
      print("1 - Cadastrar Usuário")
      print("2 - Solicitar Reserva")
      print("3 - Alterar Reseva")
      print("0 - Sair")
      opcao = input("Escolha: ")

      if opcao == "1":
        nome = input("Digite seu nome: ")
        telefone = input("Digite seu telefone (apenas números): ")
        email = input("Digite seu email: ")
        self.__controlador.cadastrar_usuario(nome, telefone, email)
        print("Usuário cadastrado com sucesso!")
    
      elif opcao == "2":
        email = input("Digite seu email: ")
        usuario = self.__controlador.buscar_usuario_por_email(email)
        if not usuario:
          print("Usuário não encontrado.")
        dados_reserva = {}
        dados_reserva["data"] = input("Data da reserva: ")
        dados_reserva["hora"] = input("Hora da reserva: ")
        
        while True:
          try:
            qtd_pessoas = int(input("Quantidade de pessoas: "))
            if qtd_pessoas <= 0:
              print("Digite um número inteiro maior que zero.")
              continue
            break
          except ValueError:
              print("Entrada inválida! Digite somente números inteiros.")
      
          dados_reserva["qtd_pessoas"] = qtd_pessoas
          dados_reserva["mesa"] = input("Número da mesa: ")
          self.__controlador.solicitar_reserva(usuario, dados_reserva)
          print("Reserva feita com sucesso!")
    
      elif opcao == "3":
        email = input("Digite seu email: ")
        usuario = self.__controlador.buscar_usuario_por_email(email)
        if not usuario:
          print("Usuário não encontrado.")
        id_reserva = int(input("ID da reserva a alterar: "))
        novos_dados = {}
        novos_dados["data"] = input("Nova data da reserva: ")
        novos_dados["hora"] = input("Nova hora da reserva: ")
    
        while True:
          try:
            qtd_pessoas = int(input("Nova quantidade de pessoas: "))
            if qtd_pessoas <= 0:
              print("Digite um número inteiro maior que zero.")
              continue
            break
          except ValueError:
              print("Entrada inválida! Digite somente números inteiros.")
          
        novos_dados["qtd_pessoas"] = qtd_pessoas
        novos_dados["mesa"] = input("Novo número da mesa: ")
        self.__controlador.alterar_reserva(usuario, id_reserva, novos_dados)
        print("Reserva alterada com sucesso!")
    
      elif opcao == "0":
            print("Saindo do Menu.")
            break
        
      else:
        print("Opção Inválida.")
