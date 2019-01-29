#! /usr/bin/env python
#*-* encoding: utf_8 *-*

from tdmerr import *


    ##############################################
    ##                                          ##
    ##               ENCABEZADO                 ##
    ##                                          ##
    ##############################################

class encabezado(object):
    'Encabezado de un archivo TDM '
    def __init__(self):
        self._propiedades = {}
        self._texto = ''
        self._raiz = '' 
        
    ##############################################
    ##          Texto del encabezado            ##
    ##############################################

    def _setTexto(self, texto):
        '''Asigna el texto del encabezado'''
        texto = texto.strip()
        tipo = _tipolin(texto)
        if tipo == 0:
            self._texto = texto
        else:
            # Lanza una excepcion si el texto no es del tipo correcto
            msj = 'El texto ' + text + ' no es valido.'
            raise tdmErrTipoLin, tipo, 0
            
        
    def _getTexto(self):
        '''Devuelve el texto del nodo'''
        return self._texto
        
    texto = property(_getTexto, _setTexto) 


    ##############################################
    ##   Manejo de propiedades del encabezado   ##
    ##############################################
        
    def propiedades(self, nom = None):
        '''Propiedades del encabezado. Si el parametro nom no es pasado o vale 
        None se devuelve una lista con todas las propiedades. Si existe el 
        parametro nom se devuelve el valor de la propiedad que tiene ese nombre.'''
        
        if nom == None:
        # Lista de propiedades
            return self._propiedades.values()
        else:
        # Valor de sel
            if type(nom) is str:
                return self._propiedades[nom].valor
            else:
                raise tdmPropArgumentoInvalido, str(nom)
        
            
    def agregarprop(self, propiedad):
        'Agrega la propiedad pasada al encabezado'
        
        if self._propiedades.has_key(propiedad.nombre):
            raise tdmPropRepetida(propiedad.nombre)
            
        self._propiedades[propiedad.nombre] = propiedad
        
        
    def quitarprop(self, nombreprop):
        'Quita la propiedad nombreprop del encabezado'
        
        try:            
            del self._propiedades[nombreprop]
        
        except KeyError:
           raise tdmPropInexistente, nombreprop 
        
    ##############################################
    ##           Funciones varias               ##
    ##############################################
    
    def _leer(self, f):
        '''Recibe un objeto file en el parametro f y lo analiza completando los 
datos correspondientes al encabezado. Cuando encuentra una llave de apertura de 
nodo termina la lectura y guarda en la variable "_raiz" el valor del nodo. Si 
no hay nodo raiz lanza una excepcion.'''
        
        linea = ''  # Linea del archivo
        pcar = ''  # Primer caracter de la linea (verifica si es propiedad)
        salir = False
        
        while not salir:
            linea = f.readline()
            pcar = linea[0]
            
            if pcar == '!':
                # Es una propiedad.
                lin = linea[1:]
                tipo = _tipolin(lin)
                if tipo == 2:
                    prop = _parserprop(lin)
                    propb = propiedadBase(prop.nombre, prop.valor)
                    self.agregarprop(propb)
                else:
                    raise tdmEncPropLineaInvalida, linea
            else:
                # Verifico si abre un nodo
                if _tipolin(linea) == 1:
                    f.seek(-len(linea), 1)
                    salir = True
                else:
                    self._texto += linea
                
            
            
            
        

    ##############################################
    ##                                          ##
    ##             PROPIEDAD BASE               ##
    ##                                          ##
    ##############################################

class propiedadBase(object):
    'Objeto base para crear propiedades.'
    
    # No contiene el parametro de comentario
    def __init__(self, nombre = '', valor = ''):
        self._nombre = ''
        self._setNombre(nombre)
        self._valor = ''
        self._setValor(valor)
        
    
    def _setNombre(self, nombre):
        'Asigna el nombre de la propiedad'
        nombre = nombre.strip()
        val = _validalin(nombre)
        if val:
            self._nombre = nombre
        else:
            # Lanza una excepcion si el nombre no es valido
            msj = 'El nombre ' + nombre + ' no es valido.'
            raise tdmErrSintaxis, msj
            
        
    def _getNombre(self):
        'Devuelve el nombre de la propiedad'
        return self._nombre
        
    nombre = property(_getNombre, _setNombre)
        
    def _setValor(self, valor):
        'Asigna el valor de la propiedad'
        valor = valor.strip()
        val = _validalin(valor)
        if val:
            self._valor = valor
        else:
            # Lanza una excepcion si el valor no es valido
            msj = 'El valor ' + valor + ' no es valido.'
            raise tdmErrSintaxis, msj
            
        
    def _getValor(self):
        'Devuelve el valor de la propiedad'
        return self._valor
        
    valor = property(_getValor, _setValor)
        
    def __str__(self):
        s = self._nombre + ' = ' + self._valor
        return s
        
    def __repr__(self):
        return str(self)


    ##############################################
    ##                                          ##
    ##              PROPIEDADES                 ##
    ##                                          ##
    ##############################################

class propiedad(propiedadBase):
    def __init__(self, nombre = '', valor = ''):
        propiedadBase.__init__(self, nombre, valor)
        self._comentario = ''
        
    pass
    
    
    ##############################################
    ##                                          ##
    ##                 NODOS                    ##
    ##                                          ##
    ##############################################

class nodo(object):
    'Objeto nodo'
    def __init__(self, nombre):
        self._nombre = ''
        self._setNombre(nombre)
        self._texto = ''
        self._propiedades = {}
        self._nodos = []
        self._comentario = ''
        
        
    ##############################################
    ##         Nombre del nodo                  ##
    ##############################################
    
    def _setNombre(self, nombre):
        'Asigna el nombre del nodo'
        nombre = nombre.strip()
        val = _validalin(nombre)
        if val:
            self._nombre = nombre
        else:
            # Lanza una excepcion si el nombre no es valido
            msj = 'El nombre ' + nombre + ' no es valido.'
            raise tdmErrSintaxis, msj
            
        
    def _getNombre(self):
        'Devuelve el nombre de la propiedad'
        return self._nombre
        
    nombre = property(_getNombre, _setNombre)        
        

    ##############################################
    ##          Texto del nodo                  ##
    ##############################################

    def _setTexto(self, texto):
        'Asigna el texto del nodo'
        texto = texto.strip()
        val = _validalin(texto)
        if val:
            self._texto = texto
        else:
            # Lanza una excepcion si el texto no es valido
            msj = 'El texto ' + text + ' no es valido.'
            raise tdmErrSintaxis, msj
            
        
    def _getTexto(self):
        'Devuelve el texto del nodo'
        return self._texto
        
    texto = property(_getTexto, _setTexto) 
           
    ##############################################
    ##         Manejo de propiedades            ##
    ##############################################
        
    def propiedades(self, nom = None):
        'Propiedades del nodo. Si el parametro nom no es pasado o vale None se \
devuelve una lista con todas las propiedades. Si existe el parametro nom se \
devuelve el valor de la propiedad que tiene ese nombre. Notar que esto ultimo \
es equivalente a hacer objetoNodo.propiedad("NombrePropiedad").valor'
        
        try:
            if nom == None:
            # Lista de propiedades
                return self._propiedades.values()
            else:
            # Valor de sel
                if type(nom) is str:
                    return self._propiedades[nom].valor
                else:
                    raise tdmPropArgumentoInvalido, str(nom)
        except KeyError:
            raise tdm.PropInexistente, nom
        else:
            raise                
    
    
    def propiedad(self, nom):
        'Devuelve la propiedad de nombre nom'
        try:
            if type(nom) is str:
                return self._propiedades[nom]
            else:
                raise tdmPropArgumentoInvalido, str(nom)
        except KeyError:
            raise tdm.PropInexistente, nom
        else:
            raise                
              
            
    def agregarprop(self, propiedad):
        'Agrega la propiedad pasada al nodo'
        
        if self._propiedades.has_key(propiedad.nombre):
            raise tdmPropRepetida(propiedad.nombre)
            
        self._propiedades[propiedad.nombre] = propiedad
        
        
    def quitarprop(self, nombreprop):
        'Quita la propiedad nombreprop del nodo'
        
        try:            
            del self._propiedades[nombreprop]
        
        except KeyError:
           raise tdmPropInexistente, nombreprop 
        

    ##############################################
    ##          Manejo de nodos hijos           ##
    ##############################################

    def nodos(self, sel = None):
        'Nodos hijos del nodo. Si sel = None devuelve una lista con todos \
los nodos hijos del nodo. Si sel = valor, y valor es una cadena de caracteres \
devuelve una lista con los nodos hijos que se llamen igual que valor. Si valor \
es un entero devuelve el hijo en la posicion indicada. Si es un entero \
negativo cuenta de atras hacia adelante.'
        
        if sel == None:
            return self._nodos

        elif type(sel) is str:
            nds = [nod for nod in self._nodos if sel == nod.nombre]
            return nds
        
        elif type(sel) is int:
            return self._nodos[sel]
        
        else:
            raise tdmNodoArgumentoInvalido, sel


    def agregarnodo(self, nodo, pos = None):
        'Agrega un hijo al nodo en la posicion pos. Si pos se omite el hijo \
se agrega al final. Si es negativo empieza a contar desde atras.'
        
       
        if type(nodo) is not type(self):
            raise tdmNodoArgumentoInvalido, nodo
            
        if pos == None:
            self._nodos.append(nodo)
        elif type(pos) is int:
            cant = len(self._nodos)
            if (pos >= cant - 1) or (pos < -cant):
                raise tdmNodoIndice, pos
            else:
                self._nodos.insert(pos, nodo)
        else:
            raise tdmNodoArgumentoInvalido, pos

    def quitarnodo(self, pos):
        'Quita el nodo hijo en la posicion pos. Si no existe esa posicion \
lanza una excepcion.'
        #del self._nodos(pos)
        pass
        

        
    def __str__(self):
        # Falta aplicar tabuladores ( chr(9) ) para indentar correctamente
        
        nom = self.nombre
        txt = self.texto
        pro = ''
        for i in self.propiedades():
            pro = pro + str(i) + chr(10)
            
        nds = ''
        for i in self.nodos():
            nds = nds + str(i)
            
        todo = nom + chr(10) + \
               txt + chr(10) + \
               pro + \
               nds
        
        return todo
        
        
    def __repr__(self):
        return self.nombre


    ##############################################
    ##                                          ##
    ##                DOCUMENTO                 ##
    ##                                          ##
    ##############################################

class documento(object):
    'Clase que representa el documento. Su contenido principal es el nodo raiz'
   
    def __init__(self):
    	self._archivo = ''
        self._encabezado = None
        self._raiz = None
        
    
    def raiz(self):
        'Devuelve el nodo raiz del documento'
        return self._raiz
        
    
    def encabezado(self):
        'Devuelve el encabezado del documento'
        return self._encabezado
        
    
    def archivo(self):
        'Devuelve el nombre del archivo del documento'
        return self._archivo
                
    
    def cargar(self, archivo):
        'Carga un archivo para que este disponible para su uso'
        self._archivo = archivo  # Guardo el nombre del archivo
        
        try:
            f = open(archivo)
            
            # Comienzo a leer el encabezado
            enc = encabezado()
            enc._leer(f)
            self._encabezado = enc
            
            # Comienzo a leer los nodos
            self._raiz = _leerNodo(f)
            
            
        except:
            raise
        finally:
            f.close()
        
    

    ##############################################
    ##                                          ##
    ##       FUNCIONES GLOBALES VARIAS          ##
    ##                                          ##
    ##############################################

def _validalin(linea):
    'Devuelve True si la linea es valida para ser utilizada como texto, es \
decir que no tiene literales o los tiene escapados. Si encuentra algun literal \
sin escapar devuelve False. '

    res = True
    c = _tipolin(linea)
    if c != 0:
        res = False
    
    return res
    
    
def _tipolin(linea):
    ''' Devuelve el tipo de linea
    0 = texto del nodo
    1 = abre nodo
    2 = propiedad
    3 = cierra nodo
    4 = comentario (toda la linea comentada)
    
    Si la linea es valida con comentario al final suma 10 al valor devuelto
    10 = texto del nodo con comentario
    11 = abre nodo con comentario
    12 = propiedad con comentario
    13 = cierra nodo con comentario
    
    Si la linea contiene 2 literales sin escapar lanza la excepcion tdmErrSintaxis
    '''
    
    linea = linea.lstrip()
    res = 0  # Resultado a devolver
    escape = False  # True si estoy escapando el caracter siguiente
    litenc = False  # True si ya encontre el literal que define la linea.
                    # Si vuelvo a encontrar alguno sin escapar ocurre error.
    primc = True    # True si es el primer caracter que analizo (para comentario)

    for c in linea:
        # Verifico si estoy escapando el caracter siguiente
        if c == "/" and not escape:
            escape = True
            continue
            
        # Verifico si abre un nodo
        if c == "{" and not escape:
            if litenc:
                msj = 'Se encontro el caracter ' + c + '. Se esperaba fin de linea.'
                raise tdmErrSintaxis, msj
            else:
                res = 1
                litenc = True
            
        # Verifico si e una propiedad  
        if c == "=" and not escape:
            if litenc:
                msj = 'Se encontro el caracter ' + c + '. Se esperaba fin de linea.'
                raise tdmErrSintaxis, msj
            else:
                res = 2
                litenc = True
                            
        # Verifico si cierra un nodo    
        if c == "}" and not escape:
            if litenc:
                msj = 'Se encontro el caracter ' + c + '. Se esperaba fin de linea.'
                raise tdmErrSintaxis, msj
            else:
                res = 3
                litenc = True
                        
        # Verifico si es una linea comentada
        if c == "'" and not escape:
            if primc:
                res = 4  # Todo el renglon comentado
            else:
                res = res + 10  # Si tiene comentario le suma 10 al resultado
                
            break  # Apenas encuentro el comentario salgo.
                       # Todo lo sgte no se evalua y no da error.
                
        escape = False  # Termino el escapado del literal
        primc = False  # Despues de la primer pasada ya no es el primer caracter
        
        
    # Si no encontro ningun literal sin escapar entonces res no ha sido
    # modificado y corresponde a texto del nodo.
    return res
    
    
def _parserprop(linea):
    'Parsea una linea de propiedad (tipo 2 o tipo 12) y la devuelve como objeto.'
    
    linea = linea.strip()
    escape = False
    nombre = ''
    valor = ''
    comentario = ''
    parte = 0
    
    # La variable parte define que parte de la propiedad estoy parseando. Si
    # vale 0 el caracter leido es parte del nombre, si vale 1 es parte del valor
    # y si es igual a 2 es comentario.
     

    for n in linea:
        if parte != 2:   # Busco literales escapados fuera del comentario
            if n == "/" and not escape:  
                escape = True
                continue
            
            if n == "=" and not escape:   # Paso a armar el valor
                # Encuentro un igual sin escapar. Si estoy en el nombre
                # (parte = 0) hago parte = 1 para obtener el valor. Si ya estaba
                # en el valor (parte = 1), lanzo una excepcion de sintaxis.
                if parte == 0:
                    parte = 1
                    continue 
                elif parte == 1:
                    raise tdmErrSintaxis, linea
                    
            if n == "'" and not escape:   # Paso a armar el comentario
                parte = 2
                continue
                
        # Asigno el caracter a la parte que corresponda        
        
        if parte == 0:
            nombre += n
        elif parte == 1:
            valor += n
        else:
            comentario += n
        
        escape = False
        
                      
    # Creo la propiedad y la devuelvo
               
    prop = propiedad(nombre, valor)
    prop._comentario = comentario
    
    return prop
    

def _parsernombrenod(linea):
    'Parsea una linea de apertura de nodo (tipo 1) y devuelve el nombre, sin \
espacios ni llave de apertura'
    
    nombre = ''
    valido = False  # Si no encuentro una llave de apertura no es nombre
    linea = linea.strip()
    
    # Verifico si el nombre tiene comentarios escapados.
    # Ademas elimino el comentario inline en el caso de que hubiera.
    for n in linea:
        if n == "/" and not escape:
            escape = True
            continue
        if n == "{" and not escape:
            valido = True
            break
        if n == "'" and not escape:
            break
        
        nombre += n
        escape = False
    
    if valido:
        return nombre
    else:
        return None
        

def _leerNodo(f):
    ' Parsea un nodo desde un objeto file pasado como parametro. El cursor \
de lectura debe estar situado al principio de la linea donde comienza el nodo.'
        
    texto = ''
    salir = False
    lin = f.readline()
    n = nodo(_parsernombrenod(lin))
       
    while not salir:
        lin = f.readline()
        tipo = _tipolin(lin)
          
        if tipo == 0 or tipo == tipo + 10:
            texto += lin + '\n'
               
        if tipo == 1 or tipo == tipo + 10:
            f.seek(-len(lin), 1)
            h = _leerNodo(f)
            n.agregarnodo(h)
                
        if tipo == 2 or tipo == tipo + 10:
            prop = _parserprop(lin)
            n.agregarprop(prop)
            
        if tipo == 3 or tipo == tipo + 10:
            n.texto = texto
            salir = True
            return n
            
        if tipo == 4:
            # Es toda la linea comentada
            n._comentario += lin
              
