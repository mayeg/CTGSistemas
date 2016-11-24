
from dto.propuesta import Propuesta
from dto.usuario import Usuario
from dto.entregable_propuesta import  EntregablePropuesta


class Entregable_propuestaDao:

    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()

    def crear_entregable_propuesta(self, pro):
        try:
            print pro.getId(), 'pro.getid'
            query = " INSERT INTO entregable_propuesta (id_propuesta) VALUES (%s)"
            param = (pro.getId(),)
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__, e.message
            return

    def get_entregable_propuesta(self, pro):
        try:
            query = "SELECT * FROM entregable_propuesta WHERE id_propuesta=%s"
            param = (pro.getId_propuesta().getId(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            entregable = EntregablePropuesta(id=data[0],id_propuesta=data[1],
                                             entregable=data[2],
                                             fecha_entregable=data[3], fecha=data[4])
            return entregable
        except Exception as e:
            print e.__class__, e.message
            return False

    def subir_entregable(self, entregable):
        try:
            query = "UPDATE entregable_propuesta SET entregable=%s , fecha=%s " \
                    "WHERE id=%s"
            param = (entregable.getEntregable(), entregable.getFecha(),
                     entregable.getId())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__, e.message
            return False