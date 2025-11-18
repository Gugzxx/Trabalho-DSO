from Objetos.cliente import Cliente
from Objetos.funcionario import Funcionario
from Objetos.reserva import Reserva
from Objetos.restaurante import Restaurante
from DAOs.cliente_dao import ClienteDAO
from DAOs.funcionario_dao import FuncionarioDAO
from DAOs.restaurante_dao import RestauranteDAO
from DAOs.reserva_dao import ReservaDAO

class Sistema:
    def __init__(self):
        self.__cliente_dao = ClienteDAO()
        self.__funcionario_dao = FuncionarioDAO()
        self.__restaurante_dao = RestauranteDAO()
        self.__reserva_dao = ReservaDAO()
        
        self.pagamentos = [] 
        self.logado = None
        
        if not self.__funcionario_dao.get("admin"):
            admin = Funcionario("admin", "admin", "Administrador", "admin@example.com", True)
            self.__funcionario_dao.add(admin)

    @property
    def clientes(self):
        return self.__cliente_dao.get_all()

    @property
    def funcionarios(self):
        return self.__funcionario_dao.get_all()

    @property
    def restaurantes(self):
        return self.__restaurante_dao.get_all()

    @property
    def reservas(self):
        return self.__reserva_dao.get_all()
    
    @property
    def usuarios(self):
        return self.clientes + self.funcionarios

    def autenticar(self, login, senha, tipo):
        if tipo == "cliente":
            usuario = self.__cliente_dao.get(login)
        elif tipo == "funcionario":
            usuario = self.__funcionario_dao.get(login)
        else:
            return False
            
        if usuario and usuario.senha == senha:
            self.logado = usuario
            return True
        return False

    def buscar_usuario(self, login):
        usuario = self.__funcionario_dao.get(login)
        if usuario:
            return usuario
        return self.__cliente_dao.get(login)

    def cadastrar_cliente(self, login, senha, nome, email):
        if self.buscar_usuario(login):
            return False
        cliente = Cliente(login, senha, nome, email)
        self.__cliente_dao.add(cliente)
        return True

    def cadastrar_funcionario(self, login, senha, nome, email, is_admin=False):
        if self.buscar_usuario(login):
            return False
        funcionario = Funcionario(login, senha, nome, email, is_admin)
        self.__funcionario_dao.add(funcionario)
        return True

    def buscar_cliente(self, login):
        return self.__cliente_dao.get(login)

    def buscar_funcionario(self, login):
        return self.__funcionario_dao.get(login)

    def adicionar_reserva(self, reserva):
        self.__reserva_dao.add(reserva)

    def buscar_reserva(self, id_reserva):
        return self.__reserva_dao.get(id_reserva)

    def listar_reservas_cliente(self, cliente_login):
        todas = self.__reserva_dao.get_all()
        return [r for r in todas if r.cliente_login == cliente_login]

    def listar_todas_reservas(self):
        return self.__reserva_dao.get_all()

    def adicionar_restaurante(self, restaurante):
        self.__restaurante_dao.add(restaurante)
        
    def remover_cliente(self, cliente):
        self.__cliente_dao.remove(cliente.login)
        
    def remover_funcionario(self, funcionario):
        self.__funcionario_dao.remove(funcionario.login)
        
    def atualizar_reserva(self, reserva: Reserva):
        if reserva and isinstance(reserva.id, int):
            self.__reserva_dao.update(reserva.id, reserva)

    def remover_reserva(self, reserva_or_id):
        # aceita tanto o objeto Reserva quanto o id (int)
        if isinstance(reserva_or_id, int):
            self.__reserva_dao.remove(reserva_or_id)
        else:
            try:
                self.__reserva_dao.remove(reserva_or_id.id)
            except Exception:
                return None
