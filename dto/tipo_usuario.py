class TipoUsuario:

    def __init__(self, id=0, nombre="", label=""):
        self.__id = id
        self.__nombre = nombre
        self.__label = label

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getLabel(self):
        return self.__label

    def setLabel(self, label):
        self.__label = label