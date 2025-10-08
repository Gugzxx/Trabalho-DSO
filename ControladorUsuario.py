from Usuario import Usuario
from ControladorReserva import ControladorReserva

class ControladorUsuario:
  def __init__(self, controlador_reserva):
    self.__controlador_reserva = controlador_reserva
    self.__usuarios = []

  def cadastrar_usuario:
    novo_usuario = Usuario(nome, telefone, email)
    self.__usuarios.append(novo_usuario)
    return novo_usuario

  def listar_usuarios:
    return self.__usuarios

  def anotar_reserva(self, usuario, dados_reserva):
    return self.__controlador_reserva.solicitar_reserva(usuario, dados_reserva)

  def
  


