from flask.blueprints import Blueprint
from flask import request, redirect, url_for
from flask.globals import session
from controllers.login import Login
from controllers.usuario import UsuarioController

login_r = Blueprint("login", __name__)


@login_r.route("/", methods=["POST"])
def login():
    codigo = request.form.get('codigo', None)
    contrasena = request.form.get('contrasena', None)
    Login().login(codigo, contrasena)
    return redirect(url_for("login.get_home"))


@login_r.route("/", methods=["GET"])
def get_home():
    return Login().get_home_usuario()


@login_r.route("/logout", methods=["GET"])
def logout():
    Login().logout()
    return redirect(url_for("login.get_home"))


@login_r.route("/cambiar_contrasena/<token>/", methods=["GET", "POST"])
@login_r.route("/cambiar_contrasena/", methods=["GET", "POST"])
def recordar_contrasena(token=None):
    if token:
        if request.method == "GET":
            res = Login().get_cambiar_contrasena(token)
            if not res:
                return redirect(url_for("login.get_home"))
            return res
        else:
            contrasena_1 = request.form.get("contrasena", None)
            contrasena_2 = request.form.get("contrasena2", None)
            Login().cambiar_contrasena_olvidada(
                contrasena_1, contrasena_2, token)
            return redirect(url_for("login.get_home"))
    else:
        if request.method == "GET":
            return Login().get_recordar_contrasena()
        else:
            codigo = request.form.get('codigo', None)
            Login().recordar_contrasena(codigo)
            return redirect(url_for("login.get_home"))

@login_r.route("/registrar", methods=["GET", "POST"])
def registro_estudiante():
    if request.method == "GET":
        return UsuarioController().get_registro()
    codigo = request.form.get('codigo', None)
    nombres = request.form.get('nombres', None)
    apellidos = request.form.get('apellidos', None)
    cedula = request.form.get('cedula', None)
    email = request.form.get('email', None)
    contrasena = request.form.get('contrasena', None)
    tipo_usuario = "5"
    return UsuarioController().crear_usuario(codigo,
                                             nombres, apellidos, cedula, email,
                                             contrasena, tipo_usuario)