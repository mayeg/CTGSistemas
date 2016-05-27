# -*- coding: utf-8 -*-
from dto.tipo_usuario import TipoUsuario


class Usuario:

    def __init__(self, codigo="", cedula="", contrasena="", id=0, nombres="",
                 apellidos="", email="", tipo_usuario=0):
        self.__codigo = codigo
        self.__cedula = cedula
        self.__contrasena = contrasena
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__email = email
        self.__id = id
        self.__tipo_usuario = TipoUsuario(id=tipo_usuario)

    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getCedula(self):
        return self.__cedula

    def setCedula(self, cedula):
        self.__cedula = cedula

    def getContrasena(self):
        return self.__contrasena

    def setContrasena(self, contrasena):
        self.__contrasena = contrasena

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNombres(self):
        return self.__nombres

    def setNombres(self, nombres):
        self.__nombres = nombres

    def getApellidos(self):
        return self.__apellidos

    def setApellidos(self, apellidos):
        self.__apellidos = apellidos

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getTipoUsuario(self):
        return self.__tipo_usuario

    def setTipoUsuario(self, tipo_usuario):
        self.__tipo_usuario = tipo_usuario

    def __unicode__(self):
        return "Codigo: {}, contrasena:{}".format(
            self.__codigo, self.__contrasena)

    def get_dict(self):
        return {
            'nombres': self.__nombres,
            'tipo': self.__tipo_usuario.getLabel(),
            'id': self.__id,
            'codigo': self.__codigo
        }