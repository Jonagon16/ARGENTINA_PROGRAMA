n = int(input("Ingrese la cantidad de personas que desea ingresar: "))
l = dict()
for i in range(n):
    c = list(input("ingrese los datos de la persona con formato 'dni,nombre,edad,domicilio,trabajo1,trabajo2': ").split(","))
    dni, nombre, edad, domicilio = c[:4]
    trabajo = []
    for j in c[4:]:
        trabajo.append(j)
    l[dni] = {
        'Nombre': nombre,
        'Edad': int(edad),
        'Docimilio': domicilio,
        'Trabajos': tuple(trabajo)
    }
op = int(input("Si quiere busca a un empleado coloque '1' En su defecto si quiere salir del programa coloque '0'"))
while op == 1:
    emp = str(input("Ingrese el Dni sin puntos, de un empleado o 'exit' para terminar: "))
    if emp in l:
        print(f"El siguiente dni corresponde a {l[emp]}")
        break
    elif emp == "exit":
        break
    else:
        print("El DNI no se encontro\n")
        continue