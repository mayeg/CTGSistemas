class Protocolo:

    def __init__(self, id=0, nombre="", descripcion="", documento=""):
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__documento = documento

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre = nombre

    def getDescripcion(self):
        return self.__descripcion

    def setDescripcion(self,descripcion):
        self.__descripcion = descripcion

    def getDocumento(self):
        return self.__documento

    def setDocumento(self, documento):
        self.__documento = documento
