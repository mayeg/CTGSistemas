from flask.blueprints import Blueprint
from flask import request, session

from controllers.jurado import JuradoController
from controllers.login import Login
from controllers.usuario import UsuarioController

jurado = Blueprint("jurado", __name__)

@jurado.route("/home", methods=["GET"])
def home():
        return Login().get_home_usuario()

@jurado.route("/configuracion", methods=["GET", "POST"])
def cambiar_contrasena():
    if request.method == "GET":
        return UsuarioController().get_cambiar_contrasena_jurado()
    contrasena_a = request.form.get('contrasena_a', None)
    contrasena_n = request.form.get('contrasena_n', None)
    contrasena_nc = request.form.get('contrasena_nc', None)
    return UsuarioController().cambiar_contrasena(contrasena_a,
                                                  contrasena_n, contrasena_nc)

@jurado.route("/propuestas_cargo",methods=["GET", "POST"])
def consultar_propuestas():
    if request.method == "GET":
        return JuradoController().get_view_consultar_propuesta()


@jurado.route("/trabajos_cargo",methods=["GET", "POST"])
def consultar_trabajos():
    if request.method == "GET":
        return JuradoController().get_view_consultar_trabajo()

@jurado.route("/sustentaciones",methods=["GET", "POST"])
def consultar_sustentacion():
    if request.method == "GET":
        return JuradoController().get_view_consultar_sustentaciones()
