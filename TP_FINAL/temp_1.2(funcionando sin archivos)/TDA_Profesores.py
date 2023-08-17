def crear (nombre,dni):
    enca={}
    enca[nombre] = dni
    return enca

def modificar (atr,valor,dic):
    dic[atr] = valor

def mostrar (atr,dic):
    return dic[atr]

def validarProfesor (nombre,materia,curso,division,dic):
    r=0
    for i,j in dic.items():
        if nombre == j['nombre'] and materia == j['materia'] and division == j['division'] and curso == j['curso']:
            r=1
            break
    return r
def validarAlumno(alumno,dic):
    r=1
    if alumno in dic.keys():
        r=2
    return r

def mostrarNotas(dic):
    for alumno, datos in dic.items():
        print("#" * 20)
        print(f"Alumno: {datos['nombre']}")
        print(f"Materia: {datos['materia']}")
        print(f"Nota: {datos['nota']}")


def eliminarNota(alumno,materia,dic):
    dic[alumno]['Nota']= -1

def modificarNota(alumno,materia,nota,dic):
        dic[alumno]['nota'] = nota
