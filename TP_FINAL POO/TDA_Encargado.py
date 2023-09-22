import TDA_Alumno as al
class Encargado:
    __id = 0
    def __init__(self,nombre,dni):
        self.__nombre = nombre
        self.__dni = dni
        Encargado.__id += 1
        self.__id = Encargado.__id
        self.__alumnosInscriptos = []

    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self,n):
        n = limpiarDni(n)
        if isinstance(n,int):
            self.__dni = n
        else:
            raise ValueError ("El documento solo puede ser numerico")

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def alumnosInscriptos(self):
        return self.__alumnosInscriptos
    @alumnosInscriptos.setter
    def alumnosInscriptos(self,alumno):
        self.__alumnosInscriptos.append(alumno)

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        raise AttributeError ("Este valor es de solo lectura no puede modificarse")

    def inscribirAlumno(self,fecha=None, alumno=None, materia=None, profesor=None, curso=None, division=None, dic=None):
        a = al.Alumno(fecha, alumno, materia, profesor, curso, division, nota=-1)
        dic[a.id] = a
        self.__alumnosInscriptos.append(a)


def limpiarDni(s):
    s = s.replace(".","")
    return s

def crear (nombre,dni,tencargados):
    for i in tencargados.values():
        if int(i.dni) == int(dni):
           return "El encargado Ya Existe"
        else:
            encargado = Encargado(nombre,dni)
            tencargados[encargado.id] = encargado

def crearEncargados(archivo):
    fl = {}
    with open (archivo,'r') as arch:
        for i in arch:
            nombre, dni = i.strip().split(',')
            encargado = Encargado(nombre,dni)
            fl[encargado.id] = encargado
    return fl


def guardarEncargado(archivo,dict):
    f=open(archivo,"w")
    for i,j in dict.items():
        f.write(f"{j.nombre},{j.dni}\n")
    f.close()

def validarEncargado (nombre,dni,dic):
    for i,j in dic.items():
        if nombre in j.nombre and dni == j.dni:
            return True
        else:
            return False



