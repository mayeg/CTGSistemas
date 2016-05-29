from flask.blueprints import Blueprint
from flask import request, session
from controllers.login import Login
from controllers.secretaria import SecretariaController
from controllers.usuario import UsuarioController

secretaria = Blueprint("secretaria", __name__)

@secretaria.route("/home", methods=["GET"])
def home():
        return Login().get_home_usuario()

@secretaria.route("/configuracion", methods=["GET", "POST"])
def cambiar_contrasena():
    if request.method == "GET":
        return UsuarioController().get_cambiar_contrasena_secretaria()
    contrasena_a = request.form.get('contrasena_a', None)
    contrasena_n = request.form.get('contrasena_n', None)
    contrasena_nc = request.form.get('contrasena_nc', None)
    return UsuarioController().cambiar_contrasena(contrasena_a,
                                                  contrasena_n, contrasena_nc)
@secretaria.route("/registrar/jurado", methods=["GET", "POST"])
def registrar_jurados():
    if request.method == "GET":
        return UsuarioController().get_registrar_jurado()
    codigo = request.form.get('codigo', None)
    nombres = request.form.get('nombres', None)
    apellidos = request.form.get('apellidos', None)
    cedula = request.form.get('cedula', None)
    email = request.form.get('email', None)
    contrasena = request.form.get('contrasena', None)
    tipo_usuario = request.form.get('tipo_usuario', 0)
    return UsuarioController().crear_usuario(codigo,
                                             nombres, apellidos, cedula, email,
                                             contrasena, tipo_usuario)



@secretaria.route("/consultar_acta", methods=["GET","POST"])
def consultar_acta():
    if(request.method == "GET"):
        return SecretariaController().get_view_consulta()
    titulo = request.form.get('titulo',None)
    tipo = request.form.get('tipo',None)
    fecha = request.form.get('fecha',None)
    return SecretariaController().get_consulta(titulo,tipo,fecha)


@secretaria.route("/registrar_acta",methods=["GET","POST"])
def registro_acta():
    if(request.method == "GET"):
        return SecretariaController().get_view_registro()
    titulo = request.form.get('titulo',None)
    tipo = request.form.get('tipo',None)
    fecha = request.form.get('fecha',None)
    archivo = request.form.get('archivo', None)
    descripcion = request.form.get('descripcion',None)
    return SecretariaController().crear_acta(titulo,tipo,fecha,archivo,descripcion)

@secretaria.route("/descargar-modificar_acta",methods=["GET","POST"])
def descargar_modificar_acta():
    if(request.method == "GET"):
        return SecretariaController().get_view_descargar()
    titulo = request.form.get('titulo', None)
    tipo = request.form.get('tipo', None)
    fecha = request.form.get('fecha', None)
    return SecretariaController().get_consulta_descarga(titulo, tipo, fecha)

@secretaria.route("/modificar/<titulo_acta>", methods=["GET","POST"])
def modificar_acta(titulo_acta):
    if(request.method== "GET"):
        return SecretariaController().get_modificar(titulo_acta)
    titulo = request.form.get('titulo', None)
    codigo = request.form.get('codigo',None)
    tipo = request.form.get('tipo', None)
    fecha = request.form.get('fecha', None)
    archivo = request.form.get('archivo', None)
    descripcion = request.form.get('descripcion', None)
    return SecretariaController().modificar_acta(titulo_acta,codigo,titulo, tipo, fecha, archivo, descripcion)


@secretaria.route("/consultar_propuesta",methods=["GET","POST"])
def consultar_propuesta():
    if(request.method == "GET"):
        return SecretariaController().get_view_consultar_propuesta()
    titulo = request.form.get('titulo',None)
    codigo = request.form.get('codigo',None)
    return SecretariaController().consultar_propuesta(titulo,codigo)


@secretaria.route("/modificarEstado_propuesta/<codigo_propuesta>", methods=["GET","POST"])
def modificarEstado_propuesta(codigo_propuesta):
    if(request.method=="GET"):
        return SecretariaController().get_modificar_estado_propuesta(codigo_propuesta)
    estado = request.form.get('estado',None)
    return SecretariaController().modificar_estado_propuesta(codigo_propuesta,estado)

@secretaria.route("/agregarFechas_propuesta/<codigo_propuesta>", methods=["GET","POST"])
def modificarFechas_propuesta(codigo_propuesta):
    if(request.method=="GET"):
        return SecretariaController().get_agregar_fechas_propuesta(codigo_propuesta)
    fechaCorrecciones = request.form.get('fechaCorrecciones',None)
    fechaComentarios = request.form.get('fechaComentarios',None)
    print "lo que recibe: "+fechaComentarios
    return SecretariaController().modificar_fechas_propuesta(codigo_propuesta,fechaCorrecciones,fechaComentarios)

@secretaria.route("/habilitarEntregables_propuesta/<codigo_propuesta>", methods = ["GET","POST"])
def habilitar_envios_entregables(codigo_propuesta):
    if(request.method=="GET"):
        return SecretariaController().get_habilitar_envio_entregables(codigo_propuesta)
    entregable = request.form.get('entregable',None)
    return SecretariaController().habilitar_envio_entregables(codigo_propuesta,entregable)