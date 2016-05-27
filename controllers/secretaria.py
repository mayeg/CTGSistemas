import hashlib
from _hashlib import new

from dao.acta_dao import ActaDao
from dto.acta import Acta
from flask.helpers import flash
from flask import render_template, redirect, url_for, session


class SecretariaController:
    def __init__(self):
        pass


    def get_view_registro(self):
        return render_template("secretaria/acta/RegistrarActa.html")




    def crear_acta(self,titulo,tipo,fecha,archivo,descripcion):

        acta = Acta(titulo,tipo,fecha,archivo,descripcion)

        if(ActaDao().get_acta_titulo(acta)!= None):
            flash("Ya existe un acta con ese titulo {}.".format(
                acta.getTitulo()), "error")
            return render_template("secretaria/acta/RegistrarActa.html")

        if (ActaDao().crear_acta(acta)):
            flash("El acta se registro correctamente.", "success")
        else:
            flash("Error al registrar el acta.", "error")
        return render_template("secretaria/acta/RegistrarActa.html")





    def get_view_consulta(self):
        return render_template("secretaria/acta/ConsultarActa.html")

    def get_consulta(self,titulo,tipo,fecha):
        acta = Acta(titulo,tipo,fecha,"","")
        if(ActaDao.get_acta_consulta(acta)is not None):
            actas = ActaDao.get_acta_consulta(acta)
            return render_template("secretaria/acta/ConsultarActa.html",actas=actas)
        else:
            flash("No existen Actas con esos parametros.","error")
        return render_template("secretaria/acta/ConsultarActa.html")

    def get_view_descargar(self):
        print "entro"
        return render_template("secretaria/acta/Descargar-ModificarActa.html")

    def get_descarga(self, titulo, tipo, fecha):
        acta = Acta(titulo, tipo, fecha, "", "")
        if (ActaDao.get_acta_consulta(acta) is not None):
            actas = ActaDao.get_acta_consulta(acta)
            return render_template("secretaria/acta/Descargar-ModificarActa.html", actas=actas)
        else:
            flash("No existen Actas con esos parametros.", "error")
        return render_template("secretaria/acta/Descargar-ModificarActa.html")


