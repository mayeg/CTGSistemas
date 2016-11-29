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
            print data, 'data'
            if data is None:
                return None
            propuest = Propuesta(id=data[0], titulo=data[1], documentacion=data[7],
                                 modalidad=data[8], fecha=data[14])
            return propuest

        except Exception as e:
            print e.__class__, e.message
            return None



    def subir_correcciones(self, prop):
        try:
            query = "UPDATE propuesta SET documentacion=%s " \
                    "WHERE id=%s"
            param = (prop.getId_propuesta().getDocumentacion(),
                     prop.getId_propuesta().getId())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__, e.message
            return False

    def solicitar_sustentacion(self, prop):
        try:
            query = "UPDATE propuesta SET solicitud_sustentacion=%s " \
                    "WHERE id=%s"
            param = (prop.getId_propuesta().getSolicitud_Sustentacion(),
                     prop.getId_propuesta().getId())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__, e.message
            return False

    def solicitar_retiro_propuesta(self, prop):
        try:
            query = "UPDATE propuesta SET solicitud_retiro=%s " \
                    "WHERE id=%s"
            param = (prop.getId_propuesta().getSolicitud_retiro(),
                     prop.getId_propuesta().getId())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__, e.message
            return False

    def solicitar_prorroga(self, prop):
        try:
            print(prop.getId_propuesta().getSolicitud_prorroga())
            query = "UPDATE propuesta SET solicitud_prorroga=%s " \
                            "WHERE id=%s"
            param = (prop.getId_propuesta().getSolicitud_prorroga(),
                             prop.getId_propuesta().getId())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__, e.message
            return False

#CODIGO = ID

    def get_propuesta_codigo(self,propuestaa):
        try:
            query = "SELECT * FROM propuesta WHERE id = %s"
            param = (propuestaa.getId(),)
            self.__cur.execute(query, param)
            propuesta = self.__cur.fetchone()
            if propuesta is None:
                return None
            return Propuesta(id=propuesta[0], titulo=propuesta[1], director_trabajo=propuesta[2],
                             cod_jurado1=propuesta[3],cod_jurado2=propuesta[4],cod_jurado3=propuesta[5],comentario=propuesta[6],
                             documentacion=propuesta[7],modalidad=propuesta[8],solicitud_retiro=propuesta[9],
                             solicitud_sustentacion=propuesta[10],solicitud_prorroga=propuesta[11],
                             fecha_comentario=propuesta[12],fecha_correcciones=propuesta[13],fecha=propuesta[14])
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
                             documentacion=propuesta[7],modalidad=propuesta[8],solicitud_retiro=propuesta[9],
                             solicitud_sustentacion=propuesta[10],solicitud_prorroga=propuesta[11],
                             fecha_comentario=propuesta[12],fecha_correcciones=propuesta[13],fecha=propuesta[14])
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
                             documentacion=propuesta[7],modalidad=propuesta[8],solicitud_retiro=propuesta[9],
                             solicitud_sustentacion=propuesta[10],solicitud_prorroga=propuesta[11],
                             fecha_comentario=propuesta[12],fecha_correcciones=propuesta[13],fecha=propuesta[14])
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
                             documentacion=propuesta[7],modalidad=propuesta[8],solicitud_retiro=propuesta[9],
                             solicitud_sustentacion=propuesta[10],solicitud_prorroga=propuesta[11],
                             fecha_comentario=propuesta[12],fecha_correcciones=propuesta[13],fecha=propuesta[14])
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
        if(propuesta.getFecha_Comentario() == None and propuesta.getFecha_Correcciones() != ""):
            try:

                query = "UPDATE propuesta SET fecha_correcciones= %s WHERE id=%s "

                param = (propuesta.getFecha_Correcciones(), propuesta.getId())
                self.__cur.execute(query, param)
                self.__conn.commit()
                return True
            except Exception as e:
                print e.__class__
                print e.message
                return False

        elif(propuesta.getFecha_Comentario() != "" and propuesta.getFecha_Correcciones() == None):
            try:

                query = "UPDATE propuesta SET fecha_comentario= %s WHERE id=%s "

                param = (propuesta.getFecha_Comentario(), propuesta.getId())
                self.__cur.execute(query, param)
                self.__conn.commit()
                return True
            except Exception as e:
                print e.__class__
                print e.message
                return False

        elif(propuesta.getFecha_Comentario() != "" and propuesta.getFecha_Correcciones() != ""):
            try:

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
            query = "SELECT * FROM  propuesta WHERE cod_jurado1 IS NULL OR cod_jurado2 IS NULL OR cod_jurado3 IS NULL "
            param = ()
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for propuesta in data:
                pro = Propuesta(id=propuesta[0], titulo=propuesta[1])
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
                pro = Propuesta(id=propuesta[0],titulo=propuesta[1], fecha_comentario=propuesta[12],comentario=propuesta[6])
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
                             cod_jurado1=propuesta[3],cod_jurado2=propuesta[4],cod_jurado3=propuesta[5],comentario=propuesta[6],
                             documentacion=propuesta[7],modalidad=propuesta[8],solicitud_retiro=propuesta[9],
                             solicitud_sustentacion=propuesta[10],solicitud_prorroga=propuesta[11],
                             fecha_comentario=propuesta[12],fecha_correcciones=propuesta[13],fecha=propuesta[14])
                resultado.append(pro)
            return resultado
        except Exception as e:
            print e.message
            return []
            
            
    def get_propuesta_consultaN(self, propuest):
        try:
            query = "SELECT * FROM `propuesta` WHERE titulo LIKE  %s or titulo LIKE %s or titulo LIKE %s"
            param = (propuest.getTitulo() + "%", "%" + propuest.getTitulo() + "%", "%" + propuest.getTitulo())
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()

            if data is None:
                return None
            for propuesta in data:
                pro = Propuesta(titulo=propuesta[1], director_trabajo=propuesta[2],comentario=propuesta[6],fecha=propuesta[14],
                                modalidad = propuesta[8])
                resultado.append(pro)
            return resultado

        except Exception as e:
            print e.message
            return None
            
            
    def get_propuesta_cancelar(self, propuesta, estado):
        try:
            query = "UPDATE `propuesta` SET estado= %s WHERE titulo=%s "
            param = (propuesta.getEstado(),propuesta.getTitulo(),)
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False




    def get_propuesta_estado(self, propuesta):
        try:
            query = "SELECT * FROM `propuesta` WHERE estado = %s"
            param = (propuesta.getEstado(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()

            if data is None:
                return None
            for propuesta in data:
                pro = Propuesta(titulo=propuesta[1], director_trabajo=propuesta[2],comentario=propuesta[7],estado=propuesta[9],
                                modalidad = propuesta[11])
                resultado.append(pro)
            return resultado

        except Exception as e:
            print e.message
            return None
        

    def get_propuesta2(self, propuesta):

        try:
            query = "SELECT * FROM `propuesta` WHERE id = %s"
            param = (propuesta,)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return Propuesta(id=data[0], titulo=data[1], director_trabajo=data[2], comentario=data[7], estado=data[9],
                             modalidad=data[11])
        except Exception as e:
            print e.message
            return None

    def get_comentarios(self, id):

        try:
            query = "SELECT Comentario FROM `propuesta` WHERE id = %s"
            param = (id,)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return data[0]
        except Exception as e:
            print e.message
            return None

    def get_guardar_comentario(self, id, comentario):
        try:
            query = "UPDATE propuesta SET comentario= %s WHERE id=%s "
            param = (comentario, id)
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False

    def get_propuesta_solicitud_sustentacion(self):
        try:
            query = "SELECT * FROM propuesta WHERE `solicitud_sustentacion` IS NOT NULL"
            self.__cur.execute(query)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for propuesta in data:
                pro = Propuesta(id=propuesta[0], titulo=propuesta[1], director_trabajo=propuesta[2],
                                cod_jurado1=propuesta[3], cod_jurado2=propuesta[4], cod_jurado3=propuesta[5],
                                comentario=propuesta[6],documentacion=propuesta[7], modalidad=propuesta[8],
                                solicitud_retiro=propuesta[9], solicitud_sustentacion=propuesta[10],
                                solicitud_prorroga=propuesta[11],
                                fecha_comentario=propuesta[12], fecha_correcciones=propuesta[13], fecha=propuesta[14])
                resultado.append(pro)
            return resultado
        except Exception as e:
            print e.message
            return []

    def verificar_propuesta_activa(self,propuesta):
        try:
            query = "SELECT * FROM  `propuesta` AS p INNER JOIN  `usuario_propuesta` AS u ON p.id = u.id_propuesta " \
                    "AND u.estado = 'Activa' AND p.solicitud_sustentacion IS NOT NULL AND p.id = %s"
            param = (propuesta.getId(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return False
            return True

        except Exception as e:
            print e.__class__, e.message
            return False

    def get_propuesta_modalidadT(self, propuesta):
        try:

            query = "SELECT * FROM `propuesta` WHERE modalidad = %s"
            param = (propuesta.getModalidad(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            print data, 'Data proues'
            resultado = list()
            if data is None:
                return []
            for propuesta in data:
                pro = Propuesta(id=propuesta[0],)
                resultado.append(pro)

            return resultado
        except Exception as e:
            print e.message
            return []

