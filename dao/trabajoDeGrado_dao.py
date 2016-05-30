from dto.trabajoGrado import TrabajoGrado


class TrabajoGradoDao:
    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()

    def get_trabajo_titulo(self, trabajoG):
        try:
            query = "SELECT * FROM 'trabajo de grado'  WHERE titulo = %s"
            param = (trabajoG.getTitulo(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return trabajoG(codigo=data[0], titulo=data[1], estudiante1=data[3], estudiante2=data[4],
                            estudiante3=data[5], estudiante4=data[6], jurado1=data[7], jurado2=data[8], jurado3=data[9],
                            modalidad=[10], estado=data[13])
        except Exception as e:
            print e.message
            return None

    def consultar_trabajos(self, trabaj):
        if (trabaj.getTitulo() == "" and trabaj.getCodigo() != ""):
            try:
                query = "SELECT * FROM `trabajo de grado` WHERE codigo LIKE %s or codigo LIKE %s or codigo LIKE %s"
                param = (trabaj.getCodigo() + "%", "%" + trabaj.getCodigo() + "%", "%" + trabaj.getCodigo())
                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for trabajo in data:
                    tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1], fecha_correcciones=trabajo[17],
                                       nota=trabajo[19])
                    resultado.append(tra)
                return resultado
            except Exception as e:
                print e.message
                return []

        if (trabaj.getTitulo() != "" and trabaj.getCodigo() == ""):
            return None
        if (trabaj.getTitulo() != "" and trabaj.getCodigo() != ""):
            return None

    def get_trabajo_codigo(self, codigo):
        try:
            query = "SELECT * FROM `trabajo de grado`  WHERE codigo = %s"
            param = (codigo,)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return TrabajoGrado(codigo=data[0], titulo=data[1])
        except Exception as e:
            print e.message
            return None


    def registrar_nota(self,trabajo):
        try:
            query = "UPDATE `trabajo de grado` SET nota= %s WHERE codigo=%s "

            param = (trabajo.getNota(), trabajo.getCodigo())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False

    def agregar_fechas_correcciones(self,trabajo):
        try:
            query = "UPDATE `trabajo de grado` SET fecha_correcciones= %s WHERE codigo=%s "

            param = (trabajo.getFecha_Correcciones(), trabajo.getCodigo())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False
