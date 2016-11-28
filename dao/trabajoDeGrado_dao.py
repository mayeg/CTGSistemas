from dto.trabajoGrado import TrabajoGrado


class TrabajoGradoDao:
    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()

    def get_trabajo_titulo(self, trabajoG):
        try:
            query = "SELECT * FROM trabajo_de_grado  WHERE titulo = %s"
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
                query = "SELECT * FROM trabajo_de_grado WHERE codigo LIKE %s or codigo LIKE %s or codigo LIKE %s"
                param = (trabaj.getCodigo() + "%", "%" + trabaj.getCodigo() + "%", "%" + trabaj.getCodigo())
                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for trabajo in data:
                    tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1],cod_jurado1=trabajo[2],cod_jurado2=trabajo[3],
                                       cod_jurado3=trabajo[4],correciones=trabajo[5],documentacion=trabajo[6],estado=trabajo[7],
                                       fecha_correcciones=trabajo[8],nota=trabajo[9],id_propuesta=trabajo[10],
                                       fecha=trabajo[11],fecha_sustentacion=trabajo[12],lugar_sustentacion=trabajo[13],
                                        hora_sustentacion=trabajo[14])
                    resultado.append(tra)
                return resultado
            except Exception as e:
                print e.message
                return []

        if (trabaj.getTitulo() != "" and trabaj.getCodigo() == ""):
            try:
                query = "SELECT * FROM trabajo_de_grado WHERE titulo LIKE %s or titulo LIKE %s or titulo LIKE %s"
                param = (trabaj.getTitulo() + "%", "%" + trabaj.getTitulo() + "%", "%" + trabaj.getTitulo())
                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for trabajo in data:
                    tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1], cod_jurado1=trabajo[2],
                                       cod_jurado2=trabajo[3],
                                       cod_jurado3=trabajo[4], correciones=trabajo[5], documentacion=trabajo[6], estado=trabajo[7],
                                       fecha_correcciones=trabajo[8], nota=trabajo[9], id_propuesta=trabajo[10],
                                       fecha=trabajo[11], fecha_sustentacion=trabajo[12],
                                       lugar_sustentacion=trabajo[13],
                                       hora_sustentacion=trabajo[14])
                    resultado.append(tra)
                return resultado
            except Exception as e:
                print e.message
                return []

        if (trabaj.getTitulo() != "" and trabaj.getCodigo() != ""):
            try:
                query = "SELECT * FROM trabajo_de_grado WHERE titulo LIKE %s AND codigo LIKE %s or titulo LIKE %s AND codigo LIKE %s or " \
                        "titulo LIKE %s AND codigo LIKE %s or titulo LIKE %s AND codigo LIKE %s or titulo LIKE %s AND codigo LIKE %s or " \
                        "titulo LIKE %s AND codigo LIKE %s or titulo LIKE %s AND codigo LIKE %s or titulo LIKE %s AND codigo LIKE %s or " \
                        "titulo LIKE %s AND codigo LIKE %s"
                param = (trabaj.getTitulo() + "%",trabaj.getCodigo() + "%",trabaj.getTitulo() + "%", "%" + trabaj.getCodigo() + "%",
                         trabaj.getTitulo() + "%","%" + trabaj.getCodigo(),"%" + trabaj.getTitulo() + "%",trabaj.getCodigo() + "%",
                         "%" + trabaj.getTitulo() + "%","%" + trabaj.getCodigo() + "%","%" + trabaj.getTitulo() + "%","%" + trabaj.getCodigo(),
                         "%" + trabaj.getTitulo(),trabaj.getCodigo() + "%","%" + trabaj.getTitulo(),"%" + trabaj.getCodigo() + "%",
                         "%" + trabaj.getTitulo(),"%" + trabaj.getCodigo())
                self.__cur.execute(query, param)
                data = self.__cur.fetchall()
                resultado = list()
                if data is None:
                    return []
                for trabajo in data:
                    tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1], cod_jurado1=trabajo[2],
                                       cod_jurado2=trabajo[3],
                                       cod_jurado3=trabajo[4], correciones=trabajo[5], documentacion=trabajo[6], estado=trabajo[7],
                                       fecha_correcciones=trabajo[8], nota=trabajo[9], id_propuesta=trabajo[10],
                                       fecha=trabajo[11], fecha_sustentacion=trabajo[12],
                                       lugar_sustentacion=trabajo[13],
                                       hora_sustentacion=trabajo[14])
                    resultado.append(tra)
                return resultado
            except Exception as e:
                print e.message
                return []

    def get_trabajo_codigo(self, codigo):
        try:
            query = "SELECT * FROM trabajo_de_grado  WHERE codigo = %s"
            param = (codigo,)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return TrabajoGrado(codigo=data[0], titulo=data[1], cod_jurado1=data[2], cod_jurado2=data[3],
                                cod_jurado3=data[4], correciones=data[5], documentacion=data[6], estado=data[7],
                                fecha_correcciones=data[8], nota=data[9], id_propuesta=data[10],
                                fecha=data[11], fecha_sustentacion=data[12], lugar_sustentacion=data[13],
                                hora_sustentacion=data[14])
        except Exception as e:
            print e.message
            return None


    def registrar_nota(self,trabajo):
        try:
            query = "UPDATE trabajo_de_grado SET nota= %s WHERE codigo=%s "

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
            query = "UPDATE  `ufps_15`.`trabajo_de_grado` SET  `fecha_correciones` =  %s WHERE  `trabajo_de_grado`.`codigo` =%s "

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
            query = "SELECT * FROM  trabajo_de_grado WHERE  fecha_sustentacion IS NULL AND  lugar_sustentacion IS NULL " \
                    "AND  hora_sustentacion IS NULL"
            param = ()
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for trabajo in data:
                tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1], cod_jurado1=trabajo[2], cod_jurado2=trabajo[3],
                                   cod_jurado3=trabajo[4], correciones=trabajo[5], documentacion=trabajo[6], estado=trabajo[7],
                                   fecha_correcciones=trabajo[8], nota=trabajo[9], id_propuesta=trabajo[10],
                                   fecha=trabajo[11], fecha_sustentacion=trabajo[12], lugar_sustentacion=trabajo[13],
                                   hora_sustentacion=trabajo[14])
                resultado.append(tra)
            return resultado
        except Exception as e:
            print(e.message)
            return []


    def agregar_datos_sustentacion(self,trabajo):
        try:
            query = "UPDATE trabajo_de_grado SET fecha_sustentacion= %s, lugar_sustentacion= %s, hora_sustentacion= %s" \
                    "WHERE codigo=%s"

            param = (trabajo.getFecha_Sustentacion(),trabajo.getLugar_Sustentacion(),trabajo.getHora_Sustentacion(),
                     trabajo.getCodigo())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print(e.__class__)
            print(e.message)
            return False


    def get_trabajos_sin_jurados(self):
        try:
            query = "SELECT * FROM  trabajo_de_grado WHERE cod_jurado1 = '--' AND cod_jurado2 '--' AND cod_jurado3 '--' "
            param = ()
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for trabajo in data:
                tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1], cod_jurado1=trabajo[2], cod_jurado2=trabajo[3],
                                   cod_jurado3=trabajo[4], correciones=trabajo[5], documentacion=trabajo[6], estado=trabajo[7],
                                   fecha_correcciones=trabajo[8], nota=trabajo[9], id_propuesta=trabajo[10],
                                   fecha=trabajo[11], fecha_sustentacion=trabajo[12], lugar_sustentacion=trabajo[13],
                                   hora_sustentacion=trabajo[14])
                resultado.append(tra)
            return resultado
        except Exception as e:
            print(e.message)
            return []

    def asignar_jurados_trabajo(self, trabajo, jurado1, jurado2, jurado3):
        try:
            query = "UPDATE trabajo_de_grado SET cod_jurado1= %s, cod_jurado2= %s, cod_jurado3= %s WHERE titulo=%s "

            param = (jurado1, jurado2, jurado3, trabajo)
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print(e.__class__)
            print(e.message)
            return False


    def get_trabajo_consulta_jurado(self,jurado):
        try:
            query = "SELECT * FROM trabajo_de_grado  WHERE cod_jurado1 = %s or cod_jurado2 =%s or cod_jurado3 =%s"
            param = (jurado.getCodigo(),jurado.getCodigo(),jurado.getCodigo())
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for trabajoG in data:
                for trabajo in data:
                    tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1], cod_jurado1=trabajo[2],
                                       cod_jurado2=trabajo[3],
                                       cod_jurado3=trabajo[4], correciones=trabajo[5], documentacion=trabajo[6], estado=trabajo[7],
                                       fecha_correcciones=trabajo[8], nota=trabajo[9], id_propuesta=trabajo[10],
                                       fecha=trabajo[11], fecha_sustentacion=trabajo[12],
                                       lugar_sustentacion=trabajo[13],
                                       hora_sustentacion=trabajo[14])
                    resultado.append(tra)
            return resultado
        except Exception as e:
            print e.message
            return []
    
    def get_trabajo_tituloT(self, trabajoG):
        try:
            query = "SELECT * FROM `trabajo_de_grado` WHERE titulo LIKE  %s or titulo LIKE %s or titulo LIKE %s"
            param = (trabajoG.getTitulo() + "%", "%" + trabajoG.getTitulo() + "%", "%" + trabajoG.getTitulo())
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()

            if data is None:
                return None
            for trabajo in data:
                pro = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1],fecha=trabajo[11],fecha_sustentacion=trabajo[12],
                                estado=trabajo[7], nota = trabajo[9])
                resultado.append(pro)
            return resultado

        except Exception as e:
            print e.message
            return None

    def get_trabajo_modalidadT(self, trabajoG, trabajo_a):

        try:
            query = "SELECT * FROM `trabajo_de_grado` WHERE modalidad = %s AND fecha LIKE %s"
            param = (trabajoG.getModalidad(), trabajo_a+"%")
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for trabajo in data:
                tra = TrabajoGrado(codigo=data[0], titulo=data[1],fecha=data[11],fecha_sustentacion=data[12],
                                estado=data[7], nota = data[9])
                resultado.append(tra)
            return resultado
        except Exception as e:
            print e.message
            return []

    def get_trabajo_estadoT(self, trabajoG, trabajo_a):

        try:
            query = "SELECT * FROM `trabajo_de_grado` WHERE estado = %s AND fecha LIKE %s"
            param = (trabajoG.getEstado(), trabajo_a + "%")
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for trabajo in data:
                tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1], cod_jurado1=trabajo[2], cod_jurado2=trabajo[3],
                                   cod_jurado3=trabajo[4], correciones=trabajo[5], documentacion=trabajo[6],
                                   estado=trabajo[7],
                                   fecha_correcciones=trabajo[8], nota=trabajo[9], id_propuesta=trabajo[10],
                                   fecha=trabajo[11], fecha_sustentacion=trabajo[12], lugar_sustentacion=trabajo[13],
                                   hora_sustentacion=trabajo[14])
                resultado.append(tra)
            return resultado
        except Exception as e:
            print e.message
            return []



    def get_trabajo_Jurado(self, trabajoG):
        try:
            query = "SELECT * FROM `trabajo_de_grado` WHERE  cod_jurado1 = %s or cod_jurado2 = %s or cod_jurado3 = %s"
            param = (trabajoG.getCod_jurado1(), trabajoG.getCod_jurado1(), trabajoG.getCod_jurado1(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for trabajo in data:
                tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1], cod_jurado1=trabajo[2], cod_jurado2=trabajo[3],
                                   cod_jurado3=trabajo[4], correciones=trabajo[5], documentacion=trabajo[6],
                                   estado=trabajo[7],
                                   fecha_correcciones=trabajo[8], nota=trabajo[9], id_propuesta=trabajo[10],
                                   fecha=trabajo[11], fecha_sustentacion=trabajo[12], lugar_sustentacion=trabajo[13],
                                   hora_sustentacion=trabajo[14])
                resultado.append(tra)
            return resultado
        except Exception as e:
            print e.message
            return []

    def get_trabajo_Estudiante(self, trabajoG):
        try:
            query = "SELECT * FROM trabajo_de_grado WHERE id_propuesta =%s"
            param = (trabajoG.getId_propuesta().getId(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return None
            for trabajo in data:
                tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1], cod_jurado1=trabajo[2], cod_jurado2=trabajo[3],
                                   cod_jurado3=trabajo[4], correciones=trabajo[5], documentacion=trabajo[6], estado=trabajo[7],
                                   fecha_correcciones=trabajo[8], nota=trabajo[9], id_propuesta=trabajo[10],
                                   fecha=trabajo[11], fecha_sustentacion=trabajo[12], lugar_sustentacion=trabajo[13],
                                   hora_sustentacion=trabajo[14])
                resultado.append(tra)
            return resultado
        except Exception as e:
            print e.message
            return None

    def get_trabajos_Jurado(self, jurado):
        try:
            query = "SELECT * FROM `trabajo_de_grado` WHERE  cod_jurado1 = %s or cod_jurado2 = %s or cod_jurado3 = %s"
            param = (jurado.getCodigo(), jurado.getCodigo(), jurado.getCodigo())
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for trabajo in data:
                act = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1], fecha=trabajo[11], fecha_sustentacion=trabajo[12],lugar_sustentacion=trabajo[13],hora_sustentacion=trabajo[14])
                resultado.append(act)
            return resultado
        except Exception as e:
            print e.message
            return []
        
        

    def get_trabajos(self):
        try:
            query = "SELECT * FROM trabajo_de_grado "
            param = ()
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()

            if data is None:
                return None
            for trabajo in data:
                tra = TrabajoGrado(codigo=trabajo[0], titulo=trabajo[1], cod_jurado1=trabajo[2], cod_jurado2=trabajo[3],
                                   cod_jurado3=trabajo[4], correciones=trabajo[5], documentacion=trabajo[6], estado=trabajo[7],
                                   fecha_correcciones=trabajo[8], nota=trabajo[9], id_propuesta=trabajo[10],
                                   fecha=trabajo[11], fecha_sustentacion=trabajo[12], lugar_sustentacion=trabajo[13],
                                   hora_sustentacion=trabajo[14])
                resultado.append(tra)
            return resultado

        except Exception as e:
            print e.message
            return None
        
    def de_propuesta_a_trabajo_de_grado(self,trabajo):
        try:
            query = "INSERT INTO `trabajo_de_grado` (`titulo` ,`cod_jurado1` ,`cod_jurado2` ,`cod_jurado3` ," \
                    "`documentacion` ,`estado` ,`nota` ,`id_propuesta` ,  `fecha` ,`fecha_sustentacion` ," \
                    "`lugar_sustentacion` ,`hora_sustentacion`) VALUES (%s, %s,  %s,  %s, %s, %s, %s, %s ," \
                    "  %s ,  %s,  %s,  %s)"
            param = (trabajo.getTitulo(),'--','--','--',
                    trabajo.getDocumentacion(),'Activo','0',trabajo.getId_propuesta().getId(),trabajo.getFecha(),
                     trabajo.getFecha_Sustentacion(),trabajo.getLugar_Sustentacion(),trabajo.getHora_Sustentacion())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False
