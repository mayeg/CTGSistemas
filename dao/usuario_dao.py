# -*- coding: utf-8 -*-
from dto.tipo_usuario import TipoUsuario
from dto.usuario import Usuario


class UsuarioDao:

    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()

    def get_user_login(self, usuario):
        try:
            query = "SELECT * FROM usuario WHERE codigo=%s AND contraseña=%s"
            param = (usuario.getCodigo(), usuario.getContrasena())
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return Usuario(id=data[0], nombres=data[4], codigo=data[1],
                           contrasena=data[3], tipo_usuario=data[7])
        except Exception as e:
            print e.message
            return None

    def get_lista_usuarios(self, pagina, codigo, nombres, cedula, apellidos,
                           tipoU):
        try:
            limit = 10
            offset = (pagina - 1) * limit
            query = "SELECT * FROM usuario " \
                    "JOIN tipo_usuario ON tipo_usuario.id = usuario.tipo_usuario " \
                    "WHERE tipo_usuario = %s AND codigo LIKE %s AND nombres " \
                    "LIKE %s AND cedula LIKE %s AND apellidos LIKE %s LIMIT %s " \
                    "OFFSET %s"
            param = (4, "%"+codigo+"%", "%"+nombres+"%", "%"+cedula+"%",
                     "%"+apellidos+"%", limit, offset)
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for usuario in data:
                user = Usuario(id=usuario[0], codigo=usuario[1], cedula=usuario[2],
                               contrasena=usuario[3], nombres=usuario[4],
                               apellidos=usuario[5], email=usuario[6])
                tipo_usuario = TipoUsuario(
                    id=usuario[8], label=usuario[10], nombre=usuario[9])
                user.setTipoUsuario(tipo_usuario)
                resultado.append(user)
            return resultado
        except Exception as e:
            print e.message
            return []

    def listar_jurados(self, usuario):
        try:
            query= "SELECT * FROM usuario WHERE tipo_usuario=%s"
            param = (int(usuario.getTipoUsuario().getId()),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for jurado in data:
                user = Usuario(id=jurado[0], codigo=jurado[1], cedula=jurado[2],
                               contrasena=jurado[3], nombres=jurado[4],
                               apellidos=jurado[5], email=jurado[6])

                tipo_usuario = TipoUsuario(id=jurado[8], label=jurado[10],
                                       nombre=jurado[9])
                user.setTipoUsuario(tipo_usuario)
                resultado.append(user)

            return resultado

        except Exception as e:
            print e.message
            return []


    def get_total_usuarios(self, pagina, codigo, nombres, cedula, apellidos):
        try:
            query = "SELECT Count(*) FROM usuario WHERE codigo LIKE %s AND"  \
                    "nombres LIKE %s AND cedula LIKE %s AND apellidos LIKE %s"
            param = ("%"+codigo+"%", "%"+nombres+"%", "%"+cedula+"%"
                     , "%"+apellidos+"%")
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            print data[0]
            if data is None:
                return 0
            return data[0]
        except Exception as e:
            print e.message
            return 0

    def get_usuario_por_codigo(self, usuario):
        try:
            print usuario.getCodigo(), 'codigo dao'
            query = "SELECT * FROM usuario WHERE codigo = %s"
            param = (str(usuario.getCodigo()),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            print data
            if data is None:
                return None
            return Usuario(id=data[0], codigo=data[1], cedula=data[2],
                           nombres=data[4], apellidos=data[5], email=data[6],
                           token_password=data[8], tipo_usuario=data[7])
        except Exception as e:
            print e.message
            return None

    def crear_usuario(self, usuario):
        try:
            query = "INSERT INTO usuario (codigo, nombres, apellidos, cedula, " \
                    "email, contraseña, tipo_usuario) VALUES (%s, %s, %s, %s, %s" \
                    ", %s, %s)"
            param = (usuario.getCodigo(), usuario.getNombres(),
                     usuario.getApellidos(), str(usuario.getCedula()),
                     usuario.getEmail(), usuario.getContrasena(),
                     int(usuario.getTipoUsuario().getId()))
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False

    def get_usuario_por_tipo(self, usuario_tipo):
        try:
            print "en el dao"+ usuario_tipo.getTipoUsuario().getId()
            query = "SELECT * FROM usuario WHERE tipo_usuario = %s"
            param = (int(usuario_tipo.getTipoUsuario().getId()),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            print data, "data dao"
            if data is None:
                return None
            return Usuario(id=data[0], cedula=data[2], contrasena=data[3],
                           nombres=data[4], apellidos=data[5],
                           tipo_usuario=data[7])
        except Exception as e:
            print e.message, "execpcion"
            return None

    def get_usuario_por_id(self, usuario):
        try:
            query = "SELECT * FROM usuario WHERE id = %s"
            param = (usuario.getId(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return Usuario(id=data[0], cedula=data[2], contrasena=data[3],
                           nombres=data[4], apellidos=data[5], email=data[6],
                           tipo_usuario=data[7])
        except Exception as e:
            print e.message
            return None

    def get_usuario_por_token(self, usuario):
        try:
            query = "SELECT * FROM usuario WHERE token_password = %s"
            param = (usuario.getTokenPassword(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return Usuario(id=data[0], cedula=data[2], contrasena=data[3],
                           nombres=data[4], apellidos=data[5], email=data[6],
                           tipo_usuario=data[7])
        except Exception as e:
            print e.message
            return None

    def eliminar_usuario(self, usuario):
        try:
            query = "DELETE FROM usuario WHERE id = %s"
            param = (usuario.getId(),)
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.message
            return False

    def editar_usuario(self, usuario):
        try:
            query = "UPDATE usuario SET nombres= %s, apellidos= %s, cedula= %s," \
                    "email= %s, tipo_usuario= %s, token_password= %s WHERE id=%s "
            param = (usuario.getNombres(), usuario.getApellidos(),
                     usuario.getCedula(), usuario.getEmail(),
                     int(usuario.getTipoUsuario().getId()),
                     usuario.getTokenPassword(), int(usuario.getId()))
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__, e.message
            return False

    def cambiar_contrasena(self, usuario, contrasena_n):
        try:
            query = "UPDATE usuario SET contraseña = %s WHERE id=%s"
            param = (contrasena_n, usuario.getId())
            print contrasena_n, usuario.getId()
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            return False

    def cambiar_recordar_contrasena(self, usuario):
        try:
            query = "UPDATE usuario SET contraseña = %s, token_password= %s " \
                    "WHERE id=%s"
            param = (usuario.getContrasena(), usuario.getTokenPassword(),
                     usuario.getId())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            return False
    
    def get_jurados(self, usuario_tipo):
        try:
            query = "SELECT * FROM usuario WHERE tipo_usuario = %s"
            param = (usuario_tipo,)
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for usuario in data:
                user = Usuario(id=usuario[0], codigo=usuario[1], cedula=usuario[2],
                               contrasena=usuario[3], nombres=usuario[4],
                               apellidos=usuario[5], email=usuario[6])
                resultado.append(user)
            return resultado
        except Exception as e:
            print e.message
            return []        
