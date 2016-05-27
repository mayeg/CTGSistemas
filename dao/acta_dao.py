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
            return Acta(titulo=data[1], tipo=data[2], fecha=data[3],
                           archivo=data[4], descripcion=data[5])
        except Exception as e:
            print e.message
            return None


    def crear_acta(self, acta):
        print "entro a crear acta"
        print acta.getTitulo()
        print acta.getTipo()
        print acta.getFecha()
        print acta.getArchivo()
        print acta.getDescripcion()

        try:
            query = "INSERT INTO ufps35.acta (titulo, tipo, fecha, " \
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



     #def get_acta_consulta(self,acta):
      #   if (acta.getTitulo() == "" and acta.getTipo() == "" and acta.getFecha() != ""):
       #      return None
        # if (acta.getTitulo() == "" and acta.getTipo() != "" and acta.getFecha() == ""):
         #    return None
        # if (acta.getTitulo() == "" and acta.getTipo() != "" and acta.getFecha() != ""):
        #     return None
        # if (acta.getTitulo() != "" and acta.getTipo() == "" and acta.getFecha() == ""):
        #     return None
        # if (acta.getTitulo() != "" and acta.getTipo() == "" and acta.getFecha() != ""):
        #     return None
        # if (acta.getTitulo() != "" and acta.getTipo() != "" and acta.getFecha() == ""):
        #     return None
        # if (acta.getTitulo() != "" and acta.getTipo() != "" and acta.getFecha() != ""):
        #     return None

