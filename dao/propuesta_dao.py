from dto.propuesta import Propuesta


class PropuestaDao:
    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()


    def get_propuesta_consulta(self,propuest):
        if(propuest.getCodigo() == "" and propuest.getTitulo() != ""):
            print "entro a solo titulo"
            try:
                query = "SELECT * FROM propuesta WHERE titulo = %s"
                param = (propuest.getTitulo(),)
                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for propuesta in data:
                    pro = Propuesta(codigo=propuesta[0], titulo=propuesta[1], director_trabajo=propuesta[2], cod_estudiante1=propuesta[3], codigo_estudiante2=propuesta[4],
                               codigo_estudiante3=propuesta[5],codigo_estudiante4=propuesta[1],cod_jurado1=propuesta[1],cod_jurado2=propuesta[1],cod_jurado3=propuesta[1],
                                    comentario=propuesta[1],entregables=propuesta[1],estado=propuesta[1],documentacion=propuesta[1],modalidad=propuesta[1],solicitud_retiro=propuesta[1],
                                    solicitud_sustentacion=propuesta[1],solicitud_prorroga=propuesta[1],fecha_comentario=propuesta[1],fecha_entregables=propuesta[1],fecha=propuesta[1],)
                    resultado.append(pro)
                return resultado
            except Exception as e:
                print e.message
                return []
        elif(propuest.getCodigo != "" and propuest.getTitulo() == ""):
            return None
        elif(propuest.getCodigo() != "" and propuest.getTitulo() != ""):
            return None