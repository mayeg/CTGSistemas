from dto.propuesta import Propuesta
from dto.usuario import Usuario


class UsuarioPropuesta:

    def __init__(self, id=0, id_estudiante=0, id_propuesta=0, estado=""):
        self.__id = id
        self.__id_estudiante = Usuario(id=id_estudiante)
        self.__id_propuesta = Propuesta(id=id_propuesta)
        self.__estado = estado

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getId_estudiante(self):
        return self.__id_estudiante

    def setId_estudiante(self, id):
        self.__id_estudiante = id

    def getId_propuesta(self):
        return self.__id_propuesta

    def setId_propuesta(self, id):
        self.__id_propuesta = id

    def getEstado(self):
        return self.__estado

    def setEstado(self, estado):
        self.__estado = estado



