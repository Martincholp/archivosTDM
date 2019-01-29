#! /usr/bin/env python
#*-* encoding: utf_8 *-*


###########################################################
##               Excepciones comunes                     ##
###########################################################


class tdmErrBase(Exception):
    ''' Clase base para las excepciones de tdm'''
    def __init__(self):
        pass


class tdmErrSintaxis(tdmErrBase):
    ' Sucede ante un error en la sintaxis del archivo'
    def __init__(self, msj):
        self.mensaje = str(msj)
    
    def __str__(self):
        return self.mensaje
        

class tdmErrTipoLin(tdmErrBase):
    'Se esperaba un tipo de linea y se recibio otro'
    def __init__(self, obtenido, esperado):
        self.obtenido = _tipo(obtenido)
        self.esperado = _tipo(esperado)
        
    def __str__(self):
        mje = 'El valor obtenido es ' + self.obtenido + \
              '. Se esperaba' + self.esperado + '.'
        return mje
    
    def _tipo(val):
        tipo = ''
        if val == 0:
            tipo = 'texto'
        elif val == 1:
            tipo = 'apertura de nodo'
        elif val == 2:
            tipo = 'propiedad'
        elif val == 3:
            tipo = 'cierre de nodo'
        elif val == 4:
            tipo = 'linea comentada'
        elif val == 10:
            tipo = 'texto con comentario'
        elif val == 11:
            tipo = 'apertura de nodo con comentario'
        elif val == 12:
            tipo = 'propiedad con comentario'
        elif val == 13:
            tipo = 'cierre de nodo con comentario'
        else:
            tipo = 'desconocido'
        
        return tipo
        
###########################################################
##             Excepciones de propiedades                ##
###########################################################

class tdmErrProp(tdmErrBase):
    ''' Clase base para las excepciones de propiedades'''
    def __init__(self):
        pass
        
        
class tdmPropRepetida(tdmErrProp):
    ''' La propiedad ya existe en el nodo'''
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __str__(self):
        return 'La propiedad ' + self.nombre + ' ya existe en el nodo.'
        
        
class tdmPropInexistente(tdmErrProp):
    ''' La propiedad no existe en el nodo'''
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __str__(self):
        return 'La propiedad ' + self.nombre + ' no existe en el nodo.'


class tdmPropArgumentoInvalido(tdmErrProp):
    'El argumento recibido no es valido'
    def __init__(self, arg):
        self.argumento = arg
        
    def __str__(self):
        return 'El argumento ' + str(arg) + ' no es valido para la accion requerida'


###########################################################
##           Excepciones del encabezado                  ##
###########################################################

class tdmEncPropLineaInvalida(tdmErrProp):
    'La linea no es propiedad de encabezado'
    def __init__(self, arg):
        self.argumento = arg
        
    def __str__(self):
        return 'La linea ' + str(arg) + ' no es de tipo propiedadBase'


  
        
###########################################################
##           Excepciones de archivo                      ##
###########################################################

class tdmErrArch(tdmErrBase):
    ' Clase base para las excepciones de archivo'
    def __init__(self):
        pass


class tdmArchNoDefinido(tdmErrArch):
    'La ruta de archivo aun no ha sido definida'
    def __init__(self):
        pass
        
    def __str__(self):
        return 'La ruta de archivo aun no ha sido definida.'


############################################################
##          Excepciones de nodos                          ##
############################################################

class tdmErrNodo(tdmErrBase):
    'Clase base para las excepciones de nodos'
    def __init__(self):
        pass
        
        
class tdmNodoArgumentoInvalido(tdmErrNodo):
    'El argumento recibido no es valido'
    def __init__(self, arg):
        self.argumento = arg
        
    def __str__(self):
        return 'El argumento ' + str(arg) + ' no es valido para la accion requerida'
        
class tdmNodoIndice(tdmErrNodo):
    'El indice esta fuera del rango'
    def __init__(self, indice):
        self.indice = indice
        
    def __str__(self):
        return 'El indice ' + str(indice) + ' esta fuera del rango'        

