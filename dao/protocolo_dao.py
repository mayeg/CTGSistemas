from dto.protocolo import Protocolo


class ProtocoloDao:
    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()



    def get_protocolo_nombre(self, protocolo):
        try:
            query = "SELECT * FROM protocolos WHERE titulo = %s"
            param = (protocolo.getNombre(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            protocolo = Protocolo(nombre=data[1], descripcion=data[2], document0=data[3])
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

    def get_protocolos(self):
        try:
            query = "SELECT * FROM protocolos"
            self.__cur.execute(query)
            data = self.__cur.fetchall()
            print(data)
            resultado = list()
            if data is None:
                return None
            for prot in data:
                protocolo = Protocolo(id=prot[0], nombre=prot[1], descripcion=prot[2],
                                  documento=prot[3])
                resultado.append(protocolo)
            return resultado

        except Exception as e:
            print e.__class__, e.message
            return None
