from TelaReserva import TelaReserva
from Reserva import Reserva
from StatusReserva import StatusReserva

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

        nova_reserva = Reserva(
            id_reserva=self.__id_reserva,
            data=dados.get("data"),
            hora=dados.get("hora"),
            qtd_pessoas=dados.get("qtd_pessoas"),
            status=StatusReserva.PENDENTE,
            cliente=cliente,
            mesa=dados.get("mesa"),
            usuario_responsavel=None,
            pagamento=None
        )

        self.__reservas.append(nova_reserva)
        self.__id_reserva += 1
        print("Reserva solicitada com sucesso! ID:", nova_reserva.id_reserva)
        return nova_reserva

    def confirmar_reserva(self):
            id_reserva = self.__tela_reserva.solicita_id_reserva()
            for reserva in self.__reservas:
                if reserva.id_reserva == id_reserva:
                    reserva.status = StatusReserva.CONFIRMADA
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
                    funcao_escolhida()
                except (ValueError, KeyError):
                    print("Opção inválida!")
