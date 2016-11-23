from dto.propuesta import Propuesta
from dto.usuario import Usuario
from dto.usuario_propuesta import UsuarioPropuesta


class Propuesta_UsuarioDao:

    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()

    def get_propuesta_usuario(self, usuarioP):
        try:
            query = "SELECT * FROM usuario_propuesta " \
                    "JOIN usuario ON usuario.id = usuario_propuesta.id_estudiante " \
                    "WHERE id_estudiante = %s "
            param = (usuarioP.getId_estudiante().getId(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            user = UsuarioPropuesta(id_estudiante=data[1], id_propuesta=data[2],
                                    estado=data[3])
            estudiante = Usuario(codigo=data[4], nombres=data[8], apellidos=data[9],
                                 email=data[10])
            user.setId_estudiante(estudiante)
            return user
        except Exception as e:
            print e.__class__, e.message
            return None

    def get_propuesta_codigo(self, usuarioP):
        try:
            query = "SELECT * FROM usuario_propuesta " \
                    "JOIN propuesta ON propuesta.id = usuario_propuesta.id_propuesta " \
                    "WHERE id_propuesta = %s "
            param = (usuarioP.getId_propuesta().getId(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            user = UsuarioPropuesta(id=data[0], id_estudiante=data[1],
                                    id_propuesta=data[2], estado=data[3])
            propuesta = Propuesta(id=user.getId_propuesta().getId(), titulo=data[5],
                                  director_trabajo=data[6], documentacion=data[11],
                                  modalidad=data[12], fecha_correcciones=data[17],
                                  fecha=data[18])
            user.setId_propuesta(propuesta)
            return user
        except Exception as e:
            print e.__class__, e.message
            return None

    def crear_propuesta_usuario(self, propuest, id):
        try:
            query = "INSERT INTO usuario_propuesta " \
                    "(id_estudiante, id_propuesta, estado) " \
                    "VALUES (%s, %s, %s)"
            param = (id, propuest.getId(), "Activa")
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False
