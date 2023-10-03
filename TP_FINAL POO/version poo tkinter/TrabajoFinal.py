import Profesores as Profe
import Encargado as Enca
import Alumno as alum
import admin
import os
#diccionarios para desempaquetar archivos
c_profesor = ""
c_alumno = ""
c_encargado = ""
temp_cookie = ""
tprofesores = {}
tencargados = {}
talumnos = {}
try:
    tencargados = Enca.crearEncargados("encargados.txt")
    print(tencargados)
except FileNotFoundError:
    print("Archivo de encargados no encontrado.")
try:
    tprofesores = Profe.crearProfesores("profesores.txt")
    print(tprofesores)
except FileNotFoundError:
    print("Archivo de profesores no encontrado.")
try:
    talumnos = alum.crearAlumnos("alumnos.txt")
    print(talumnos)
except FileNotFoundError:
    print("Archivo de alumnos no encontrado.")
def lp():
    os.system('cls' if os.name == 'nt' else 'clear')

def guardar():
    alum.guardarAlumnos("alumnos.txt", talumnos)
#variables para salir de bucles
x = False
z = False
v = False
#menu inicial
while not x:
    print("#"*20)
    print("Bienvenido elija su opcion")
    print("1_Profesor")
    print("2_Encargado")
    print("3_Salir")
    op = input("")
    print("#" * 20)
#verifico si se eligio la opcion 1 y hago la vadilacion de datos
    if op == "1":
        try:
            nombre, materia, curso, division = input("Ingrese: Nombre,Materia,curso,division ").split(",")
            if not Profe.validarProfesor(nombre,materia,curso,division,tprofesores):
                raise SyntaxError
            else:
                z = False
                c_prof =alum.nombre_id(nombre,tprofesores)
                c_profesor = tprofesores[c_prof]
                lp()
                #ingreso al menu profesor
                while not z:
                    print("#" * 20)
                    print(f"Bienvenido Profesor ")
                    print("1_Cargar Notas")
                    print("2_Mostrar Notas")
                    print("3_Modificar Notas")
                    print("4_Eliminar Notas")
                    print("5_Volver al Menu anterior")
                    op1 = input("")
                    print("#" * 20)
                    #verifica si existe el alumno y si existe lo modifica
                    if op1 == "1":
                        try:
                            alumno, materia, nota = input("ingrese: Alumno,materia,nota ").split(",")
                            if not alum.validarAlumno(alumno,materia,talumnos):
                                raise ValueError
                            else:
                                Profe.modificarNota(alumno,materia,Profe.validarNota(nota),talumnos)
                                lp()
                                guardar()
                                print(f"Se asigno la nota {nota} al alumno {alumno} correctamente")
                        except ValueError:
                            lp()
                            print("El Alumno ingresado no existe o no esta anotado para la materia nombrada")
                            continue
                        except KeyError:
                            lp()
                            print("El Alumno ingresado no existe o no esta anotado para la materia nombrada")
                            continue

                    elif op1 == "2":
                        lp()
                        Profe.mostrarNotas(talumnos)

                    #modifica notas
                    elif op1 == "3":
                        try:
                            alumno, materia, nota = input("ingrese: Alumno,materia,nota ").split(",")
                            if not alum.validarAlumno(alumno,materia,talumnos):
                                raise ValueError
                            else:
                                Profe.modificarNota(alumno, materia, Profe.validarNota(nota), talumnos)
                                lp()
                                guardar()
                                print(f"Se modifico la nota del alumno {alumno} correctamente")
                        except ValueError:
                            lp()
                            print("El Alumno ingresado no existe o no esta anotado para la materia nombrada")
                            continue

                    #elimina una nota de un alumno en una materia
                    elif op1 == "4":
                        try:
                            alumno, materia = input("ingrese: Alumno,materia ").split(",")
                            if not alum.validarAlumno(alumno,materia,talumnos):
                                raise ValueError
                            else:
                                Profe.eliminarNota(alumno,talumnos)
                                lp()
                                guardar()
                                print(f"Se elimino la nota del alumno {alumno} correctamente")
                        except ValueError:
                            lp()
                            print("El Alumno ingresado no existe o no esta anotado para la materia nombrada")
                            continue

                    elif op1 == "5":
                        alum.guardarAlumnos("alumnos.txt", talumnos)
                        lp()
                        c_prof = ""
                        c_profesor = ""
                        z = True

                    else:
                        lp()
                        print("Ingrese una opcion correcta.")
        except SyntaxError:
            lp()
            print("Datos incorrectos, por favor intente nuevamente")
            continue
        except ValueError:
            lp()
            print("Debe cargar todos los datos solicitados")
            continue

#valida los datos del encargado
    elif op == "2":
        try:
            nombre, dni = input("Ingrese:Nombre,DNI ").split(",")
            if Enca.validarEncargado(nombre,dni,tencargados) == 0:
                raise ValueError
            else:
                v = False
                lp()
                c_enc = alum.nombre_id(nombre,tencargados)
                c_encargado = tencargados[c_enc]
                #ingreso al menu encargado
                while not v:
                    print("#" * 20)
                    print(f"Bienvenido Encargado")
                    print("1_Inscribir Alumno")
                    print("2_Mostrar Alumnos")
                    print("3_Modificar Alumno")
                    print("4_Eliminar Alumno")
                    print("5_Volver al Menu anterior")
                    op2 = input("")
                    print("#" * 20)
                    #verifica si existe el alumno o si no lo agrega
                    if op2 == "1":
                        try:
                            fecha, alumno, materia, profesor, curso, division = input(
                                "ingrese: Fecha,Alumno,materia,profesor,curso,division ").split(",")
                            if alum.validarAlumno(alumno,materia,talumnos) == "1":
                                raise SyntaxError
                            else:
                                c_encargado.inscribirAlumno(fecha,alumno,materia,profesor,curso,division,talumnos)
                                lp()
                                guardar()
                                print(f"Se inscribio al alumno {alumno} en la materia {materia} correctamente.")
                        except SyntaxError:
                            lp()
                            print("El Alumno ingresado ya se encuentra anotado en esa materia")
                            continue
                        except ValueError:
                            lp()
                            print("Debe colocar todos los datos solicitados")
                            continue

                    elif op2 == "2":
                        lp()
                        alum.mostrarAlumnos(talumnos)

                    #modifica el alumno
                    elif op2 == "3":
                        try:
                            fecha, alumno, materia, profesor, curso, division = input(
                                "ingrese: Fecha,Alumno,materia,profesor,curso,division ").split(",")
                            if not alum.validarAlumno(alumno, materia,talumnos):
                                raise ValueError
                            else:
                                c_encargado.inscribirAlumno(fecha, alumno, materia, profesor, curso, division,talumnos)
                                lp()
                                guardar()
                                print(f"Se modifico el alumno {alumno} correctamente.")
                        except ValueError:
                            lp()
                            print("El Alumno ingresado no se encuentra inscripto.")
                            continue

                    elif op2 == "4":
                        try:
                            alumno, materia, = input(
                                "ingrese el alumno que desea eliminar: alumno,materia ").split(",")
                            if not alum.validarAlumno(alumno, materia,talumnos):
                                raise ValueError
                            else:
                                if alum.eliminarAlumno(alumno, talumnos):
                                    lp()
                                    guardar()
                                    print(f"Se elimino el alumno {alumno} correctamente.")
                                else:
                                    lp()
                                    print(f"No se pudo eliminar al alumno correctamente")
                        except ValueError:
                            lp()
                            print("El Alumno ingresado no se encuentra inscripto.")
                            continue

                    elif op2 == "5":
                        alum.guardarAlumnos("alumnos.txt",talumnos)
                        lp()
                        v = True
                    else:
                        lp()
                        print("Ingrese una opcion correcta.")
        except ValueError:
            lp()
            print("Datos Incorrectos, por favor intente nuevamente")
            continue

    elif op == "3":
        alum.guardarAlumnos("alumnos.txt", talumnos)
        lp()
        x = True

    elif op == "admin":
        alum.guardarAlumnos("alumnos.txt", talumnos)
        lp()
        try:
            user, passw = input("Ingrese usuario,contraseña: ").split(",")
            if admin.validarAdmin(user, passw):
                admin.menu_secreto(tencargados, tprofesores)
            else:
                print("Datos incorrectos, acceso denegado")
        except ValueError:
            print("Debe colocar los usuario y contraseña separados por una ','")

    else:
        lp()
        print("Ingrese una opcion correcta.")