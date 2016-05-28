


class TrabajoGrado:

    def __init__(self, codigo="", titulo="", director_proyecto="", cod_estudiante1="",
                 cod_estudiante2="", cod_estudiante4="", cod_estudiante3="",
                 cod_jurado1="", cod_jurado2="", cod_jurado3="", correciones="",
                 protocolo="", estado="", documentacion="", modalidad="",
                 fecha_correciones="", fecha_sustentacion="",
                 lugar_sustentacion="", fecha=""):

        self.__codigo = codigo
        self.__titulo = titulo
        self.__director_proyecto = director_proyecto
        self.__cod_estudiante1 = cod_estudiante1
        self.__cod_estudiante2 = cod_estudiante2
        self.__cod_estudiante3 = cod_estudiante3
        self.__cod_estudiante4 = cod_estudiante4
        self.__cod_jurado1 = cod_jurado1
        self.__cod_jurado2 = cod_jurado2
        self.__cod_jurado3 = cod_jurado3
        self.__modalidad = modalidad
        self.__correciones = correciones
        self.__estado = estado
        self.__documentacion = documentacion
        self.__protocolo = protocolo
        self.__fecha_correciones = fecha_correciones
        self.__fecha_sustentacion = fecha_sustentacion
        self.__lugar_sustentacion = lugar_sustentacion
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

    def getCorreciones(self):
        return self.__correciones

    def setCorreciones(self, correciones):
        self.__correciones = correciones

    def getProtocolo(self):
        return self.__protocolo

    def setProtoloco(self, protocolo):
        self.__protocolo = protocolo


    def getDocumentacion(self):
        return self.__documentacion

    def setDocumentacion(self, documentacion):
        self.__documentacion = documentacion


    def getEstado(self):
        return self.__estado

    def setEstado(self, estado):
        self.__estado = estado

    def getFecha_Correciones(self):
        return self.__fecha_correciones

    def setFecha_Correciones(self, fechaC):
        self.__fecha_correciones = fechaC

    def getFecha_Sustentacion(self):
        return self.__fecha_sustentacion

    def setFecha_Sustentacion(self, fecha_sustentacion):
        self.__fecha_sustentacion = fecha_sustentacion

    def getFecha(self):
        return self.__fecha

    def setFecha(self, fecha):
        self.__fecha = fecha




