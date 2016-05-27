
# -*- coding: utf-8 -*-
import hashlib

from flask.helpers import flash

from dao.tipo_usuario_dao import TipoUsuarioDao
from dao.usuario_dao import UsuarioDao
from flask import render_template, redirect, url_for, session
from dto.tipo_usuario import TipoUsuario
from dto.usuario import Usuario


class UsuarioController:
    def __init__(self):
        pass

    def get_lista_usuarios(self, pagina, codigo, nombres, cedula, apellidos):
        usuarios = UsuarioDao().get_lista_usuarios(
            pagina, codigo,  nombres, cedula, apellidos)
        total_usuarios = UsuarioDao().get_total_usuarios(
            pagina, codigo, nombres, cedula, apellidos)
        total_paginas = (total_usuarios / 10) + 1
        return render_template("usuarios/listar.html", usuarios=usuarios,
                               total_paginas=total_paginas,
                               total_usuarios=total_usuarios)

    def get_registrar_jurado(self):
        usuario = {
            'codigo':"", 'nombres': "", 'apellidos': "", 'cedula': "",
            'contrasena': "", 'email': ""
        }
        tipos = TipoUsuarioDao().listar_tipo_usuario()
        return render_template("secretaria/registroJ.html", usuario=usuario,
                               tipos=tipos)

    def get_registro(self):
        usuario = {
            'codigo': "", 'nombres': "", 'apellidos': "", 'cedula': "",
            'contrasena': "", 'email': ""
        }
        tipos = TipoUsuarioDao().listar_tipo_usuario()
        return render_template("usuarios/registro.html", usuario=usuario,
                               tipos=tipos)

    def crear_usuario(self, codigo, nombres, apellidos, cedula, email, contrasena,
                      tipo_usuario):
        contrasena = hashlib.sha1(contrasena).hexdigest()
        usuario = Usuario(codigo=codigo, cedula=cedula, contrasena=contrasena,
                          nombres=nombres, apellidos=apellidos, email=email,
                          tipo_usuario=tipo_usuario)
        usuario_error = {
            'codigo':codigo, 'cedula': cedula, 'nombres': nombres,
            'apellidos': apellidos, 'email': email
        }
        if UsuarioDao().get_usuario_por_codigo(usuario) is not None:
            flash("Ya existe un usuario con el codigo {}.".format(
                usuario.getCodigo()), "error")
            tipos = TipoUsuarioDao().listar_tipo_usuario()
            return render_template(
                "usuarios/registro.html", usuario=usuario_error, tipos=tipos)

        if UsuarioDao().crear_usuario(usuario):
            flash("El usuario se creo correctamente.", "success")
        else:
            flash("Error al registrar el usuario.", "error")
        return redirect(url_for("usuarios.listar_usuarios"))

    def eliminar_usuario(self, id_usuario):
        usuario = Usuario(id=id_usuario)
        if UsuarioDao().get_usuario_por_id(usuario) is None:
            flash("El usuario que intenta eliminar no existe.", "error")
        else:
            if UsuarioDao().eliminar_usuario(usuario):
                flash("El usuario ha sido eliminado.", "success")
            else:
                flash("El usuario no se pudo eliminar.", "error")
        return redirect(url_for("usuarios.listar_usuarios"))

    def get_editar_usuario(self, id_usuario):
        usuario = Usuario(id=id_usuario)
        usuario_e = UsuarioDao().get_usuario_por_id(usuario)
        usuario_edit = {
            'nombres': usuario_e.getNombres(),
            'apellidos': usuario_e.getApellidos(),
            'cedula': usuario_e.getCedula(), 'email': usuario_e.getEmail(),
            'tipo_usuario': usuario_e.getTipoUsuario()
        }
        tipos = TipoUsuarioDao().listar_tipo_usuario()
        if usuario_e is None:
            flash("El usuario que intenta editar no existe.", "error")
        return render_template(
            "usuarios/editar.html", usuario_edit=usuario_edit, id=id_usuario,
            tipos=tipos)

    def editar_usuario(self, nombres, apellidos, cedula, email, tipo_usuario,
                       id):
        usuario_e = Usuario(nombres=nombres, apellidos=apellidos, cedula=cedula,
                            email=email, tipo_usuario=tipo_usuario, id=id)

        if UsuarioDao().editar_usuario(usuario_e):
            flash("El usuario se edito correctamente.", "success")
        else:
            flash("Error al editar el usuario.", "error")
        return redirect(url_for("usuarios.listar_usuarios"))

    def get_cambiar_contrasena_jurado(self):
        tipo = session['usuario']['tipo']
        usuario = Usuario(nombres=session['usuario']['nombres'],
                          tipo_usuario=tipo)
        return render_template("jurado/configuracion.html", usuario=usuario)

    def get_cambiar_contrasena_secretaria(self):
        return render_template("secretaria/configuracion.html")

    def get_cambiar_contrasena_coordinador(self):
        return render_template("coordinador/configuracion.html")

    def get_cambiar_contrasena_estudiante(self):
        return render_template("estudiante/configuracion.html")

    def cambiar_contrasena(self, contrasena_a, contrasena_n,
                           contrasena_nc):
        id = session['usuario']['id']
        contrasena_c = hashlib.sha1(contrasena_a).hexdigest()
        usuario = Usuario(id=id)
        usuario_e = UsuarioDao().get_usuario_por_id(usuario)
        if usuario_e is not None:
            if usuario_e.getContrasena() == contrasena_c:
                if contrasena_n == contrasena_nc:
                    contrasena_cn = hashlib.sha1(contrasena_n).hexdigest()
                    if UsuarioDao().cambiar_contrasena(usuario_e,
                                                       contrasena_cn):
                        flash("Se cambio la contrasena correctamente.",
                              "success")
                    else:
                        flash("Error al cambiar la contrasena.", "error")
                else:
                    flash("Las contrasenas no coinciden.", "error")
                return redirect(url_for("usuarios.cambiar_contrasena"))
            else:
                flash("Las contrasenas no coinciden con la actual.", "error")
            return redirect(url_for("usuarios.cambiar_contrasena"))
        else:
            del session['usuario']
            return render_template("login/login")