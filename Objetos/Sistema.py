from Objetos.Usuario import Cliente, Funcionario, Usuario
from Objetos.Reserva import Reserva
from Objetos.Restaurante import Restaurante

class Sistema:
    def __init__(self):
        self.usuarios = []
        self.clientes = []
        self.funcionarios = []
        self.reservas = []
        self.restaurantes = []
        self.pagamentos = []
        self.logado = None
        admin = Funcionario("admin", "admin123", "Administrador", "admin@example.com", True)
        self.funcionarios.append(admin)
        self.usuarios.append(admin)

    def autenticar(self, login, senha, tipo):
        for u in self.usuarios:
            if u.login == login and u.senha == senha and u.tipo == tipo:
                self.logado = u
                return True
        return False

    def buscar_usuario(self, login):
        for u in self.usuarios:
            if u.login == login:
                return u
        return None

    def cadastrar_cliente(self, login, senha, nome, email):
        if self.buscar_usuario(login):
            return False
        cliente = Cliente(login, senha, nome, email)
        self.clientes.append(cliente)
        self.usuarios.append(cliente)
        return True

    def cadastrar_funcionario(self, login, senha, nome, email, is_admin=False):
        if self.buscar_usuario(login):
            return False
        funcionario = Funcionario(login, senha, nome, email, is_admin)
        self.funcionarios.append(funcionario)
        self.usuarios.append(funcionario)
        return True

    def buscar_cliente(self, login):
        for c in self.clientes:
            if c.login == login:
                return c
        return None

    def buscar_funcionario(self, login):
        for f in self.funcionarios:
            if f.login == login:
                return f
        return None

    def adicionar_reserva(self, reserva):
        self.reservas.append(reserva)

    def buscar_reserva(self, id_reserva):
        for r in self.reservas:
            if r.id == id_reserva:
                return r
        return None

    def listar_reservas_cliente(self, cliente_login):
        return [r for r in self.reservas if r.cliente_login == cliente_login]

    def listar_todas_reservas(self):
        return self.reservas

    # Métodos adicionais podem ser criados para gerenciar restaurantes, mesas, pagamentos, etc.
