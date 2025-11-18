from Objetos.restaurante import Restaurante
from Objetos.cardapio import Cardapio

class ControladorRestaurante:
    def __init__(self, sistema, tela_restaurante):
        self.sistema = sistema
        self.tela_restaurante = tela_restaurante
    
    
    def gerenciar_cardapio(self):
        nome_restaurante = self.tela_restaurante.pedir_nome_restaurante()
        restaurante = next((r for r in self.sistema.restaurantes if r.nome == nome_restaurante), None)
        if not restaurante:
            self.tela_restaurante.mostrar_mensagem("Restaurante não encontrado.")
            return
        if not restaurante.cardapio:
            restaurante.cardapio = Cardapio(restaurante.nome)

        escolha = self.tela_restaurante.mostrar_menu_cardapio(restaurante.nome)
        if escolha == "1":
            item = self.tela_restaurante.pedir_nome_item()
            restaurante.cardapio.adicionar_item(item)
            self.tela_restaurante.mostrar_mensagem("Item adicionado.")
        elif escolha == "2":
            item = self.tela_restaurante.pedir_nome_item()
            try:
                restaurante.cardapio.remover_item(item)
                self.tela_restaurante.mostrar_mensagem("Item removido.")
            except ValueError as e:
                self.tela_restaurante.mostrar_mensagem(str(e))
        elif escolha == "3":
            itens = restaurante.cardapio.listar_itens() if restaurante.cardapio else []
            self.tela_restaurante.mostrar_itens_cardapio(itens)

    def menu_restaurante(self):
        while True:
            escolha = self.tela_restaurante.mostrar_menu()
            if escolha == "1":
                self.tela_restaurante.mostrar_restaurantes(self.sistema.restaurantes)
            elif escolha == "2":
                nome, endereco = self.tela_restaurante.pedir_dados_restaurante()
                restaurante = Restaurante(nome, endereco)
                self.sistema.restaurantes.append(restaurante)
                self.tela_restaurante.mostrar_mensagem("Restaurante adicionado.")
            elif escolha == "3":
                self.gerenciar_cardapio()
            elif escolha == "4":
                self.tela_restaurante.mostrar_mensagem("Funcionalidade não implementada.")
            elif escolha == "0":
                break
            else:
                self.tela_restaurante.mostrar_mensagem("Opção inválida.")   
