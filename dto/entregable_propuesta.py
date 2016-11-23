from dto.propuesta import Propuesta


class EntregablePropuesta:
    def __init__(self, id=0, id_propuesta=0, entregable="", fecha_entregable="",
                  fecha=""):
        self.__id = id
        self.__id_propuesta = Propuesta(id=id_propuesta)
        self.__entregable = entregable
        self.__fecha_entregable = fecha_entregable
        self.__fecha = fecha

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getId_propuesta(self):
        return self.__id_propuesta

    def setId_propuesta(self, id):
        self.__id_propuesta = id

    def getEntregable(self):
        return self.__entregable

    def setEntregable(self, entregable):
        self.__entregable = entregable

    def getFecha_Entregable(self):
        return self.__fecha_entregable

    def setFecha_Entregable(self, fechaEntregable):
        self.__fecha_entregable = fechaEntregable

    def getFecha(self):
        return self.__fecha

    def setFecha(self, fecha):
        self.__fecha = fecha