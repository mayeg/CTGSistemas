
from dao.acta_dao import ActaDao
from dao.tipo_usuario_dao import TipoUsuarioDao
from dao.usuario_dao import UsuarioDao
from dao.propuesta_dao import PropuestaDao
from dto.acta import Acta
from flask.helpers import flash, url_for
from flask import render_template, redirect, url_for, session
from dto.usuario import Usuario
from dto.propuesta import Propuesta

class JuradoController:
    def __init__(self):
        pass

    def get_view_consultar_propuesta(self):
        tipo = session['usuario']['tipo']
        usuario = Usuario(nombres=session['usuario']['nombres'],
                          tipo_usuario=tipo)
        return render_template("jurado/consulta_propuesta.html", usuario=usuario)

    def get_view_consultar_trabajo(self):
        tipo = session['usuario']['tipo']
        usuario = Usuario(nombres=session['usuario']['nombres'],
                          tipo_usuario=tipo)
        return render_template("jurado/consulta_trabajo.html", usuario=usuario)

    def get_view_consultar_sustentaciones(self):
        tipo = session['usuario']['tipo']
        usuario = Usuario(nombres=session['usuario']['nombres'],
                          tipo_usuario=tipo)
        return render_template("jurado/consulta_sustentacion.html", usuario=usuario)
