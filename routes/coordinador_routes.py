from flask.blueprints import Blueprint
from flask import request, session

from controllers.coordinador import CoordinadorController
from controllers.login import Login
from controllers.usuario import UsuarioController

coordinador = Blueprint("coordinador", __name__)

@coordinador.route("/home", methods=["GET"])
def home():
        return Login().get_home_usuario()

@coordinador.route("/configuracion", methods=["GET", "POST"])
def cambiar_contrasena():
    if request.method == "GET":
        return UsuarioController().get_cambiar_contrasena_coordinador()
    contrasena_a = request.form.get('contrasena_a', None)
    contrasena_n = request.form.get('contrasena_n', None)
    contrasena_nc = request.form.get('contrasena_nc', None)
    return UsuarioController().cambiar_contrasena(contrasena_a,
                                                  contrasena_n, contrasena_nc)

@coordinador.route("/nombreT", methods=["GET", "POST"])
def consultar_trabajoN():

    if request.method == "GET":
        return CoordinadorController().get_view_nombreT()

    nombre_a = request.form.get('nombre_a', None)
    return CoordinadorController().consulta_nombreT(nombre_a)


@coordinador.route("/nombreP", methods=["GET", "POST"])
def consultar_propuestaM():
    if request.method == "GET":
        return CoordinadorController().get_view_nombreP()
    propuesta_a = request.form.get('propuesta_a', None)
    return CoordinadorController().consulta_nombreP(propuesta_a)


@coordinador.route("/cancelarP", methods=["GET", "POST"])
def cancelar_propuesta():
    if request.method == "GET":
        return CoordinadorController().get_view_cancelarP()
    propuesta_a = request.form.get('nombreP_c', None)
    estado_a = "Vencida"
    return CoordinadorController().consulta_cancelarP(propuesta_a, estado_a)


@coordinador.route("/estadoP", methods=["GET", "POST"])
def consultar_estado():
    if request.method == "GET":
        return CoordinadorController().get_view_estadoP()
    estado_a = request.form.get('estado', None)
    return CoordinadorController().consulta_estadoP(estado_a)


@coordinador.route("/juradoEstudiante", methods=["GET", "POST"])
def consultar_juradoEstudiante():
    if request.method == "GET":
        return CoordinadorController().get_view_juradoEstudiante()

    tipo_usuario = request.form.get('tipo_usuario', None)
    codigo_a = request.form.get('codigo_a', None)

    if (tipo_usuario == "Jurado"):

        return CoordinadorController().consulta_jurado(codigo_a)

    else:

        return CoordinadorController().consulta_estudiante(codigo_a)

@coordinador.route("/modalidadT", methods=["GET", "POST"])
def consultar_modalidad():
    if request.method == "GET":
        return CoordinadorController().get_view_modalidadT()
    tipo_modalidad = request.form.get('tipo_modalidad', None)
    trabajo_a = request.form.get('trabajo_a', None)
    return CoordinadorController().consulta_modalidadT(tipo_modalidad, trabajo_a )

@coordinador.route("/estadoT", methods=["GET", "POST"])
def consultar_estadoT():
    if request.method == "GET":
        return CoordinadorController().get_view_estadoT()
    estado = request.form.get('estado',None)
    trabajo_a = request.form.get('trabajo_a',None)
    return CoordinadorController().consulta_estadoT(estado, trabajo_a)

@coordinador.route("/consultarA", methods=["GET", "POST"])
def consultar_acta():

    if request.method == "GET":
        return CoordinadorController().get_view_consultarA()

    fecha_a = request.form.get('fecha', None)
    return CoordinadorController().consulta_actaC(fecha_a)

