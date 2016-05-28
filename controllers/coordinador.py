from flask import render_template
from flask.helpers import flash
#from dao.TrabajoGrado_dao import TrabajoGradoDao
#from dto.trabajoGrado import TrabajoGrado


class CoordinadorController:
    def __init__(self):
        pass

    def get_view_nombreT(self):
        return render_template("coordinador/nombreT.html")

    #def consulta_nombreT(self, nombre):
     #   trabajoG = TrabajoGrado ("",nombre,"","","","","","","","","","","","","","","","","","","","")

#        if (TrabajoGradoDao.get_trabajo_titulo(trabajoG) is not None):

#         trabajosDeGrado = TrabajoGrado.getTitulo(trabajoG)
 #        return render_template("coordinador/nombreT.html", trabajosDeGrado=trabajosDeGrado)

  #      else:

   #      flash("No existen Trabajos con esos parametros.", "error")

    #    return render_template("coordinador/nombreT.html")







