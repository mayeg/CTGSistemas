from flask.blueprints import Blueprint
from flask import request, redirect, url_for
from flask.globals import session

from controllers.login import Login

login_r = Blueprint("login", __name__)


@login_r.route("/", methods=["GET"])
def get_home():
    id = session['usuario']['id']
    return Login().get_home_usuario(id)


@login_r.route("/", methods=["POST"])
def login():
    codigo = request.form.get('codigo', None)
    contrasena = request.form.get('contrasena', None)
    tipo = request.form.get('tipo_usuario', 0)
    Login().login(codigo, contrasena, tipo)
    return redirect(url_for("login.get_home"))


@login_r.route("/logout", methods=["GET"])
def logout():
    Login().logout()
    return redirect(url_for("login.get_home"))