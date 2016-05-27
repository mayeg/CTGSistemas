from dto.propuesta import Propuesta

class PropuestaDao:


    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()


