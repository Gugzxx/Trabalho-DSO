from Objetos.restaurante import Restaurante
from Objetos.cardapio import Cardapio

class ControladorRestaurante:
    def __init__(self, sistema, tela_restaurante):
        self.sistema = sistema
        self.tela_restaurante = tela_restaurante
    
    def gerenciar_cardapio(self):
        nome_restaurante = self.tela_restaurante.pedir_nome_restaurante()
        if nome_restaurante is None:  # Usuário clicou Cancelar
            return
            
        restaurante = next((r for r in self.sistema.restaurantes if r.nome == nome_restaurante), None)
        if not restaurante:
            self.tela_restaurante.mostrar_mensagem("Restaurante não encontrado.")
            return
            
        if not restaurante.cardapio:
            restaurante.cardapio = Cardapio(restaurante.nome)

        escolha = self.tela_restaurante.mostrar_menu_cardapio(restaurante.nome)
        
        if escolha == 1:  # Adicionar Item
            item = self.tela_restaurante.pedir_nome_item()
            if item is None:  # Usuário clicou Cancelar
                return
                
            restaurante.cardapio.adicionar_item(item)
            self.tela_restaurante.mostrar_mensagem("Item adicionado.")
            # Não precisa chamar adicionar_restaurante novamente, já está na lista
            
        elif escolha == 2:  # Remover Item
            item = self.tela_restaurante.pedir_nome_item()
            if item is None:  # Usuário clicou Cancelar
                return
                
            try:
                restaurante.cardapio.remover_item(item)
                self.tela_restaurante.mostrar_mensagem("Item removido.")
            except ValueError as e:
                self.tela_restaurante.mostrar_mensagem(str(e))
                
        elif escolha == 3:  # Listar Itens
            self.tela_restaurante.mostrar_itens_cardapio(restaurante.cardapio.itens)

    def menu_restaurante(self):
        while True:
            escolha = self.tela_restaurante.mostrar_menu()
            
            if escolha == 1:  # Listar Restaurantes
                self.tela_restaurante.mostrar_restaurantes(self.sistema.restaurantes)
                
            elif escolha == 2:  # Adicionar Restaurante
                dados = self.tela_restaurante.pedir_dados_restaurante()
                if dados is None:  # Usuário clicou Cancelar
                    continue
                    
                nome, endereco = dados
                restaurante = Restaurante(nome, endereco)
                self.sistema.adicionar_restaurante(restaurante)
                self.tela_restaurante.mostrar_mensagem("Restaurante adicionado.")
                
            elif escolha == 3:  # Gerenciar Cardápio
                self.gerenciar_cardapio()
                
            elif escolha == 4:  # Excluir Restaurante (não implementado)
                self.tela_restaurante.mostrar_mensagem("Funcionalidade não implementada.")
                
            elif escolha == 0:  # Voltar
                break
                
            else:
                self.tela_restaurante.mostrar_mensagem("Opção inválida.")
