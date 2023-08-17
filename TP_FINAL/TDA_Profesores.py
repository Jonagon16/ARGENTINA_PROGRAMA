def crear (nombre,materia,curso,division,dic):
    if nombre in dic:
        print("El DNI nombre ya existe para otro Profesor.")
        return False
    dic[nombre] = {
        'nombre': nombre,
        'materia': materia,
        'curso': curso,
        'division': division
    }
    return True

def modificar (nombre,materia,curso,division,dic):
    if nombre in dic:
        dic[nombre] = {
                          'nombre': nombre,
                          'materia': materia,
                          'curso': curso,
                          'division': division
                      }
        return True
    else:
        print("El profesor que quiere modificar no existe")
        return False

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
    r=0
    if alumno in dic.keys():
        r=1
    return r

def mostrarNotas(dic):
    for alumno, datos in dic.items():
        print("#" * 20)
        print(f"Alumno: {datos['nombre']}")
        print(f"Materia: {datos['materia']}")
        print(f"Nota: {datos['nota']}")


def eliminarNota(alumno,materia,dic):
    dic[alumno]['nota']= -1

def modificarNota(alumno,materia,nota,dic):
    dic[alumno]['nota'] = nota

def crearProfesores(archivo):
    fl = {}
    with open (archivo,'r') as arch:
        for i in arch:
            nombre, materia, curso, division= i.strip().split(',')
            fl_temp = {
                'nombre': nombre,
                'materia': materia,
                'curso': curso,
                'division': division
            }
            fl[nombre]=fl_temp
    return fl

def guardarProfesores(archivo,dict):
    f=open(archivo,"w")
    for i,j in dict.items():
        f.write(f"{j['nombre']},{j['materia']},{j['curso']},{j['division']}\n")
    f.close()

def validarNota(nota):
    try:
        note = int(nota)
        if 0 <= note <= 10:
            return nota
        else:
            return '-1'
    except ValueError:
        return '-1'