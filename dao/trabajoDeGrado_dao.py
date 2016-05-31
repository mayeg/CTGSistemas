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
            return TrabajoGrado(codigo=data[0], titulo=data[1],fecha_sustentacion=data[12],lugar_sustentacion=data[13],
                                   hora_sustentacion=data[17],nota=data[16],fecha=data[15])
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
                    tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1],fecha_sustentacion=trabajo[12],lugar_sustentacion=trabajo[13],
                                   hora_sustentacion=trabajo[17],nota=trabajo[16],fecha=trabajo[15])
                    resultado.append(tra)
                return resultado
            except Exception as e:
                print e.message
                return []

        if (trabaj.getTitulo() != "" and trabaj.getCodigo() == ""):
            try:
                query = "SELECT * FROM `trabajo de grado` WHERE titulo LIKE %s or titulo LIKE %s or titulo LIKE %s"
                param = (trabaj.getTitulo() + "%", "%" + trabaj.getTitulo() + "%", "%" + trabaj.getTitulo())
                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for trabajo in data:
                    tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1],fecha_sustentacion=trabajo[12],lugar_sustentacion=trabajo[13],
                                   hora_sustentacion=trabajo[17],nota=trabajo[16],fecha=trabajo[15])
                    resultado.append(tra)
                return resultado
            except Exception as e:
                print e.message
                return []

        if (trabaj.getTitulo() != "" and trabaj.getCodigo() != ""):
            try:
                print "entro"
                query = "SELECT * FROM `trabajo de grado` WHERE titulo LIKE %s or titulo LIKE %s " \
                        "or titulo LIKE %s AND codigo LIKE %s or `codigo` LIKE %s or `codigo` LIKE %s"
                param = (trabaj.getTitulo() + "%", "%" + trabaj.getTitulo() + "%", "%" + trabaj.getTitulo(),
                         trabaj.getCodigo() + "%", "%" + trabaj.getCodigo() + "%", "%" + trabaj.getCodigo())
                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for trabajo in data:
                    tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1],fecha_sustentacion=trabajo[12],lugar_sustentacion=trabajo[13],
                                   hora_sustentacion=trabajo[17],nota=trabajo[16],fecha=trabajo[15])
                    resultado.append(tra)
                return resultado
            except Exception as e:
                print e.message
                return []

    def get_trabajo_codigo(self, codigo):
        try:
            query = "SELECT * FROM `trabajo de grado`  WHERE codigo = %s"
            param = (codigo,)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return TrabajoGrado(codigo=data[0], titulo=data[1],fecha_sustentacion=data[12],lugar_sustentacion=data[13],
                                   hora_sustentacion=data[17],nota=data[16],fecha=data[15])
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


    def get_trabajos_sin_sustentacion(self):
        try:
            print "entra a dao"
            query = "SELECT * FROM  `trabajo de grado` WHERE  fecha_sustentacion ='' AND  lugar_sustentacion ='' " \
                    "AND  hora_sustentacion =''"
            param = ()
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for trabajo in data:
                tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1],fecha_sustentacion=trabajo[12],lugar_sustentacion=trabajo[13],
                                   hora_sustentacion=trabajo[17],nota=trabajo[16],fecha=trabajo[15])
                resultado.append(tra)
            return resultado
        except Exception as e:
            print e.message
            return []


    def agregar_datos_sustentacion(self,trabajo):
        try:
            query = "UPDATE `trabajo de grado` SET fecha_sustentacion= %s, lugar_sustentacion= %s, hora_sustentacion= %s" \
                    "WHERE codigo=%s"

            param = (trabajo.getFecha_Sustentacion(),trabajo.getLugar_Sustentacion(),trabajo.getHora_Sustentacion(),
                     trabajo.getCodigo())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False


    def get_trabajos_sin_jurados(self):
        try:
            query = "SELECT * FROM  `trabajo de grado` WHERE cod_jurado1 =  '' AND cod_jurado2 =  '' AND cod_jurado3 =  '' "
            param = ()
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for trabajo in data:
                tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1],fecha_sustentacion=trabajo[12],lugar_sustentacion=trabajo[13],
                                   hora_sustentacion=trabajo[17],nota=trabajo[16],fecha=trabajo[15])
                resultado.append(tra)
            return resultado
        except Exception as e:
            print e.message
            return []

    def asignar_jurados_trabajo(self, trabajo, jurado1, jurado2, jurado3):
        try:
            query = "UPDATE `trabajo de grado` SET cod_jurado1= %s, cod_jurado2= %s, cod_jurado3= %s WHERE titulo=%s "

            param = (jurado1, jurado2, jurado3, trabajo)
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False


    def get_propuesta_consulta_jurado(self, jurado):
            try:
                print jurado.getCodigo()
                query = "SELECT * FROM  `propuesta` WHERE  `cod_jurado1` = %s OR  `cod_jurado2` =%s " \
                        "OR  `cod_jurado3` =%s"
                param = (jurado.getCodigo(), jurado.getCodigo(), jurado.getCodigo())
                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for propuesta in data:
                    pro = Propuesta(codigo=propuesta[0], titulo=propuesta[1], director_propuesta=propuesta[2],
                                    cod_jurado1=propuesta[3], cod_jurado2=propuesta[4], cod_jurado3=propuesta[5],
                                    comentario=propuesta[6],
                                    entegrables=propuesta[7], estado=propuesta[8], documentacion=propuesta[9],
                                    modalidad=propuesta[10],
                                    solicitud_retiro=propuesta[11], solicitud_sustentacion=propuesta[12],
                                    solicitud_prorroga=propuesta[13],
                                    fecha_comentario=propuesta[14], fecha_correcciones=propuesta[15],
                                    fecha_entregables=propuesta[16],
                                    fecha=propuesta[17])
                    print pro.getCodigo()
                    resultado.append(pro)
                return resultado
            except Exception as e:
                print e.message
                return []
