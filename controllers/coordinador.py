from flask import render_template
from flask.helpers import flash
from dao.trabajoDeGrado_dao import TrabajoGradoDao
from dto.trabajoGrado import TrabajoGrado


class CoordinadorController:
    def __init__(self):
        pass

    def get_view_nombreT(self):
        return render_template("/coordinador/nombreT.html")

    def consulta_nombreT(self, nombre):
        trabajoG = TrabajoGrado ("","",nombre,"","","","","","","","","","","","","","","","")

        if (TrabajoGradoDao().get_trabajo_titulo(trabajoG) is not None):


         trabajosDeGrado = TrabajoGradoDao().get_trabajo_titulo(trabajoG)
         return render_template("/coordinador/nombreT.html", trabajosDeGrado=trabajosDeGrado)

        else:

         flash("No existen Trabajos con esos parametrosiiii.", "error")

        return render_template("/coordinador/nombreT.html")







