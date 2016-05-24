from flask.blueprints import Blueprint
from flask import request, session
from controllers.usuario import UsuarioController

usuario = Blueprint("usuarios", __name__)


@usuario.route("/", methods=["GET"])
def listar_usuarios():
    pagina = request.args.get('pagina', 1)
    codigo = request.args.get('codigo', "")
    nombre = request.args.get('nombres', "")
    cedula = request.args.get('cedula', "")
    apellidos = request.args.get('apellidos', "")
    return UsuarioController().get_lista_usuarios(
        pagina, codigo, nombre, cedula, apellidos)


@usuario.route("/registro", methods=["GET", "POST"])
def registro_usuario():
    if request.method == "GET":
        return UsuarioController().get_registro()
    codigo = request.form.get('codigo', None)
    nombres = request.form.get('nombres', None)
    apellidos = request.form.get('apellidos', None)
    cedula = request.form.get('cedula', None)
    email = request.form.get('email', None)
    contrasena = request.form.get('contrasena', None)
    tipo_usuario = request.form.get('tipo_usuario', 0)
    return UsuarioController().crear_usuario(codigo,
        nombres, apellidos, cedula, email, contrasena, tipo_usuario)


@usuario.route("/eliminar/<id_usuario>", methods=["GET"])
def eliminar_usuario(id_usuario):
    return UsuarioController().eliminar_usuario(id_usuario)


@usuario.route("/editar/<id_usuario>", methods=["GET", "POST"])
def editar_usuario(id_usuario):
    if request.method == "GET":
        return UsuarioController().get_editar_usuario(id_usuario)
    nombres = request.form.get('nombres', None)
    apellidos = request.form.get('apellidos', None)
    cedula = request.form.get('cedula', None)
    email = request.form.get('email', None)
    tipo_usuario = request.form.get('tipo_usuario', 0)
    id = id_usuario
    return UsuarioController().editar_usuario(nombres, apellidos, cedula,
                                              email, tipo_usuario, id)

@usuario.route("/configuracion", methods=["GET", "POST"])
def cambiar_contrasena():
    if request.method == "GET":
        return UsuarioController().get_cambiar_contrasena()
    contrasena_a = request.form.get('contrasena_a', None)
    contrasena_n = request.form.get('contrasena_n', None)
    contrasena_nc = request.form.get('contrasena_nc', None)
    return UsuarioController().cambiar_contrasena(contrasena_a,
                                                  contrasena_n, contrasena_nc)

