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
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        return render_template("secretaria/acta/RegistrarActa.html",usuario=usuario)

    def crear_acta(self,titulo,tipo,fecha,archivo,descripcion):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        acta = Acta(titulo=titulo, tipo=tipo, fecha=fecha,archivo=archivo,descripcion=descripcion)
        if(ActaDao().get_acta_titulo(acta)!= None):
            flash("Ya existe un acta con ese titulo {}.".format(
                acta.getTitulo()), "error")
            return render_template("secretaria/acta/RegistrarActa.html",usuario=usuario)

        if (ActaDao().crear_acta(acta)):
            flash("El acta se registro correctamente.", "success")
        else:
            flash("Error al registrar el acta.", "error")
        return render_template("secretaria/acta/RegistrarActa.html",usuario=usuario)




    def modificar_acta(self,titulo_acta,codigo, titulo, tipo, fecha, archivo, descripcion):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        acta = Acta(codigo=codigo,titulo=titulo, tipo=tipo, fecha=fecha,archivo=archivo,descripcion=descripcion)
        if (ActaDao().modificar_acta(titulo_acta,acta)):
            flash("Se ha modificado correctamente.", "success")
            return render_template("secretaria/acta/Descargar-ModificarActa.html",usuario=usuario)
        else:
            flash("Error modificar acta.", "error")
        return render_template("secretaria/acta/ModificarActa.html",usuario=usuario)




    def get_view_consulta(self):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        return render_template("secretaria/acta/ConsultarActa.html",usuario=usuario)



    def get_modificar(self,titulo):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        act = Acta(titulo=titulo,tipo="<-- No Selected -->")
        acta = ActaDao().get_acta_consulta(act)
        return render_template("secretaria/acta/ModificarActa.html",acta=acta,usuario=usuario)



    def get_consulta(self,titulo,tipo,fecha):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        acta = Acta(titulo=titulo, tipo=tipo, fecha=fecha)
        actas = ActaDao().get_acta_consulta(acta)
        if(actas is not None):
            return render_template("secretaria/acta/ConsultarActa.html",actas=actas,usuario=usuario)
        else:
            flash("No existen Actas con esos parametros.","error")
        return render_template("secretaria/acta/ConsultarActa.html",usuario=usuario)


    def get_consulta_descarga(self,titulo,tipo,fecha):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        acta = Acta(titulo=titulo,tipo=tipo, fecha=fecha)
        actas = ActaDao().get_acta_consulta(acta)
        if (actas is not None):
            return render_template("secretaria/acta/Descargar-ModificarActa.html", actas=actas,usuario=usuario)
        else:
            flash("No existen Actas con esos parametros.", "error")
        return render_template("secretaria/acta/Descargar-ModificarActa.html",usuario=usuario)





    def get_view_descargar(self):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        return render_template("secretaria/acta/Descargar-ModificarActa.html",usuario=usuario)




    def get_descarga(self, titulo, tipo, fecha):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        acta = Acta(titulo=titulo, tipo=tipo, fecha=fecha)
        if (ActaDao.get_acta_consulta(acta) is not None):
            actas = ActaDao.get_acta_consulta(acta)
            return render_template("secretaria/acta/Descargar-ModificarActa.html", actas=actas)
        else:
            flash("No existen Actas con esos parametros.", "error")
        return render_template("secretaria/acta/Descargar-ModificarActa.html")






    def get_view_consultar_propuesta(self):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        return render_template("secretaria/propuesta/ConsultarPropuesta.html",usuario=usuario)

#CODIGO = ID
    def consultar_propuesta(self,titulo,codigo):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        propuesta = Propuesta(codigo=codigo,titulo=titulo)
        propuestas= PropuestaDao().get_propuesta_consulta(propuesta)
        if(propuestas is not None):
            return render_template("secretaria/propuesta/ConsultarPropuesta.html", propuestas=propuestas,usuario=usuario)
        else:
            flash("No existen Propuestas con esos parametros.", "error")
        return render_template("secretaria/propuesta/ConsultarPropuesta.html",usuario=usuario)






    def get_modificar_estado_propuesta(self,codigo_propuesta):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        propuest = Propuesta(codigo=codigo_propuesta)
        propuesta= PropuestaDao().get_propuesta_codigo(propuest)
        return render_template("secretaria/propuesta/ModificarEstado.html",propuesta=propuesta,usuario=usuario)

    def modificar_estado_propuesta(self,codigo_propuesta,estado):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        propuesta= Propuesta(codigo=codigo_propuesta,estado=estado)
        if(PropuestaDao().modificar_estado(propuesta)):
            flash("Se ha modificado exitosamente el estado.","success")
            return render_template("secretaria/propuesta/ConsultarPropuesta.html",usuario=usuario)
        else:
            flash("No se ha podido modificar el estado.","error")
        return render_template("secretaria/propuesta/ConsultarPropuesta.html",usuario=usuario)





    def get_agregar_fechas_propuesta(self,codigo_propuesta):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        propuest = Propuesta(codigo=codigo_propuesta)
        propuesta = PropuestaDao().get_propuesta_codigo(propuest)
        return render_template("secretaria/propuesta/AgregarFechas.html", propuesta=propuesta,usuario=usuario)

    def modificar_fechas_propuesta(self,codigo_propuesta,fechaCorrecciones,fechaComentarios,fechaEntregables):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        propuesta= Propuesta(codigo=codigo_propuesta,fecha_comentario=fechaComentarios,
                             fecha_correcciones=fechaCorrecciones,fecha_entregables=fechaEntregables)
        if(PropuestaDao().modificar_fechas(propuesta)):
            flash("Se han modificado las fechas exitosamente.", "success")
            return render_template("secretaria/propuesta/ConsultarPropuesta.html",usuario=usuario)
        else:
            flash("No se ha podido modificar las fechas.", "error")
        return render_template("secretaria/propuesta/ConsultarPropuesta.html",usuario=usuario)


    def get_habilitar_envio_entregables(self,codigo_propuesta):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        propuest = Propuesta(codigo=codigo_propuesta)
        propuesta = PropuestaDao().get_propuesta_codigo(propuest)
        return render_template("secretaria/propuesta/HabilitarEnvioEntregables.html", propuesta=propuesta,usuario=usuario)


    def habilitar_envio_entregables(self,codigo_propuesta,entregable):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        propuesta=Propuesta(codigo=codigo_propuesta,entegrables=entregable)
        if (PropuestaDao().habilitar_envio_entregables(propuesta)):
            flash("Se han ingresado las fechas exitosamente.", "success")
            return render_template("secretaria/propuesta/ConsultarPropuesta.html",usuario=usuario)
        else:
            flash("No se ha podido ingresar las fechas.", "error")
        return render_template("secretaria/propuesta/ConsultarPropuesta.html",usuario=usuario)






    def get_view_asignar_jurado_propuesta(self):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        propuestas = PropuestaDao().get_propuesta_sin_jurado()
        jurados = UsuarioDao().get_jurados(4)
        return render_template("secretaria/propuesta/AsignarJuradosPropuesta.html",propuestas=propuestas,jurados=jurados,usuario=usuario)


    def asignar_jurado_propuesta(self,propuesta,jurado1,jurado2,jurado3):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        propuestaDividida=propuesta.split('-')
        jurado1Dividido= jurado1.split('-')
        jurado2Dividido= jurado2.split('-')
        jurado3Dividido= jurado3.split('-')
        if(PropuestaDao().asignar_jurados(propuestaDividida[0],jurado1Dividido[1],jurado2Dividido[1],jurado3Dividido[1])):
            flash("Se han asignado exitosamente los Jurados a la Propuesta.","success")
            return render_template("secretaria/propuesta/AsignarJuradosPropuesta.html",usuario=usuario)
        else:
            flash("No se han podido asignar Jurados.","error")
        return render_template("secretaria/propuesta/AsignarJuradosPropuesta.html",usuario=usuario)





    def get_view_consultar_trabajo_de_grado(self):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        return render_template("secretaria/trabajoGrado/ConsultarTrabajoGrado.html",usuario=usuario)

    def consultar_trabajo_de_grado(self,titulo,codigo):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        trabaj=TrabajoGrado(titulo=titulo,codigo=codigo)
        trabajos=TrabajoGradoDao().consultar_trabajos(trabaj)
        return render_template("secretaria/trabajoGrado/ConsultarTrabajoGrado.html",trabajos=trabajos,usuario=usuario)





    def get_view_registrar_nota(self,codigo_trabajo):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        trabajo= TrabajoGradoDao().get_trabajo_codigo(codigo_trabajo)
        return render_template("secretaria/trabajoGrado/RegistrarNota.html", trabajo=trabajo,usuario=usuario)

    def registrar_nota(self,codigo_trabajo,nota):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        trabajo = TrabajoGrado(codigo=codigo_trabajo,nota=nota)
        if(TrabajoGradoDao().registrar_nota(trabajo)):
            flash("Se ha registrado la Nota exitosamente.","success")
            return render_template("secretaria/trabajoGrado/ConsultarTrabajoGrado.html",usuario=usuario)
        else:
            flash("No se ha podido registrar Nota","error")
        return render_template("secretaria/trabajoGrado/ConsultarTrabajoGrado.html",usuario=usuario)





    def get_view_agregar_fechas_trabajo(self,codigo_trabajo):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        trabajo = TrabajoGradoDao().get_trabajo_codigo(codigo_trabajo)
        return render_template("secretaria/trabajoGrado/AgregarFechas.html", trabajo=trabajo,usuario=usuario)

    def agregar_fechas_trabajo(self,codigo_trabajo,fechaCorrecciones):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        trabajo= TrabajoGrado(codigo=codigo_trabajo,fecha_correcciones=fechaCorrecciones)
        if(TrabajoGradoDao().agregar_fechas_correcciones(trabajo)):
            flash("Se ha registrado las Fechas exitosamente.","success")
            return render_template("secretaria/trabajoGrado/ConsultarTrabajoGrado.html",usuario=usuario)
        else:
            flash("No se ha podido registrar Fechas.","error")
        return render_template("secretaria/trabajoGrado/ConsultarTrabajoGrado.html",usuario=usuario)


    def get_view_agregar_datos_sustentacion(self):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        trabajos = TrabajoGradoDao().get_trabajos_sin_sustentacion()
        return render_template("secretaria/trabajoGrado/AgregarDatosSustentacion.html",trabajos=trabajos,usuario=usuario)

    def agregar_datos_sustentacion(self,trabajo,lugar,fecha,hora):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        trabajoDividido= trabajo.split('-')
        trab=TrabajoGrado(codigo=trabajoDividido[1],lugar_sustentacion=lugar,fecha_sustentacion=fecha,hora_sustentacion=hora)
        if(TrabajoGradoDao().agregar_datos_sustentacion(trab)):
            flash("Se han agregado los datos exitosamente","success")
            return render_template("secretaria/home.html",usuario=usuario)
        else:
            flash("No se han podido agregar datos","error")
        return render_template("secretaria/home.html",usuario=usuario)



    def get_view_asignar_jurado_trabajo(self):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        trabajos=TrabajoGradoDao().get_trabajos_sin_jurados()
        jurados = UsuarioDao().get_jurados(4)
        return render_template("secretaria/trabajoGrado/AsignarJuradosTrabajo.html",trabajos=trabajos,jurados=jurados,usuario=usuario)

    def asignar_jurado_trabajo(self,trabajo,jurado1,jurado2,jurado3):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        trabajoDividido = trabajo.split('-')
        jurado1Dividido = jurado1.split('-')
        jurado2Dividido = jurado2.split('-')
        jurado3Dividido = jurado3.split('-')
        if (TrabajoGradoDao().asignar_jurados_trabajo(trabajoDividido[0], jurado1Dividido[1], jurado2Dividido[1],
                                           jurado3Dividido[1])):
            flash("Se han asignado exitosamente los Jurados a la Propuesta.", "success")
            return render_template("secretaria/home.html",usuario=usuario)
        else:
            flash("No se han podido asignar Jurados.", "error")
        return render_template("secretaria/home.html",usuario=usuario)



    def get_view_registrar_protocolo(self):
        cod = session['usuario']['codigo']
        usuario = Usuario(nombres=session['usuario']['nombres'], codigo=cod)
        return render_template("secretaria/protocolo/SubirArchivo.html",usuario=usuario)

    def get_actas(self):
        actas = ActaDao().get_actas()
        return actas
