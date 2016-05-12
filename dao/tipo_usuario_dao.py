# -*- coding: utf-8 -*-
from dto.tipo_usuario import TipoUsuario


class TipoUsuarioDao:

    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()

    def listar_tipo_usuario(self):
        try:
            query = "SELECT * FROM tipo_usuario "
            self.__cur.execute(query)
            data = self.__cur.fetchall()
            if data is None:
                return []
            tipos = list()
            for tipo in data:
                tipo_u = TipoUsuario(id=tipo[0], nombre=tipo[1], label=tipo[2])
                tipos.append(tipo_u)
            return tipos
        except Exception as e:
            print e.message
            return []
