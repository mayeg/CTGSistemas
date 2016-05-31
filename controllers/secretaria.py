import hashlib
from _hashlib import new

from dao.acta_dao import ActaDao
from dao.tipo_usuario_dao import TipoUsuarioDao
from dao.usuario_dao import UsuarioDao
from dao.propuesta_dao import PropuestaDao
from dto.acta import Acta
from flask.helpers import flash, url_for
from flask import render_template, redirect, url_for, session
from dto.usuario import Usuario
from dto.propuesta import Propuesta


class SecretariaController:
    def __init__(self):
        pass

    def get_lista_jurados(self, pagina, codigo, nombres, cedula, apellidos,tipoU):
        usuarios = UsuarioDao().get_lista_usuarios(
            pagina, codigo, nombres, cedula, apellidos, tipoU)
        total_usuarios = UsuarioDao().get_total_usuarios(
            pagina, codigo, nombres, cedula, apellidos)
        total_paginas = (total_usuarios / 10) + 1
        return render_template("secretaria/listar.html", usuarios=usuarios,
                               total_paginas=total_paginas,
                               total_usuarios=total_usuarios)

    def get_registrar_jurado(self):
        usuario = {
            'codigo': "", 'nombres': "", 'apellidos': "", 'cedula': "",
            'contrasena': "", 'email': ""
        }
        tipoU = TipoUsuarioDao().get_nombre(session['usuario']['tipo'])
        usuario_u = Usuario(nombres=session['usuario']['nombres'])
        tipos = TipoUsuarioDao().listar_tipo_usuario()
        return render_template("secretaria/registroJ.html", usuario=usuario,
                               tipos=tipos, usuario_u=usuario_u, tipoU=tipoU)

    def crear_jurado(self, codigo, nombres, apellidos, cedula, email,
                          contrasena,
                          tipo_usuario):

        contrasena = hashlib.sha1(contrasena).hexdigest()
        usuario = Usuario(codigo=codigo, cedula=cedula, contrasena=contrasena,
                  nombres=nombres, apellidos=apellidos, email=email,
                  tipo_usuario=tipo_usuario)
        usuario_error = {
                'codigo': codigo, 'cedula': cedula, 'nombres': nombres,
                'apellidos': apellidos, 'email': email
                }
        if UsuarioDao().get_usuario_por_codigo(usuario) is not None:
            flash("Ya existe un usuario con el codigo {}.".format(
                usuario.getCodigo()), "error")
            tipos = TipoUsuarioDao().listar_tipo_usuario()
            return render_template("secretaria/registroJ.html",
                                   usuario=usuario_error, tipos=tipos)

        if UsuarioDao().crear_usuario(usuario):
            flash("El usuario se creo correctamente.", "success")
        else:
            flash("Error al registrar el usuario.", "error")
        return redirect(url_for("secretaria.listar_jurados"))

    def get_editar_jurado(self, id_usuario):
        print "id", id_usuario
        usuario = Usuario(id=id_usuario)
        usuario_e = UsuarioDao().get_usuario_por_id(usuario)
        usuario_edit = {
            'nombres': usuario_e.getNombres(),
            'apellidos': usuario_e.getApellidos(),
            'cedula': usuario_e.getCedula(),
            'email': usuario_e.getEmail(),
            'tipo_usuario': usuario_e.getTipoUsuario()
        }
        tipos = TipoUsuarioDao().listar_tipo_usuario()
        tipoU = TipoUsuarioDao().get_nombre(session['usuario']['tipo'])
        usuario_u = Usuario(nombres=session['usuario']['nombres'])
        if usuario_e is None:
            flash("El usuario que intenta editar no existe.", "error")
        return render_template(
            "secretaria/editar_jurado.html", usuario_edit=usuario_edit,
            id=id_usuario, tipos=tipos, usuario_u=usuario_u, tipoU=tipoU)

    def editar_usuario(self, nombres, apellidos, cedula, email, tipo_usuario,
                       id):

        usuario_e = Usuario(nombres=nombres, apellidos=apellidos, cedula=cedula,
                    email=email, tipo_usuario=tipo_usuario, id=id)

        if UsuarioDao().editar_usuario(usuario_e):
            flash("El usuario se edito correctamente.", "success")
        else:
            flash("Error al editar el usuario.", "error")
        return redirect(url_for("usuarios.listar_usuarios"))


    def get_view_registro(self):
        return render_template("secretaria/acta/RegistrarActa.html")

    def crear_acta(self,titulo,tipo,fecha,archivo,descripcion):

        acta = Acta(titulo=titulo, tipo=tipo, fecha=fecha,archivo=archivo,descripcion=descripcion)
        if(ActaDao().get_acta_titulo(acta)!= None):
            flash("Ya existe un acta con ese titulo {}.".format(
                acta.getTitulo()), "error")
            return render_template("secretaria/acta/RegistrarActa.html")

        if (ActaDao().crear_acta(acta)):
            flash("El acta se registro correctamente.", "success")
        else:
            flash("Error al registrar el acta.", "error")
        return render_template("secretaria/acta/RegistrarActa.html")

    def modificar_acta(self,titulo_acta,codigo, titulo, tipo, fecha, archivo, descripcion):

        acta = Acta(codigo=codigo,titulo=titulo, tipo=tipo, fecha=fecha,archivo=archivo,descripcion=descripcion)
        if (ActaDao().modificar_acta(titulo_acta,acta)):
            flash("Se ha modificado correctamente.", "success")
            return render_template("secretaria/acta/Descargar-ModificarActa.html")
        else:
            flash("Error modificar acta.", "error")
        return render_template("secretaria/acta/ModificarActa.html")


    def get_view_consulta(self):
        return render_template("secretaria/acta/ConsultarActa.html")


    def get_modificar(self,titulo):
        act = Acta("",titulo,"<-- No Selected -->","","","")
        acta = ActaDao().get_acta_consulta(act)
        return render_template("secretaria/acta/ModificarActa.html",acta=acta)


    def get_consulta(self,titulo,tipo,fecha):
        acta = Acta(titulo=titulo, tipo=tipo, fecha=fecha)
        actas = ActaDao().get_acta_consulta(acta)
        if(actas is not None):
            return render_template("secretaria/acta/ConsultarActa.html",actas=actas)
        else:
            flash("No existen Actas con esos parametros.","error")
        return render_template("secretaria/acta/ConsultarActa.html")


    def get_consulta_descarga(self,titulo,tipo,fecha):
        acta = Acta(titulo=titulo,tipo=tipo, fecha=fecha)
        actas = ActaDao().get_acta_consulta(acta)
        if (actas is not None):
            return render_template("secretaria/acta/Descargar-ModificarActa.html",
                                   actas=actas)
        else:
            flash("No existen Actas con esos parametros.", "error")
        return render_template("secretaria/acta/Descargar-ModificarActa.html")


    def get_view_descargar(self):
        return render_template("secretaria/acta/Descargar-ModificarActa.html")

    def get_descarga(self, titulo, tipo, fecha):
        acta = Acta(titulo=titulo, tipo=tipo, fecha=fecha)
        if (ActaDao.get_acta_consulta(acta) is not None):
            actas = ActaDao.get_acta_consulta(acta)
            return render_template("secretaria/acta/Descargar-ModificarActa.html",
                                   actas=actas)
        else:
            flash("No existen Actas con esos parametros.", "error")
        return render_template("secretaria/acta/Descargar-ModificarActa.html")






    def get_view_consultar_propuesta(self):
        return render_template("secretaria/propuesta/ConsultarPropuesta.html")

#CODIGO = ID
    def consultar_propuesta(self,titulo,codigo):
        propuesta = Propuesta(codigo=codigo,titulo=titulo)
        propuestas= PropuestaDao().get_propuesta_consulta(propuesta)
        if(propuestas is not None):
            return render_template("secretaria/propuesta/ConsultarPropuesta.html",
                                   propuestas=propuestas)
        else:
            flash("No existen Propuestas con esos parametros.", "error")
        return render_template("secretaria/propuesta/ConsultarPropuesta.html")






    def get_modificar_estado_propuesta(self,codigo_propuesta):
        propuest = Propuesta(codigo=codigo_propuesta)
        propuesta= PropuestaDao().get_propuesta_codigo(propuest)
        return render_template("secretaria/propuesta/ModificarEstado.html",propuesta=propuesta)

    def modificar_estado_propuesta(self,codigo_propuesta,estado):
        propuesta= Propuesta(codigo=codigo_propuesta,estado=estado)
        if(PropuestaDao().modificar_estado(propuesta)):
            flash("Se ha modificado exitosamente el estado.","success")
            return render_template("secretaria/propuesta/ConsultarPropuesta.html")
        else:
            flash("No se ha podido modificar el estado.","error")
        return render_template("secretaria/propuesta/ConsultarPropuesta.html")





    def get_agregar_fechas_propuesta(self,codigo_propuesta):
        propuest = Propuesta(codigo=codigo_propuesta)
        propuesta = PropuestaDao().get_propuesta_codigo(propuest)
        return render_template("secretaria/propuesta/AgregarFechas.html", propuesta=propuesta)

    def modificar_fechas_propuesta(self,codigo_propuesta,fechaCorrecciones,fechaComentarios):
        propuesta= Propuesta(codigo=codigo_propuesta,fecha_comentario=fechaComentarios,fecha_correcciones=fechaCorrecciones)
        if(PropuestaDao().modificar_fechas(propuesta)):
            flash("Se han modificado las fechas exitosamente.", "success")
            return render_template("secretaria/propuesta/ConsultarPropuesta.html")
        else:
            flash("No se ha podido modificar las fechas.", "error")
        return render_template("secretaria/propuesta/ConsultarPropuesta.html")


    def get_habilitar_envio_entregables(self,codigo_propuesta):
        propuest = Propuesta(codigo=codigo_propuesta)
        propuesta = PropuestaDao().get_propuesta_codigo(propuest)
        return render_template("secretaria/propuesta/HabilitarEnvioEntregables.html", propuesta=propuesta)


    def habilitar_envio_entregables(self,codigo_propuesta,entregable):
        propuesta=Propuesta(codigo=codigo_propuesta,entegrables=entregable)
        if (PropuestaDao().habilitar_envio_entregables(propuesta)):
            flash("Se han ingresado las fechas exitosamente.", "success")
            return render_template("secretaria/propuesta/ConsultarPropuesta.html")
        else:
            flash("No se ha podido ingresar las fechas.", "error")
        return render_template("secretaria/propuesta/ConsultarPropuesta.html")
