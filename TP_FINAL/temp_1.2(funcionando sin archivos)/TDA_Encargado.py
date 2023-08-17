def crear (nombre,dni):
    enca={}
    enca[nombre] = dni
    return enca

def modificar (atr,valor,dic):
    dic[atr] = valor

def mostrar (atr,dic):
    return dic[atr]

def validarEncargado (nombre,dni,dic):
    r=0
    for i,j in dic.items():
        if nombre in i and dni == j:
            r=1
    return r
def validarAlumno(alumno,materia,dic):
    r=1
    if alumno in dic.keys() and materia == dic[alumno]:
        r=2
    return r
def inscribirAlumno(fecha=None,alumno=None,materia=None,profesor=None,curso=None,division=None,dic=None):
    dic[alumno]={
        'fecha':fecha,
        'nombre':alumno,
        'materia':materia,
        'profesor':profesor,
        'curso':curso,
        'division':division,
        'nota':"-1"
    }
def mostrarAlumnos(dic):
    for alumno, datos in dic.items():
        print("#" * 20)
        print(f"Fecha: {datos['fecha']}")
        print(f"Alumno: {datos['nombre']}")
        print(f"Materia: {datos['materia']}")
        print(f"Profesor: {datos['profesor']}")
        print(f"Division: {datos['division']}")
        print(f"Nota: {datos['nota']}")


def eliminarAlumno(alumno,materia,dic):
    dic.pop(alumno,materia)
