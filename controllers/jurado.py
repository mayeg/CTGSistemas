import hashlib
from _hashlib import new

from dao.acta_dao import ActaDao
from dao.tipo_usuario_dao import TipoUsuarioDao
from dao.usuario_dao import UsuarioDao
from dao.propuesta_dao import PropuestaDao
from dao.trabajoDeGrado_dao import TrabajoGradoDao
from dto.acta import Acta
from flask.helpers import flash, url_for
from flask import render_template, redirect, url_for, session
from dto.usuario import Usuario
from dto.propuesta import Propuesta

class JuradoController:
    def __init__(self):
        pass

    def get_view_consultar_propuesta(self):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        propuestas = PropuestaDao().get_propuesta_consulta_jurado(usuario)
        if (propuestas != ""):
            return render_template("jurado/consulta_propuesta.html", usuario=usuario, propuestas=propuestas)
        else:
         flash("No existen Propuestas a cargo.", "error")
         return render_template("jurado/consulta_propuesta.html", usuario=usuario)


    def get_view_consultar_trabajo(self):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        trabajos = TrabajoGradoDao().get_trabajo_consulta_jurado(usuario)
        if (trabajos != ""):
            return render_template("jurado/consulta_trabajo.html", usuario=usuario, trabajos=trabajos)
        else:
            flash("No existen Trabajos a cargo.", "error")
            return render_template("jurado/consulta_trabajo.html", usuario=usuario)


    def get_view_consultar_sustentaciones(self):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        trabajos = TrabajoGradoDao().get_trabajo_consulta_jurado(usuario)
        if (trabajos != ""):
            return render_template("jurado/consulta_sustentacion.html", usuario=usuario, trabajos=trabajos)
        else:
            flash("No existen Trabajos a cargo.", "error")
            return render_template("jurado/consulta_sustentacion.html", usuario=usuario)
