from dto.protocolo import Protocolo


class ProtocoloDao:
    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()



    def get_protocolo_nombre(self, protocolo):
        try:
            query = "SELECT * FROM protocolo WHERE titulo = %s"
            param = (protocolo.getNombre(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            protocolo = Protocolo(nombre=data[0], descripcion=data[1], filename=data[8])
            return protocolo

        except Exception as e:
            print e.__class__, e.message
            return None


    def crear_protocolo(self, protocolo):
        try:
            query = "INSERT INTO protocolos (nombre, descripcion, " \
                    "documento) VALUES (%s, %s, %s)"
            param = (protocolo.getNombre(), protocolo.getDescripcion(),
                     protocolo.getFilename())

            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__, e.message
            return False
