

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