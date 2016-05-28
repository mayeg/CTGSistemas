from dto.acta import Acta


class ActaDao:
    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()

    def get_acta_titulo(self, acta):
        try:
            query = "SELECT * FROM acta WHERE titulo = %s"
            param = (acta.getTitulo(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return Acta(codigo=data[0], titulo=data[1], tipo=data[2],
                        fecha=data[3],
                        archivo=data[4], descripcion=data[5])
        except Exception as e:
            print e.message
            return None

    def crear_acta(self, acta):
        try:
            query = "INSERT INTO acta (titulo, tipo, fecha, " \
                    "documento, Descripcion) VALUES ( %s, %s, %s, %s, %s)"

            param = (acta.getTitulo(), acta.getTipo(), acta.getFecha(),
                     acta.getArchivo(), acta.getDescripcion())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False

    def modificar_acta(self, titulo_acta, acta):
        try:
            query = "UPDATE acta SET codigo= %s, titulo= %s, tipo= %s," \
                    "fecha= %s, documento= %s, Descripcion = %s WHERE titulo=%s "

            param = (
            acta.getCodigo(), acta.getTitulo(), acta.getTipo(), acta.getFecha(),
            acta.getArchivo(), acta.getDescripcion(), titulo_acta)
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False

    def get_acta_consulta(self, acta):

        # SOLO FECHA
        if (
                    acta.getTitulo() == "" and acta.getTipo() == "<-- No Selected -->" and acta.getFecha() != ""):
            try:
                query = "SELECT * FROM acta WHERE fecha = %s"
                param = (acta.getFecha(),)
                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for acta in data:
                    act = Acta(codigo=acta[0], titulo=acta[1], tipo=acta[2],
                               fecha=acta[3], archivo=acta[4],
                               descripcion=acta[5])
                    resultado.append(act)
                return resultado
            except Exception as e:
                print e.message
                return []

        # SOLO TITULO
        elif (
                    acta.getTitulo() != "" and acta.getTipo() == "<-- No Selected -->" and acta.getFecha() == ""):

            try:
                query = "SELECT * FROM acta WHERE titulo = %s"
                param = (acta.getTitulo(),)
                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for acta in data:
                    act = Acta(codigo=acta[0], titulo=acta[1], tipo=acta[2],
                               fecha=acta[3], archivo=acta[4],
                               descripcion=acta[5])
                    resultado.append(act)
                return resultado
            except Exception as e:
                print e.message
                return []

        elif (
                    acta.getTitulo() == "" and acta.getTipo() != "" and acta.getFecha() == ""):
            return None
        elif (
                    acta.getTitulo() == "" and acta.getTipo() != "" and acta.getFecha() != ""):
            return None

        elif (
                    acta.getTitulo() != "" and acta.getTipo() == "" and acta.getFecha() != ""):
            return None
        elif (
                    acta.getTitulo() != "" and acta.getTipo() != "" and acta.getFecha() == ""):
            return None
        elif (
                    acta.getTitulo() != "" and acta.getTipo() != "" and acta.getFecha() != ""):
            return None
