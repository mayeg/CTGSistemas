


class Acta:

    def __init__(self,codigo="", titulo="", tipo="", fecha="", archivo="", descripcion=""):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__tipo = tipo
        self.__fecha = fecha
        self.__archivo = archivo
        self.__descripcion = descripcion


    def getCodigo(self):
        return self.__codigo

    def setCodigo(self,codigo):
        return self.__codigo

    def getTitulo(self):
        return self.__titulo

    def getTipo(self):
        return self.__tipo

    def getFecha(self):
        return self.__fecha

    def getArchivo(self):
        return self.__archivo

    def getDescripcion(self):
        return self.__descripcion

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setTipo(self, tipo):
        self.__tipo = tipo

    def setFecha(self, fecha):
        self.__fecha = fecha

    def setArchivo(self, archivo):
        self.__archivo = archivo

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

