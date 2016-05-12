# -*- coding: utf-8 -*-
import hashlib

from flask import session, render_template

from dao.usuario_dao import UsuarioDao
from dto.usuario import Usuario


class Login:

    def __init__(self):
        pass

    @staticmethod
    def get_home_usuario():
        if 'usuario' in session:
            return render_template('home/home.html', titulo="Inicio")
        return render_template('login/login.html')

    def login(self, codigo, contrasena):
        contrasena_c = hashlib.sha1(contrasena).hexdigest()
        usuario = Usuario(codigo=codigo, contrasena=contrasena_c)
        usuario_logueado = UsuarioDao().get_user_login(usuario)
        if usuario_logueado is not None:
            session['usuario'] = usuario_logueado.get_dict()
            print session

    def logout(self):
        del session['usuario']

    @staticmethod
    def get_login():
        return render_template('login/login.html', list=['hola', 'carlos'], titulo="mi titulo")
