from flask.blueprints import Blueprint
from flask import request, session

from controllers.estudiante import EstudianteController
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


@estudiante.route("/registro_propuesta", methods=["GET", "POST"])
def registro_propuesta():
    if request.method == "GET":
        return EstudianteController().get_registro_propuesta()
    titulo = request.form.get('titulo', None)
    director = request.form.get('director', None)
    modalidad = request.form.get('modalidad', None)
    documentos = request.form.get('docuementos', None)
    id = session['usuario']['id']
    return EstudianteController().registrar_propuesta(titulo, director,
                                                      modalidad, documentos, id)



