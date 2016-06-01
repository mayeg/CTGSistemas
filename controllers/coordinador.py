from flask import render_template
from flask.helpers import flash

from dao.acta_dao import ActaDao
from dao.propuesta_dao import PropuestaDao
from dao.propuesta_usuario_dao import Propuesta_UsuarioDao
from dao.trabajoDeGrado_dao import TrabajoGradoDao
from dao.usuario_dao import UsuarioDao
from dto.propuesta import Propuesta
from dto.acta import Acta
from dto.trabajoGrado import TrabajoGrado
from dto.usuario import Usuario
from dto.usuario_propuesta import UsuarioPropuesta


class CoordinadorController:
    def __init__(self):
        pass

    def get_view_nombreT(self):
        return render_template("/coordinador/nombreT.html")

    def consulta_nombreT(self, nombre):
        trabajoG = TrabajoGrado(titulo=nombre)
        if (TrabajoGradoDao().get_trabajo_tituloT(trabajoG) is not None):
         trabajos = TrabajoGradoDao().get_trabajo_tituloT(trabajoG)
         return render_template("/coordinador/nombreT.html", trabajos=trabajos)
        else:
         flash("No existen Trabajos con esos parametros.", "error")
         return render_template("/coordinador/nombreT.html")

    def get_view_nombreP(self):
        return render_template("/coordinador/nombreP.html")

    def consulta_nombreP(self, nombre):
        propuesta = Propuesta(titulo=nombre)
        if (PropuestaDao().get_propuesta_consultaN):
            propuestas = PropuestaDao().get_propuesta_consultaN(propuesta)

            return render_template("/coordinador/nombreP.html", propuestas=propuestas)
        else:
            flash("No existen Propuestas con esos parametros.", "error")
            return render_template("/coordinador/nombreP.html")

    def get_view_cancelarP(self):
        return render_template("/coordinador/cancelarP.html")

    def consulta_cancelarP(self, nombre, estado):
        propuesta = Propuesta(titulo=nombre, estado=estado)

        if (PropuestaDao().get_propuesta_titulo(propuesta)is not None):
            PropuestaDao().get_propuesta_cancelar(propuesta, estado)
            flash("Actualiacion Exitosa", "success")
            return render_template("/coordinador/cancelarP.html")
        else:
            flash("No existen Propuesta con esos parametros.", "error")
            return render_template("/coordinador/cancelarP.html")

    def get_view_estadoP(self):
            return render_template("/coordinador/estadoP.html")

    def consulta_estadoP(self, estado):

        propuesta = Propuesta(estado=estado)
        if (PropuestaDao().get_propuesta_estado(propuesta)):
            propuestas = PropuestaDao().get_propuesta_estado(propuesta)
            return render_template("/coordinador/estadoP.html", propuestas=propuestas)
        else:
            flash("No existen Propuestas con esos parametros.", "error")
            return render_template("/coordinador/estadoP.html")

    def get_view_juradoEstudiante(self):
        return render_template("/coordinador/juradoEstudiante.html")

    def consulta_jurado(self, cod_jurado1):
        trabajoG= TrabajoGrado (cod_jurado1=cod_jurado1)
        if (TrabajoGradoDao().get_trabajo_Jurado(trabajoG) ):
            trabajos = TrabajoGradoDao().get_trabajo_Jurado(trabajoG)
            return render_template("/coordinador/juradoEstudiante.html", trabajos = trabajos)
        else:
            flash("No existen Trabajos con esos parametros.", "error")
            return render_template("/coordinador/juradoEstudiante.html")

    def consulta_estudiante(self, codigo_e):
        usuario = Usuario(codigo=codigo_e)
        usuario_e = UsuarioDao().get_usuario_por_codigo(usuario)
        if usuario_e is None:
            flash("El codigo del estudiante no existe.", "error")
            return render_template("/coordinador/juradoEstudiante.html")
        usuario_p = Propuesta_UsuarioDao().get_propuesta_usuario(UsuarioPropuesta(id_estudiante=usuario_e.getId()))
        if usuario_p is None:
            flash("El estudiante no tiene trabajos.", "error")
            return render_template("/coordinador/juradoEstudiante.html")

        trabajoG = TrabajoGrado(id_propuesta=usuario_p.getId_propuesta().getId())
        print trabajoG.getId_propuesta().getId()
        if TrabajoGradoDao().get_trabajo_Estudiante(trabajoG):
            trabajos = TrabajoGradoDao().get_trabajo_Estudiante(trabajoG)
            return render_template("/coordinador/juradoEstudiante.html", trabajos=trabajos)
        else:
            flash("No existen Trabajos con esos parametros.", "error")
            return render_template("/coordinador/juradoEstudiante.html")

    def get_view_modalidadT(self):
            return render_template("/coordinador/modalidadT.html")

    def consulta_modalidadT(self, tipo_modalidad, trabajo_a):

        trabajoG = TrabajoGrado(modalidad=tipo_modalidad)
        if (TrabajoGradoDao().get_trabajo_modalidadT(trabajoG , trabajo_a)):
            trabajos = TrabajoGradoDao().get_trabajo_modalidadT(trabajoG, trabajo_a)
            return render_template("/coordinador/modalidadT.html", trabajos=trabajos)
        else:
            flash("No existen Trabajos con esos parametros.", "error")
            return render_template("/coordinador/modalidadT.html")

    def get_view_consultarA(self):
            return render_template("/coordinador/consultarA.html")

    def consulta_actaC(self, fecha):

        acta = Acta(fecha=fecha)
        if (ActaDao().get_acta_fecha(acta)):
            actas = ActaDao().get_acta_fecha(acta)
            print "holaa poe aca 2"
            return render_template("/coordinador/consultarA.html", actas=actas)
        else:
            flash("No existen Actas con esos parametros.", "error")
            return render_template("/coordinador/consultarA.html")

    def get_view_estadoT(self):
            return render_template("/coordinador/estadoT.html")

    def consulta_estadoT(self, estado, trabajo_a):

        trabajoG = TrabajoGrado(estado=estado)
        if (TrabajoGradoDao().get_trabajo_estadoT(trabajoG, trabajo_a)):
            trabajos = TrabajoGradoDao().get_trabajo_estadoT(trabajoG, trabajo_a)
            return render_template("/coordinador/estadoT.html", trabajos=trabajos)
        else:
            flash("No existen Trabajos con esos parametros.", "error")
            return render_template("/coordinador/estadoT.html")
