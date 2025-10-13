from Objetos.Restaurante import Restaurante
from Objetos.Cardapio import Cardapio

class ControladorRestaurante:
    def __init__(self, sistema, tela_restaurante):
        self.sistema = sistema
        self.tela_restaurante = tela_restaurante
    
    
    def gerenciar_cardapio(self):
        nome_restaurante = input("Nome do restaurante: ")
        restaurante = next((r for r in self.sistema.restaurantes if r.nome == nome_restaurante), None)
        if not restaurante:
            print("Restaurante não encontrado.")
            return
        if not restaurante.cardapio:
            restaurante.cardapio = Cardapio(restaurante.nome)
        print("1 - Adicionar item")
        print("2 - Listar itens")
        escolha = input("Escolha: ")
        if escolha == "1":
            item = input("Digite o nome do item: ")
            restaurante.cardapio.adicionar_item(item)
            print("Item adicionado.")
        elif escolha == "2":
            for item in restaurante.cardapio.listar_itens():
                print(item)

    def menu_restaurante(self):
        while True:
            escolha = self.tela_restaurante.mostrar_menu()
            if escolha == "1":
                self.tela_restaurante.mostrar_restaurantes(self.sistema.restaurantes)
            elif escolha == "2":
                nome = input("Nome do restaurante: ")
                endereco = input("Endereço: ")
                restaurante = Restaurante(nome, endereco)
                self.sistema.restaurantes.append(restaurante)
                self.tela_restaurante.mostrar_mensagem("Restaurante adicionado.")
            elif escolha == "3":
                self.gerenciar_cardapio()
            elif escolha == "4":
                self.listar_pagamentos()
            elif escolha == "0":
                break
            else:
                self.tela_restaurante.mostrar_mensagem("Opção inválida.")

    
