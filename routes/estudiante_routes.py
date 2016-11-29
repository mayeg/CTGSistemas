import os

from flask.blueprints import Blueprint
from flask import request, session, app
from flask.globals import current_app
from flask.helpers import flash, send_from_directory
from werkzeug.utils import redirect
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
    file = request.files['documento']
    if file.filename == '':
        flash('No selecciono el archivo', 'Error')
        return redirect(request.url)
    id = session['usuario']['id']
    return EstudianteController().registrar_propuesta(
        titulo, director, modalidad, file, id)


@estudiante.route("/asignar_estudiante", methods=["POST"])
def asignar_estudiante():
    if request.method == "POST":
        codigo = request.form.get('codigo_estudiante', None)
        print request.form.get('codigo_estudiante', None), 'desde routes'
        return EstudianteController().asignar_propuesta(codigo)


@estudiante.route("/subir/entregables", methods=["GET", "POST"])
def subir_entregables():
    if request.method == "GET":
        return EstudianteController().get_subir_entregable()
    file = request.files['documento']
    id = session['usuario']['id']
    if file.filename == '':
        flash('No selecciono el archivo', 'Error')
        return redirect(request.url)
    return EstudianteController().subir_entregable(file, id)

@estudiante.route("/subir/correcciones", methods=["GET", "POST"])
def subir_correcciones():
    if request.method == "GET":
        return EstudianteController().get_subir_correciones()
    file = request.files['documento']
    id = session['usuario']['id']
    if file.filename == '':
        flash('No selecciono el archivo', 'Error')
        return redirect(request.url)
    return EstudianteController().subir_correcciones(file, id)


@estudiante.route("/solicitud/sustentacion", methods=["GET", "POST"])
def solicitar_sustentacion():
    if request.method == "GET":
        return EstudianteController().get_solicitar_sustentacion()
    file = request.files['documento']
    id = session['usuario']['id']
    if file.filename == '':
        flash('No selecciono el archivo', 'Error')
        return redirect(request.url)
    return EstudianteController().solicitar_sustentacion(file, id)


@estudiante.route("/solicitud/retiro_propuesta", methods=["GET", "POST"])
def solicitar_retiro_propuesta():
    if request.method == "GET":
        return EstudianteController().get_solicitar_retiro_propuesta()
    file = request.files['documento']
    id = session['usuario']['id']
    if file.filename == '':
        flash('No selecciono el archivo', 'Error')
        return redirect(request.url)
    return EstudianteController().solicitar_retiro(file, id)

@estudiante.route("/solicitud/prorroga", methods=["GET", "POST"])
def solicitar_prorroga():
    if request.method == "GET":
        return EstudianteController().get_solicitar_prorroga()
    else:
        file = request.files['documento']
        id = session['usuario']['id']
        if file.filename == '':
            flash('No selecciono el archivo', 'Error')
            return redirect(request.url)
        return EstudianteController().solicitar_prorroga(file, id)

@estudiante.route("/protocolos", methods=["GET", "POST"])
def protocolos():
    if request.method == "GET":
        return EstudianteController().get_protocolos()

@estudiante.route("/descargar/<filename>", methods=["POST"])
def descargar_propuesta(filename):
    print('entro a routes')
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename)


