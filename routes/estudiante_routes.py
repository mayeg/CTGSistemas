from flask.blueprints import Blueprint
from flask import request, session

from controllers.login import Login
from controllers.usuario import UsuarioController

estudiante = Blueprint("estudiante", __name__)

@estudiante.route("/home", methods=["GET"])
def home():
        return Login().get_home_usuario()

@estudiante.route("/configuracion", methods=["GET", "POST"])
def cambiar_contrasena():
    if request.method == "GET":
        return UsuarioController().get_cambiar_contrasena_estudiante()
    contrasena_a = request.form.get('contrasena_a', None)
    contrasena_n = request.form.get('contrasena_n', None)
    contrasena_nc = request.form.get('contrasena_nc', None)
    return UsuarioController().cambiar_contrasena(contrasena_a,
                                                  contrasena_n, contrasena_nc)
