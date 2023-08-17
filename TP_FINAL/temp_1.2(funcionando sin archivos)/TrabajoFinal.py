import TDA_Profesores as Profe
import TDA_Encargado as Enca

trad = str.maketrans("ÁÉÍÓÚ", "AEIOU")
#s = s.upper().strip().translate(trad)
#diccionarios para desempaquetar archivos
cookiep = {}
cookiee = {}
cookiea = {}
temp_cookie = ""
profesores = {}
encargados = {}
alumnos = {}
tprofesores = {'jona':{'nombre':'jona','materia':'matematicas','curso':'A','division':'2'},
                'diana':{'nombre':'jona','materia':'matematicas','curso':'A','division':'2'},
                'diego':{'nombre':'jona','materia':'matematicas','curso':'A','division':'2'}
               }
tencargados = {'jona':'40','diana':'41'}
talumnos = {'jona':{'fecha':'12/12/12','nombre':'jona','profesor':'mario','materia':'matematicas','curso':'A','division':'2','nota':'-1'},
                'diana':{'fecha':'12/3/20','nombre':'diana','profesor':'mario','materia':'matematicas','curso':'A','division':'2','nota':'-1'},
                'diego':{'fecha':'12/6/21','nombre':'diego','profesor':'mario','materia':'matematicas','curso':'A','division':'2','nota':'-1'}
               }
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
    print("4_Mostrar Diccionario")
    print("3_Salir")
    op = input("")
    print("#" * 20)
#verifico si se eligio la opcion 1 y hago la vadilacion de datos
    if op == "1":
        nombre, materia, curso, division = input("Ingrese: Nombre,Materia,curso,division ").split(",")
        try:
            if Profe.validarProfesor(nombre,materia,curso,division,tprofesores) == 0:
                raise ValueError
            else:
                z = False
                cookiep={'nombre':nombre,'materia':materia}
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
                        alumno, materia, nota = input("ingrese: Alumno,materia,nota ").split(",")
                        try:
                            if Profe.validarAlumno(alumno,talumnos) == "0":
                                raise ValueError
                            else:
                                Profe.modificarNota(alumno,materia,nota,talumnos)
                                print(f"Se asigno la nota {nota} al alumno {alumno} correctamente")
                        except ValueError:
                            print("El Alumno ingresado no existe o no esta anotado para la materia nombrada")
                            continue
                    elif op1 == "2":
                        Profe.mostrarNotas(talumnos)
                    #modifica notas
                    elif op1 == "3":
                        alumno, materia, nota = input("ingrese: Alumno,materia,nota ").split(",")
                        try:
                            if Profe.validarAlumno(alumno,talumnos) == "0":
                                raise ValueError
                            else:
                                Profe.modificarNota(alumno, materia, nota, talumnos)
                                print(f"Se modifico la nota del alumno {alumno} correctamente")
                        except ValueError:
                            print("El Alumno ingresado no existe o no esta anotado para la materia nombrada")
                            continue
                    #elimina una nota de un alumno en una materia
                    elif op1 == "4":
                        alumno, materia = input("ingrese: Alumno,materia ").split(",")
                        try:
                            if Profe.validarAlumno(alumno,talumnos) == "0":
                                raise ValueError
                            else:
                                Profe.eliminarNota(alumno, materia,talumnos)
                                print(f"Se elimino la nota del alumno {alumno} correctamente")
                        except ValueError:
                            print("El Alumno ingresado no existe o no esta anotado para la materia nombrada")
                            continue
                    elif op1 == "5":
                        z = True
                    else:
                        print("Ingrese una opcion correcta.")
        except ValueError:
            print("No se encontraron datos, por favor intente nuevamente")
            continue
#valida los datos del encargado
    elif op == "2":
        nombre, dni = input("Ingrese:Nombre,DNI ").split(",")
        try:
            if Enca.validarEncargado(nombre,dni,tencargados) == 0:
                raise ValueError
            else:
                v = False
                cookiee = {'nombre': nombre, 'dni': dni}
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
                        fecha, alumno, materia, profesor, curso, division = input("ingrese: Fecha,Alumno,materia,profesor,curso,division ").split(",")
                        try:
                            if Enca.validarAlumno(alumno,materia,talumnos) == "1":
                                raise ValueError
                            else:
                                Enca.inscribirAlumno(fecha,alumno,materia,profesor,curso,division,talumnos)
                                print(f"Se inscribio al alumno {alumno} en la materia {materia} correctamente.")
                        except ValueError:
                            print("El Alumno ingresado ya se encuentra anotado en esa materia")
                            continue
                    elif op2 == "2":
                        Enca.mostrarAlumnos(talumnos)
                    #modifica el alumno
                    elif op2 == "3":
                        fecha, alumno, materia, profesor, curso, division = input(
                            "ingrese: Fecha,Alumno,materia,profesor,curso,division ").split(",")
                        try:
                            if Enca.validarAlumno(alumno, materia,talumnos) == "0":
                                raise ValueError
                            else:
                                Enca.inscribirAlumno(fecha, alumno, materia, profesor, curso, division,talumnos)
                                print(f"Se modifico el alumno {alumno} correctamente.")
                        except ValueError:
                            print("El Alumno ingresado no se encuentra inscripto.")
                            continue
                    elif op2 == "4":
                        alumno, materia, = input(
                            "ingrese el alumno que desea eliminar: alumno,materia ").split(",")
                        try:
                            if Enca.validarAlumno(alumno, materia,talumnos) == "0":
                                raise ValueError
                            else:
                                Enca.eliminarAlumno(alumno, materia,talumnos)
                                print(f"Se elimino el alumno {alumno} correctamente.")
                        except ValueError:
                            print("El Alumno ingresado no se encuentra inscripto.")
                            continue
                    elif op2 == "5":
                        v = True
                    else:
                        print("Ingrese una opcion correcta.")
        except ValueError:
            print("No se encontraron datos, por favor intente nuevamente")
            continue
    elif op == "3":
        x = True
    else:
        print("Ingrese una opcion correcta.")
#ya funciona sin archivos
#falta realizar el translate para sacar los acentos espacios en blanco.
#falta el admin
#falta abrir el archivo y leer