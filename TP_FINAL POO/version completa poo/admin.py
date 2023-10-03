import TDA_Encargado as Enca
import TDA_Profesores as Profe
import os
def lp():
    os.system('cls' if os.name == 'nt' else 'clear')

def validarAdmin(user, passw):
    try:
        with open('user.txt', 'r') as file:
            for line in file:
                u, p = line.strip().split(',')
                if u == user and p == passw:
                    return True
    except FileNotFoundError:
        lp()
        print("Archivo de usuarios no encontrado.")
    return False

def menu_secreto(tencargados,tprofesores):
    while True:
        print("#" * 20)
        print("Bienvenido Administrador")
        print("1_Crear Encargado")
        print("2_Modificar Encargado")
        print("3_Eliminar Encargado")
        print("4_Crear Profesor")
        print("5_Modificar Profesor")
        print("6_Eliminar Profesor")
        print("7_Mostrar Encargados")
        print("8_Mostrar Profesores")
        print("9_Guardar y Salir")
        op = input("")
        print("#" * 20)

        if op == "1":
            try:
                nombre, dni = input("Ingrese Nombre,Dni: ").split(",")
                if Enca.crear(nombre,dni,tencargados):
                    lp()
                    print("Se creo correctamente el encargado")
                    print(tencargados)
                    Enca.guardarEncargado("encargados.txt",tencargados)
                else:
                    lp()
                    print("No se pudo crear el encargado")
            except ValueError:
                lp()
                print("Debe colocar ambos datos")

        elif op == "2":
            try:
                nombre, dni = input("Ingrese Nombre,Dni: ").split(",")
                if Enca.modificar(nombre,dni,tencargados):
                    lp()
                    print("Se modifico el encargado")
                    print(tencargados)
                    Enca.guardarEncargado("encargados.txt",tencargados)
                else:
                    lp()
                    print("No se pudo modificar el encargado")
            except ValueError:
                lp()
                print("Debe colocar ambos datos")
            except KeyError:
                lp()
                print("El encargado que desa modificar no existe")

        elif op == "3":
            try:
                nombre = input("Ingrese encargado a eliminar: ")
                tencargados.pop(nombre)
                lp()
                print("El encargado a sido eliminado")
            except KeyError:
                lp()
                print("El encargado que desa eliminar no existe")
        elif op == "4":
            try:
                nombre, materia, curso, division = input("Ingrese Nombre, Materia, Curso, Division del Profesor: ").split(",")
                if Profe.crear(nombre, materia,curso,division, tprofesores):
                    lp()
                    print("Se creo correctamente el encargado")
                    print(tprofesores)
                    Profe.guardarProfesores("profesores.txt", tprofesores)
                else:
                    lp()
                    print("No se pudo crear el profesor")
            except ValueError:
                lp()
                print("Debe colocar ambos datos")

        elif op == "5":
            try:
                nombre, materia, curso, division = input("Ingrese Nombre, Materia, Curso, Division del Profesor: ").split(",")
                if Profe.crear(nombre, materia,curso,division, tprofesores):
                    lp()
                    print("Se modifico el encargado correctamente")
                    print(tprofesores)
                    Profe.guardarProfesores("profesores.txt", tprofesores)
                else:
                    lp()
                    print("No se pudo crear el profesor")
            except ValueError:
                lp()
                print("Debe colocar ambos datos")
        elif op == "6":
            try:
                nombre = input("Ingrese profesor a eliminar: ")
                tprofesores.pop(nombre)
                lp()
                print("El profesor a sido eliminado")
            except KeyError:
                lp()
                print("El encargado que desa eliminar no existe")

        elif op == "7":
            lp()
            print(tencargados)

        elif op == "8":
            lp()
            print(tprofesores)

        elif op == "9":
            lp()
            break

        else:
            lp()
            print("Opcion invalida, intente nuevamente.")

