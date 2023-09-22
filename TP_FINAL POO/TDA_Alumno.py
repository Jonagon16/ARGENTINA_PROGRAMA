class Alumno:
    __id = 0
    def __init__(self,fecha, nombre, materia, profesor, curso, division,nota):
        self.__fecha = fecha
        self.__nombre = nombre
        self.__materia = materia
        self.__profesor = profesor
        self.__curso = curso
        self.__division = division
        self.__nota = nota
        Alumno.__id += 1
        self.__id = Alumno.__id

    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self,fecha):
        if formato_fecha(fecha):
            self.__fecha = fecha
        else:
            raise ValueError ("La fecha debe ser en forma dd/mm/aaaa")

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def materia(self):
        return self.__materia
    @materia.setter
    def materia(self,materia):
        self.__materia = materia

    @property
    def profesor(self):
        return self.__profesor
    @profesor.setter
    def profesor(self,profesor):
        self.__profesor = profesor

    @property
    def curso(self):
        return self.__curso
    @curso.setter
    def curso(self,curso):
        self.__curso = curso

    @property
    def division(self):
        return self.__division
    @division.setter
    def division(self,division):
        self.__division = division

    @property
    def nota(self):
        return self.__nota
    @nota.setter
    def nota(self,nota):
        self.__nota = nota

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        raise AttributeError ("Este valor es de solo lectura no puede modificarse")

    def __str__(self):
        return f"ID: {self.__id}\nFecha: {self.__fecha}\nNombre: {self.__nombre}\nProfesor: {self.__materia}\nMateria: {self.__profesor}\nCurso: {self.__curso}\nDivisión: {self.__division}\nNota: {self.__nota}"

def formato_fecha(fecha):
    fecha = fecha.split("/")
    if len(fecha) == 3:
        return True
    else:
        return False

def crearAlumnos(archivo):
    fl = {}
    with open(archivo,'r') as arch:
        for i in arch:
            fecha, nombre, materia, profesor, curso, division, nota = i.strip().split(',')
            alumno = Alumno(fecha,nombre,materia,profesor,curso,division,nota)
            fl[alumno.id] = alumno
    return fl

def limpiarDni(s):
    s = s.replace(".","")
    return s

def guardarAlumnos(archivo,dict):
    f=open(archivo,"w")
    for i,j in dict.items():
        f.write(f"{j.fecha},{j.nombre},{j.materia},{j.profesor},{j.curso},{j.division},{j.nota}\n")
    f.close()

def validarAlumno(alumno,materia,dic):
    for i in dic.values():
        if alumno in i.nombre and materia == i.materia:
            return True
        else:
            return False

def mostrarAlumnos(dic):
    for id, alumno in dic.items():
        print("#" * 20)
        print(alumno)

def eliminarAlumno(alumno,dic):
    for i,j in dic.items():
        if j == alumno:
            del dic[i]
            return True
        else:
            return False

def filtrar_alumnos(profesor:object,dic:dict):
    d_alumnos = {}
    for i,alumno in dic.items():
        if profesor == alumno.profesor:
            d_alumnos[alumno.id] = alumno
            return True
        else:
            return False

def nombre_id(nombre,dic:dict):
    for id,alumno in dic.items():
        if alumno.nombre == nombre:
            return id
        else:
            return None
