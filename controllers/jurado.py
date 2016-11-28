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
        codigo = session['usuario']['codigo']
        usuario = UsuarioDao().get_usuario_por_codigo(
            Usuario(codigo=codigo))
        propuestas = PropuestaDao().get_propuesta_consulta_jurado(usuario)
        if (propuestas != ""):

            return render_template("jurado/consulta_propuesta.html", usuario=usuario, propuestas=propuestas)
        else:
         flash("No existen Propuestas a cargo.", "error")
         return render_template("jurado/consulta_propuesta.html", usuario=usuario)


    def get_view_consultar_trabajo(self):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        trabajos = TrabajoGradoDao().get_trabajos_Jurado(usuario)
        if (trabajos != ""):
            return render_template("jurado/consulta_trabajo.html", usuario=usuario, trabajos=trabajos)
        else:
            flash("No existen Trabajos a cargo.", "error")
            return render_template("jurado/consulta_trabajo.html", usuario=usuario)



    def get_view_enviar_comentario(self,id_propuesta):
        codigo = session['usuario']['codigo']
        usuario = UsuarioDao().get_usuario_por_codigo(
            Usuario(codigo=codigo))
        propuesta = PropuestaDao().get_propuesta2(id_propuesta)
        return render_template("jurado/comentario.html", propuesta=propuesta,
                               usuario=usuario)


    def get_guardar_comentario(self, id_propuesta, comentario):
        com1 = PropuestaDao().get_comentarios(id_propuesta)
        codigo = session['usuario']['codigo']
        usuario = UsuarioDao().get_usuario_por_codigo(
            Usuario(codigo=codigo))
        p = PropuestaDao().get_propuesta_consulta_jurado(usuario)
        t = TrabajoGradoDao().get_trabajos_Jurado(usuario)
        if(com1 is None):
            com1=""
        va =PropuestaDao().get_guardar_comentario(id_propuesta,com1+";"+comentario)
        if (va):
            flash("Se ha enviado Exitosamente.", "success")

            return render_template('jurado/home.html', titulo="Inicio",
                                   usuario=usuario, propuestas=p, trabajos=t)
        flash("Ha ocurrido un error.","error")
        return render_template("jurado/consulta_trabajo.html", usuario=usuario,
                               trabajos=t)
