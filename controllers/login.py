# -*- coding: utf-8 -*-
import hashlib

from flask import session, render_template

from dao.tipo_usuario_dao import TipoUsuarioDao
from dao.usuario_dao import UsuarioDao
from dto.usuario import Usuario


class Login:

    def __init__(self):
        pass

    @staticmethod
    def get_home_usuario(self, id):
        tipos = TipoUsuarioDao().listar_tipo_usuario()
        if 'usuario' in session:
            usuario = UsuarioDao.get_usuario_por_id(id)
            return render_template('home/home.html', titulo="Inicio",
                                   usuario=usuario)
        return render_template('login/login.html', tipos=tipos)

    def login(self, codigo, contrasena, tipo):
        contrasena_c = hashlib.sha1(contrasena).hexdigest()
        usuario = Usuario(codigo=codigo, contrasena=contrasena_c,
                          tipo_usuario=tipo)
        usuario_logueado = UsuarioDao().get_user_login(usuario)
        if usuario_logueado is not None:
            session['usuario'] = usuario_logueado.get_dict()
            print session

    def logout(self):
        del session['usuario']

