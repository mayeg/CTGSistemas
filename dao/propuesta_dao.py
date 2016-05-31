from dto.propuesta import Propuesta


class PropuestaDao:
    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()


    def crear_propuesta(self, propuesta):
        try:
            query = "INSERT INTO propuesta (titulo, director_trabajo, " \
                    "documentacion, modalidad, fecha) VALUES (%s, %s, %s, %s," \
                    " %s)"
            param = (propuesta.getTitulo(), propuesta.getDirector_trabajo(),
                     propuesta.getDocumentacion(), propuesta.getModalidad(),
                     str(propuesta.getFecha()))

            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__, e.message
            return False

    def get_propuesta_titulo(self, propuesta):
        try:
            query = "SELECT * FROM propuesta WHERE titulo = %s"
            param = (propuesta.getTitulo(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            propuest = Propuesta(id=data[0], titulo=data[1], estado=data[8],
                             documentacion=data[9], modalidad=data[10],
                             fecha=data[17])
            return propuest

        except Exception as e:
            print e.__class__, e.message
            return None

#CODIGO = ID

    def get_propuesta_codigo(self,propuesta):
        try:
            print "en dao:"+propuesta.getId()
            query = "SELECT * FROM propuesta WHERE id = %s"
            param = (propuesta.getId(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return Propuesta(id=data[0], titulo=data[1], cod_jurado1=data[3],cod_jurado2=data[4],cod_jurado3=data[5],comentario=data[6],
                             entegrables=data[7],estado=data[8],documentacion=data[9],modalidad=data[10],
                             solicitud_retiro=data[11],solicitud_sustentacion=data[12],solicitud_prorroga=data[13],
                             fecha_comentario=data[14],fecha_correcciones=data[15],fecha_entregables=data[16],
                             fecha=data[17])
        except Exception as e:
            print e.message
            return None

    def get_propuesta_consulta(self,propuest):
        if(propuest.getId() == "" and propuest.getTitulo() != ""):
            try:
                query = "SELECT * FROM propuesta WHERE titulo LIKE %s or titulo LIKE %s or titulo LIKE %s"
                param = (propuest.getTitulo()+"%","%"+propuest.getTitulo()+"%","%"+propuest.getTitulo())
                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for propuesta in data:
                    pro = Propuesta(id=propuesta[0], titulo=propuesta[1], director_trabajo=propuesta[2],
                             cod_jurado1=propuesta[3],cod_jurado2=propuesta[4],cod_jurado3=propuesta[5],comentario=propuesta[6],
                             entegrables=propuesta[7],estado=propuesta[8],documentacion=propuesta[9],modalidad=propuesta[10],
                             solicitud_retiro=propuesta[11],solicitud_sustentacion=propuesta[12],solicitud_prorroga=propuesta[13],
                             fecha_comentario=propuesta[14],fecha_correcciones=propuesta[15],fecha_entregables=propuesta[16],
                             fecha=propuesta[17])
                    resultado.append(pro)
                return resultado
            except Exception as e:
                print e.message
                return []
        elif propuest.getId() != "" and propuest.getTitulo() == "":
            try:
                query = "SELECT * FROM propuesta WHERE id LIKE %s or id LIKE %s or id LIKE %s"
                param = (propuest.getId() + "%", "%" + propuest.getId() + "%", "%" + propuest.getCodigo())
                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for propuesta in data:
                    pro = Propuesta(id=propuesta[0], titulo=propuesta[1], director_trabajo=propuesta[2],
                             cod_jurado1=propuesta[3],cod_jurado2=propuesta[4],cod_jurado3=propuesta[5],comentario=propuesta[6],
                             entegrables=propuesta[7],estado=propuesta[8],documentacion=propuesta[9],modalidad=propuesta[10],
                             solicitud_retiro=propuesta[11],solicitud_sustentacion=propuesta[12],solicitud_prorroga=propuesta[13],
                             fecha_comentario=propuesta[14],fecha_correcciones=propuesta[15],fecha_entregables=propuesta[16],
                             fecha=propuesta[17])
                    resultado.append(pro)
                return resultado
            except Exception as e:
                print e.message
                return []
        elif(propuest.getId() != "" and propuest.getTitulo() != ""):
            try:
                print "entro "
                query = "SELECT * FROM propuesta WHERE titulo LIKE %s AND id LIKE %s or titulo LIKE %s AND id LIKE %s or " \
                        "titulo LIKE %s AND id LIKE %s or titulo LIKE %s AND id LIKE %s or titulo LIKE %s AND id LIKE %s or " \
                        "titulo LIKE %s AND id LIKE %s or titulo LIKE %s AND id LIKE %s or titulo LIKE %s AND id LIKE %s or " \
                        "titulo LIKE %s AND id LIKE %s"
                param = (propuest.getTitulo() + "%",propuest.getId() + "%",propuest.getTitulo() + "%", "%" + propuest.getId() + "%",
                         propuest.getTitulo() + "%","%" + propuest.getId(),"%" + propuest.getTitulo() + "%",propuest.getId() + "%",
                         "%" + propuest.getTitulo() + "%","%" + propuest.getId() + "%","%" + propuest.getTitulo() + "%","%" + propuest.getId(),
                         "%" + propuest.getTitulo(),propuest.getId() + "%","%" + propuest.getTitulo(),"%" + propuest.getId() + "%",
                         "%" + propuest.getTitulo(),"%" + propuest.getId())
                # propuest.getCodigo() + "%", "%" + propuest.getCodigo() + "%", "%" + propuest.getCodigo(),
                # propuest.getTitulo() + "%", "%" + propuest.getTitulo() + "%", "%" + propuest.getTitulo()

                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for propuesta in data:
                    pro = Propuesta(id=propuesta[0], titulo=propuesta[1], director_trabajo=propuesta[2],
                             cod_jurado1=propuesta[3],cod_jurado2=propuesta[4],cod_jurado3=propuesta[5],comentario=propuesta[6],
                             entegrables=propuesta[7],estado=propuesta[8],documentacion=propuesta[9],modalidad=propuesta[10],
                             solicitud_retiro=propuesta[11],solicitud_sustentacion=propuesta[12],solicitud_prorroga=propuesta[13],
                             fecha_comentario=propuesta[14],fecha_correcciones=propuesta[15],fecha_entregables=propuesta[16],
                             fecha=propuesta[17])
                    resultado.append(pro)
                return resultado
            except Exception as e:
                print e.message
                return []



    def modificar_estado(self,propuesta):
        try:
            query = "UPDATE propuesta SET estado= %s WHERE id=%s "

            param = (propuesta.getEstado(),propuesta.getId())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False


    def modificar_fechas(self,propuesta):
        if (propuesta.getFecha_Comentario() == None and propuesta.getFecha_Correcciones() == ""
            and propuesta.getFecha_Entregables() != ""):
            try:
                print "entro a la correcta"
                query = "UPDATE propuesta SET fecha_correcciones= %s WHERE id=%s "

                param = (propuesta.getFecha_Correcciones(), propuesta.getId())
                self.__cur.execute(query, param)
                self.__conn.commit()
                return True
            except Exception as e:
                print e.__class__
                print e.message
                return False
        elif(propuesta.getFecha_Comentario() == None and propuesta.getFecha_Correcciones() != ""
             and propuesta.getFecha_Entregables() == ""):
            try:
                print "entro a la correcta"
                query = "UPDATE propuesta SET fecha_correcciones= %s WHERE id=%s "

                param = (propuesta.getFecha_Correcciones(), propuesta.getId())
                self.__cur.execute(query, param)
                self.__conn.commit()
                return True
            except Exception as e:
                print e.__class__
                print e.message
                return False

        elif(propuesta.getFecha_Comentario() != "" and propuesta.getFecha_Correcciones() == None
             and propuesta.getFecha_Entregables() == ""):
            try:
                print "entro a la correcta"
                query = "UPDATE propuesta SET fecha_comentario= %s WHERE id=%s "

                param = (propuesta.getFecha_Comentario(), propuesta.getId())
                self.__cur.execute(query, param)
                self.__conn.commit()
                return True
            except Exception as e:
                print e.__class__
                print e.message
                return False

        elif(propuesta.getFecha_Comentario() != "" and propuesta.getFecha_Correcciones() != ""
             and propuesta.getFecha_Entregables() != ""):
            try:
                print "entro a la correcta"
                query = "UPDATE propuesta SET fecha_correcciones= %s, fecha_comentario= %s WHERE id=%s "

                param = (propuesta.getFecha_Correcciones(),propuesta.getFecha_Comentario(), propuesta.getId())
                self.__cur.execute(query, param)
                self.__conn.commit()
                return True
            except Exception as e:
                print e.__class__
                print e.message
                return False


    def habilitar_envio_entregables(self,propuesta):
        try:
            query = "UPDATE propuesta SET entregables= %s WHERE id=%s "

            param = (propuesta.getEntregables(), propuesta.getId())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False



    def get_propuesta_sin_jurado(self):
        try:
            query = "SELECT * FROM  propuesta WHERE cod_jurado1 IS NULL AND cod_jurado2 IS NULL AND cod_jurado3 IS NULL "
            param = ()
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for propuesta in data:
                pro = Propuesta(id=propuesta[0], titulo=propuesta[1], director_trabajo=propuesta[2],
                             cod_jurado1=propuesta[3],cod_jurado2=propuesta[4],cod_jurado3=propuesta[5],comentario=propuesta[6],
                             entegrables=propuesta[7],estado=propuesta[8],documentacion=propuesta[9],modalidad=propuesta[10],
                             solicitud_retiro=propuesta[11],solicitud_sustentacion=propuesta[12],solicitud_prorroga=propuesta[13],
                             fecha_comentario=propuesta[14],fecha_correcciones=propuesta[15],fecha_entregables=propuesta[16],
                             fecha=propuesta[17])
                resultado.append(pro)
            return resultado
        except Exception as e:
            print e.message
            return []



    def asignar_jurados(self,propuesta,jurado1,jurado2,jurado3):
        try:
            query = "UPDATE propuesta SET cod_jurado1= %s, cod_jurado2= %s, cod_jurado3= %s WHERE titulo=%s "

            param = (jurado1,jurado2,jurado3,propuesta)
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False


    
    def get_propuesta_consulta_jurado(self, jurado):
            try:
                query = "SELECT * FROM  `propuesta` WHERE  `cod_jurado1` = %s OR  `cod_jurado2` =%s " \
                        "OR  `cod_jurado3` =%s"
                param = (jurado.getCodigo(), jurado.getCodigo(), jurado.getCodigo())
                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for propuesta in data:
                    pro = Propuesta(id=propuesta[0], titulo=propuesta[1], director_trabajo=propuesta[2],
                                    cod_jurado1=propuesta[3], cod_jurado2=propuesta[4], cod_jurado3=propuesta[5],
                                    comentario=propuesta[6],
                                    entegrables=propuesta[7], estado=propuesta[8], documentacion=propuesta[9],
                                    modalidad=propuesta[10],
                                    solicitud_retiro=propuesta[11], solicitud_sustentacion=propuesta[12],
                                    solicitud_prorroga=propuesta[13],
                                    fecha_comentario=propuesta[14], fecha_correcciones=propuesta[15],
                                    fecha_entregables=propuesta[16],
                                    fecha=propuesta[17])
                    resultado.append(pro)
                return resultado
            except Exception as e:
                print e.message
                return []


    def get_propuesta_id(self,id_propuesta):
        try:
            query = "SELECT * FROM  `propuesta` WHERE id = %s"
            param = (id_propuesta)
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for propuesta in data:
                pro = Propuesta(id=propuesta[0], titulo=propuesta[1], director_trabajo=propuesta[2],
                                cod_jurado1=propuesta[3], cod_jurado2=propuesta[4], cod_jurado3=propuesta[5],
                                comentario=propuesta[6],
                                entegrables=propuesta[7], estado=propuesta[8], documentacion=propuesta[9],
                                modalidad=propuesta[10],
                                solicitud_retiro=propuesta[11], solicitud_sustentacion=propuesta[12],
                                solicitud_prorroga=propuesta[13],
                                fecha_comentario=propuesta[14], fecha_correcciones=propuesta[15],
                                fecha_entregables=propuesta[16],
                                fecha=propuesta[17])
                resultado.append(pro)
            return resultado
        except Exception as e:
            print e.message
            return []
