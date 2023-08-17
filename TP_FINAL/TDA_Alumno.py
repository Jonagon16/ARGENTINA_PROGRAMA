def crearAlumnos(archivo):
    fl = {}
    with open(archivo,'r') as arch:
        for i in arch:
            fecha, nombre, materia, profesor, curso, division, nota = i.strip().split(',')
            fl_temp = {
                'fecha': fecha,
                'nombre': nombre,
                'materia': materia,
                'profesor': profesor,
                'curso': curso,
                'division': division,
                'nota': "-1"
            }
            fl[nombre]= fl_temp
    return fl

def limpiarDni(s):
    s = s.replace(".","")
    return s


def guardarAlumnos(archivo,dict):
    f=open(archivo,"w")
    for i,j in dict.items():
        f.write(f"{j['fecha']},{j['nombre']},{j['materia']},{j['profesor']},{j['curso']},{j['division']},{j['nota']}\n")
    f.close()


