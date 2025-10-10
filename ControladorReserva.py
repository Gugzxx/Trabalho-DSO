from TelaReserva import TelaReserva

class ControladorReserva:
    def __init__(self):
        self.__tela_reserva = TelaReserva(self)
        self.__reservas = []
        self.__id_reserva = 1

    def inicia(self):
      self.abre_tela_inicial()

    def solicitar_reserva(self, cliente=None, dados=None):
            
        if dados is None:
             dados = self.__tela_reserva.solicitar_reserva()

        if not dados:
                return None

        reserva = {
            "id": self.__id_reserva,
            "data": dados.get("data"),
            "hora": dados.get("hora"),
            "qtd_pessoas": dados.get("qtd_pessoas"),
            "mesa": dados.get("mesa"),
            "status": "pendente",
            "cliente": cliente,
            }
        self.__reservas.append(reserva)
        self.__id_reserva += 1
        print("Reserva criada com sucesso! ID:", reserva["id"])
        return reserva

    def confirmar_reserva(self):
            id_reserva = self.__tela_reserva.solicita_id_reserva()
            for reserva in self.__reservas:
                if reserva["id"] == id_reserva:
                    reserva["status"] = "confirmada"
                    print("Reserva confirmada!")
                    return
            print("Reserva não encontrada.")

    def cancelar_reserva(self):
            id_reserva = self.__tela_reserva.solicita_id_reserva()
            for reserva in self.__reservas:
                if reserva["id"] == id_reserva:
                    reserva["status"] = "cancelada"
                    print("Reserva cancelada!")
                    return
            print("Reserva não encontrada.")

    def consultar_reserva(self):
            id_reserva = self.__tela_reserva.solicita_id_reserva()
            for reserva in self.__reservas:
                if reserva["id"] == id_reserva:
                    print("Dados da reserva:", reserva)
                    return

    def lista_reservas(self):
            if not self.__reservas:
                print("Nenhuma reserva cadastrada.")
            else:
                for reserva in self.__reservas:
                    print(reserva)

    def finalizar(self):
            print("Saindo do sistema...")
            exit(0)

    def abre_tela_inicial(self):
            switcher = {0: self.finalizar, 1: self.solicitar_reserva, 2: self.confirmar_reserva, 3: self.cancelar_reserva, 4: self.consultar_reserva, 5: self.lista_reservas}

            while True:
                try:
                    opcao = self.__tela_reserva.mostra_tela_opcoes()
                    funcao_escolhida = switcher.get(opcao, self.finalizar)
                    funcao_escolhida()
                except (ValueError, KeyError):
                    print("Opção inválida!")
