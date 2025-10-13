from Objetos.Cardapio import Cardapio

class ControladorFuncionario:
    def __init__(self, sistema, tela_funcionario, controlador_usuario, controlador_reserva, controlador_restaurante):
        self.sistema = sistema
        self.tela_funcionario = tela_funcionario
        self.controlador_usuario = controlador_usuario
        self.controlador_reserva = controlador_reserva
        self.controlador_restaurante = controlador_restaurante

    def menu_funcionario(self):
        funcionario = self.sistema.buscar_funcionario(self.sistema.logado.login)
        while True:
            escolha = self.tela_funcionario.mostrar_menu()
            if escolha == '1':
                self.gerenciar_clientes()
            elif escolha == '2':
                if funcionario.is_admin:
                    self.gerenciar_funcionarios()
                else:
                    self.tela_funcionario.mostrar_mensagem("Acesso negado. Apenas administradores podem gerenciar funcionários.")
            elif escolha == '3':
                self.controlador_reserva.mostrar_todas_reservas()
            elif escolha == '4':
                self.controlador_restaurante.menu_restaurante()
            elif escolha == '5': 
                self.listar_pagamentos()
            elif escolha == '6':
                self.gerenciar_cardapios()
            elif escolha == '0':
                self.sistema.logado = None
                break
            else:
                self.tela_funcionario.mostrar_mensagem("Opção inválida.")

    def gerenciar_clientes(self):
        self.tela_funcionario.mostrar_clientes(self.sistema.clientes)
        opt = input("Deseja adicionar (a) ou remover (r) cliente? (0 para voltar): ")
        if opt.lower() == 'a':
            self.controlador_usuario.criar_cliente()
        elif opt.lower() == 'r':
            login = input("Login do cliente a remover: ")
            cliente = self.sistema.buscar_cliente(login)
            if cliente:
                self.sistema.clientes.remove(cliente)
                usu = self.sistema.buscar_usuario(login)
                if usu:
                    self.sistema.usuarios.remove(usu)
                self.tela_funcionario.mostrar_mensagem("Cliente removido.")
            else:
                self.tela_funcionario.mostrar_mensagem("Cliente não encontrado.")

    def gerenciar_funcionarios(self):
        self.tela_funcionario.mostrar_funcionarios(self.sistema.funcionarios)
        opt = input("Deseja adicionar (a) ou remover (r) funcionário? (0 para voltar): ")
        if opt.lower() == 'a':
            self.controlador_usuario.criar_funcionario()
        elif opt.lower() == 'r':
            login = input("Login do funcionário a remover: ")
            func = self.sistema.buscar_funcionario(login)
            if func:
                self.sistema.funcionarios.remove(func)
                usu = self.sistema.buscar_usuario(login)
                if usu:
                    self.sistema.usuarios.remove(usu)
                self.tela_funcionario.mostrar_mensagem("Funcionário removido.")
            else:
                self.tela_funcionario.mostrar_mensagem("Funcionário não encontrado.")

    def listar_pagamentos(self):
        print("Pagamentos realizados/pedências:")
        if hasattr(self.sistema, "pagamentos"):
            for p in self.sistema.pagamentos:
                print(f"Reserva ID: {p.reserva_id} | Valor: {p.valor} | Método: {p.metodo} | Status: {p.status}")
        else:
            print("Nenhum pagamento registrado ainda.")
    
    def gerenciar_cardapios(self):
        nome_restaurante = input("Nome do restaurante: ")
        restaurante = next((r for r in self.sistema.restaurantes if r.nome == nome_restaurante), None)
        if not restaurante:
            print("Restaurante não encontrado.")
            return
        if not restaurante.cardapio:
            restaurante.cardapio = Cardapio(restaurante.nome)
        print("1 - Adicionar item")
        print("2 - Remover item")
        print("3 - Listar itens")
        escolha = input("Escolha: ")
        if escolha == "1":
            item = input("Digite o nome do item: ")
            restaurante.cardapio.adicionar_item(item)
            print("Item adicionado.")
        elif escolha == "2":
            item = input("Digite o nome do item a remover: ")
            if item not in restaurante.cardapio.listar_itens():
                print("Item não encontrado no cardápio.")
            else:
                restaurante.cardapio.remover_item(item)
                print("Item removido.")
        elif escolha == "3":
            for item in restaurante.cardapio.listar_itens():
                print(item)
        
