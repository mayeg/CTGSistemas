from dto.propuesta import Propuesta


class PropuestaDao:
    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()

#CODIGO = ID
    def get_propuesta_codigo(self,propuesta):
        try:
            query = "SELECT * FROM propuesta WHERE id = %s"
            param = (propuesta.getCodigo(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return Propuesta(codigo=data[0], titulo=data[1], director_propuesta=data[2], cod_estudiante1=data[3],
                             cod_estudiante2=data[4],cod_estudiante3=data[5],cod_estudiante4=data[6],
                             cod_jurado1=data[7],cod_jurado2=data[8],cod_jurado3=data[9],comentario=data[10],
                             entegrables=data[11],estado=data[12],documentacion=data[13],modalidad=data[14],
                             solicitud_retiro=data[15],solicitud_sustentacion=data[16],solicitud_prorroga=data[17],
                             fecha_comentario=data[18],fecha_correcciones=data[19],fecha_entregables=data[20],
                             fecha=data[21])
        except Exception as e:
            print e.message
            return None

    def get_propuesta_consulta(self,propuest):
        if(propuest.getCodigo() == "" and propuest.getTitulo() != ""):
            try:
                query = "SELECT * FROM propuesta WHERE titulo LIKE %s or titulo LIKE %s or titulo LIKE %s"
                param = (propuest.getTitulo()+"%","%"+propuest.getTitulo()+"%","%"+propuest.getTitulo())
                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for propuesta in data:
                    pro = Propuesta(codigo=propuesta[0], titulo=propuesta[1], director_propuesta=propuesta[2], cod_estudiante1=propuesta[3],
                             cod_estudiante2=propuesta[4],cod_estudiante3=propuesta[5],cod_estudiante4=propuesta[6],
                             cod_jurado1=propuesta[7],cod_jurado2=propuesta[8],cod_jurado3=propuesta[9],comentario=propuesta[10],
                             entegrables=propuesta[11],estado=propuesta[12],documentacion=propuesta[13],modalidad=propuesta[14],
                             solicitud_retiro=propuesta[15],solicitud_sustentacion=propuesta[16],solicitud_prorroga=propuesta[17],
                             fecha_comentario=propuesta[18],fecha_correcciones=propuesta[19],fecha_entregables=propuesta[20],
                             fecha=propuesta[21])
                    resultado.append(pro)
                return resultado
            except Exception as e:
                print e.message
                return []
        elif(propuest.getCodigo != "" and propuest.getTitulo() == ""):
            return None
        elif(propuest.getCodigo() != "" and propuest.getTitulo() != ""):
            return None



    def modificar_estado(self,propuesta):
        try:
            query = "UPDATE propuesta SET estado= %s WHERE id=%s "

            param = (propuesta.getEstado(),propuesta.getCodigo())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False


    def modificar_fechas(self,propuesta):
        if(propuesta.getFecha_Comentario() == None and propuesta.getFecha_Correcciones() != ""):
            return None
        elif(propuesta.getFecha_Comentario() != "" and propuesta.getFecha_Correcciones() == None):
            try:
                print "entro a la correcta"
                query = "UPDATE propuesta SET fecha_comentario= %s WHERE id=%s "

                param = (propuesta.getFecha_Comentario(), propuesta.getCodigo())
                self.__cur.execute(query, param)
                self.__conn.commit()
                return True
            except Exception as e:
                print e.__class__
                print e.message
                return False

        elif(propuesta.getFecha_Comentario() != "" and propuesta.getFecha_Correcciones() != ""):
            return None


    def habilitar_envio_entregables(self,propuesta):
        try:
            query = "UPDATE propuesta SET entregables= %s WHERE id=%s "

            param = (propuesta.getEntregables(), propuesta.getCodigo())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False