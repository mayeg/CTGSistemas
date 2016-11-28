class Protocolo:

    def __init__(self, nombre="", descripcion="", filename=""):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__filename = filename



    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre = nombre

    def getDescripcion(self):
        return self.__descripcion

    def setDescripcion(self,descripcion):
        self.__descripcion = descripcion

    def getFilename(self):
        return self.__filename

    def setFilename(self,filename):
        self.__filename = filename
