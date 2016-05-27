# -*- coding: utf-8 -*-
import hashlib

from flask import session, render_template, redirect, url_for

from dao.tipo_usuario_dao import TipoUsuarioDao
from dao.usuario_dao import UsuarioDao
from dto.usuario import Usuario


class Login:

    def __init__(self):
        pass

    @staticmethod
    def get_home_usuario():
        tipos = TipoUsuarioDao().listar_tipo_usuario()
        if 'usuario' in session:
            tipoU = session['usuario']['tipo']
            usuario_tipo = Usuario(tipo_usuario=tipoU)
            usuario = UsuarioDao().get_usuario_por_tipo(usuario_tipo)
            print usuario.getTipoUsuario().getId()
            if usuario.getTipoUsuario().getId() == 2:
                return render_template('secretaria/home.html', titulo="Inicio",
                                       usuario=usuario)
            elif usuario.getTipoUsuario().getId() == 3:
               return render_template('coordinador/home.html', titulo="Inicio",
                                       usuario=usuario)
            elif usuario.getTipoUsuario().getId() == 4:
                return render_template('jurado/home.html', titulo="Inicio",
                                      usuario=usuario)
            elif usuario.getTipoUsuario().getId() == 5:
                return render_template('estudiante/home.html', titulo="Inicio",
                                       usuario=usuario)

        return render_template('login/login.html', tipos=tipos)

    def login(self, codigo, contrasena, tipo):
        contrasena_c = hashlib.sha1(contrasena).hexdigest()
        usuario = Usuario(codigo=codigo, contrasena=contrasena_c,
                          tipo_usuario=tipo)
        usuario_logueado = UsuarioDao().get_user_login(usuario)
        if usuario_logueado is not None:
            session['usuario'] = usuario_logueado.get_dict()


    def logout(self):
        del session['usuario']

