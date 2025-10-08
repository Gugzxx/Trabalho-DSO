from Usuario import Usuario
from ControladorReserva import ControladorReserva

class ControladorUsuario:
  def __init__(self, controlador_reserva):
    self.__controlador_reserva = controlador_reserva
    self.__usuarios = []

  def cadastrar_usuario(self, nome, telefone, email):
    novo_usuario = Usuario(nome, telefone, email)
    self.__usuarios.append(novo_usuario)
    return novo_usuario

  def solicitar_reserva(self, usuario, dados_reserva):
    return self.__controlador_reserva.solicitar_reserva(usuario, dados_reserva)

  def alterar_reserva(self, usuario, id_reserva, novos_dados):
    return self.__controlador_reserva.alterar_reserva(usuario, id_reserva, novos_dados)

  def buscar_usuario_por_email(self, email):
    for usuario in self.__usuarios:
      if usuario.email == email:
        return usuario
      return None
          
  


