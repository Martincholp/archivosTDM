#! /usr/bin/env python
#*-* encoding: utf_8 *-*

from tdmerr import *

'''Definicion de las entidades'''

class Propiedad(object):
    """Propiedad de tipo clave-valor"""
    def __init__(self, clave, valor):
        self._clave = clave
        self._valor = valor

    @property
    def clave(self):
        '''Clave de la propiedad'''
        return self._clave
    
    @property
    def valor(self):
        '''Valor de la propiedad'''
        return self._valor
    
    @valor.setter
    def valor(self, val):
        self._valor = val
    
    
        
class Seccion(object):
    """Seccion de TDM"""
    def __init__(self, nombre):
        self._nombre = nombre
        self._texto = Texto()
        self._props = {}
        self._coms = Comentario()
        self._subSecc = []

    @property
    def nombre(self):
        '''Nombre de la seccion'''
        return self._nombre

    def addProp(self, propiedad):
        '''Agrega una propiedad a la entidad'''
        self._props[propiedad.clave] = propiedad

    def getProp(self, clave):
        '''Devuelve la propiedad solicitada'''
        return self._props[clave]

    def getProps(self):
        '''Devuelve una lista con todas las propiedades de la entidad'''
        return self._props.values()

    def getClavesProps(self):
        '''Devuelve una lista con las claves de las propiedades de la entidad'''
        return self._props.keys()

    def __getitem__(self, clave):
        '''Devuelve el valor de una propiedad usando la sintaxis valor=entidad[clave]'''
        return self._props[clave].valor

    
    def addSeccion(self, seccion):
        '''Agrega una seccion hija'''
        self._subSecc.append(seccion)

    def getSecciones(self, nombre=""):
        '''Devuelve una lista de las subsecciones con el nombre indicado. Si no hay subsecciones con ese nombre la lista estará vacía.
        Si se omite el nombre, o es una cadena vacia devuelve todas las subsecciones hijas.'''

        if nombre == "":
            res = self._subSecc
        else:
            res = []
            for s in self._subSecc:
                if s.nombre == nombre:
                    res.append(s)

        return res

    def getSeccion(self, indice):
        '''Devuelve una seccion hija segun el indice indicado. Si no tiene subsecciones devuelve error'''
        return self._subSecc[indice]

    def getCantSecciones(self):
        '''Devuelve un entero con la cantidad de secciones hijas de la entidad'''
        return len(self._subSecc)

class Texto(object):
    """Texto de entidad"""
    def __init__(self, val=""):
        self._val = val

    def addLinea(self, linea):
        '''Agrega una linea mas al texto de la entidad'''
        self._val = self._val + '\n' + linea

    @property
    def valor(self):
        '''Contenido del texto de entidad'''
        return self._valor
        
    @valor.setter
    def valor(self, val):
        self._valor = val
    
            

class Comentario(object):
    """Comentario de una entidad"""
    def __init__(self, com):
        self.__com = com
        
class Documento(Seccion):
    """Documento de archivo TDM"""
    def __init__(self, arg):
        super(Documento, self).__init__()
        self.arg = arg
        
        