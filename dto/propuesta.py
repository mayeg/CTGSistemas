class Propuesta:

    def __init__(self, codigo="", titulo="", director_propuesta="",
                 cod_estudiante1="", cod_estudiante2="",
                 cod_estudiante4="", cod_estudiante3="",cod_jurado1="",
                 cod_jurado2="", cod_jurado3="", comentario="", entegrables="",
                 estado="", documentacion="", modalidad="", solicitud_retiro="",
                 solicitud_sustentacion="", solicitud_prorroga="",
                 fecha_cometario="", fecha_entregables="", fecha=""):

        self.__codigo = codigo
        self.__titulo = titulo
        self.__director_propuesta = director_propuesta
        self.__cod_estudiante1 = cod_estudiante1
        self.__cod_estudiante2 = cod_estudiante2
        self.__cod_estudiante3 = cod_estudiante3
        self.__cod_estudiante4 = cod_estudiante4
        self.__cod_jurado1 = cod_jurado1
        self.__cod_jurado1 = cod_jurado2
        self.__cod_jurado1 = cod_jurado3
        self.__comentario = comentario
        self.__entegrables = entegrables
        self.__estado = estado
        self.__documentacion = documentacion
        self.__modalidad = modalidad
        self.__solicitud_retiro = solicitud_retiro
        self.__solicitud_sustentacion = solicitud_sustentacion
        self.__solicitud_prorroga = solicitud_prorroga
        self.__fecha_cometario = fecha_cometario
        self.__fecha_entregables = fecha_entregables
        self.__fecha = fecha


    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getTitulo(self):
        return self.__titulo

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def getDirector_proyecto(self):
        return self.__director_proyecto

    def setDirector_proyecto(self, director_proyecto):
        self.__director_proyecto = director_proyecto

    def getCod_estudiante1(self):
        return self.__cod_estudiante1

    def setCod_estudiante1(self, cod_estudiante1):
        self.__cod_estudiante1 = cod_estudiante1

    def getCod_estudiante2(self):
        return self.__cod_estudiante2

    def setCod_estudiante2(self, cod_estudiante2):
        self.__cod_estudiante2 = cod_estudiante2

    def getCod_estudiante3(self):
        return self.__cod_estudiante3

    def setCod_estudiante3(self, cod_estudiante3):
        self.__cod_estudiante3 = cod_estudiante3

    def getCod_estudiante4(self):
        return self.__cod_estudiante4

    def setCod_estudiante4(self, cod_estudiante4):
        self.__cod_estudiante4 = cod_estudiante4

    def getCod_jurado1(self):
        return self.__cod_jurado1

    def setCod_jurado1(self, cod_jurado1):
        self.__cod_jurado1 = cod_jurado1

    def getCod_jurado2(self):
        return self.__cod_jurado2

    def setCod_jurado2(self, cod_jurado2):
        self.__cod_jurado2 = cod_jurado2

    def getCod_jurado3(self):
        return self.__cod_jurado3

    def setCod_jurado3(self, cod_jurado3):
        self.__cod_jurado3 = cod_jurado3

    def getModalidad(self):
        return self.__modalidad

    def setModalidad(self, modalidad):
        self.__modalidad = modalidad

    def getEntregables(self):
        return self.__entegrables

    def setEntregables(self, entregables):
        self.__entegrables = entregables

    def getComentario(self):
        return self.__comentario

    def setComentario(self, comentario):
        self.__comentario = comentario


    def getDocumentacion(self):
        return self.__documentacion

    def setDocumentacion(self, documentacion):
        self.__documentacion = documentacion

    def getEstado(self):
        return self.__estado

    def setEstado(self, estado):
        self.__estado = estado

    def getFecha_Comentario(self):
        return self.__fecha_comentario

    def setFecha_Comentario(self, fechaComentario):
        self.__fecha_comentario = fechaComentario

    def getFecha_Entregables(self):
        return self.__fecha_entregables

    def setFecha_Entregables(self, fechaEntregable):
        self.__fecha_entregables = fechaEntregable

    def getSolicitud_retiro(self):
        return self.__solicitud_retiro

    def setSolicitud_retiro(self, solucitud_retiro):
        self.__solicitud_retiro = solucitud_retiro

    def getSolicitud_prorroga(self):
        return self.__solicitud_prorroga

    def setSolicitud_prorroga(self, solucitud_prorroga):
        self.__solicitud_prorroga = solucitud_prorroga

    def getSolicitud_Sustentacion(self):
        return self.__solicitud_sustentacion

    def setSolicitud_Sustentacion(self, solucitud_sustentacion):
        self.__solicitud_sustentacion = solucitud_sustentacion

    def getFecha(self):
        return self.__fecha

    def setFecha(self, fecha):
        self.__fecha = fecha





