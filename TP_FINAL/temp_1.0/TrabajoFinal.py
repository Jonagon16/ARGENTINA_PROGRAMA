import TDA_Profesor as Profe
import TDA_Encargado as Enca
x = False
z = False
v = False
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
            if not Profe.validarProfesor(nombre,materia,curso,division) == 1:
                raise ValueError
            else:
                #ingreso al menu profesor
                while not z:
                    print("#" * 20)
                    print("Bienvenido Profesor ")
                    print("1_Cargar Notas")
                    print("2_Mostrar Notas")
                    print("2_Modificar notas Notas")
                    print("3_Volver al Menu anterior")
                    op1 = input("")
                    print("#" * 20)
                    #verifica si existe el alumno y si existe lo modifica
                    if op1 == "1":
                        alumno, materia, nota = input("ingrese: Alumno,materia,nota").split(",")
                        try:
                            if Profe.validarAlumno(alumno) == "0":
                                raise ValueError
                            else:
                                Profe.modificarNota(alumno,materia,nota)
                        except ValueError:
                            print("El Alumno ingresado no existe o no esta anotado para la materia nombrada")
                            continue
                    if op1 == "2":
                        Profe.mostrarNotas()
                    if op1 == "3":
                        z = True
        except ValueError:
            print("No se encontraron datos, por favor intente nuevamente")
            continue
#valida los datos del encargado
    if op == "2":
        nombre, dni = input("Ingrese:Nombre,DNI ").split(",")
        try:
            if not Enca.validarEncargado(nombre,dni) == 1:
                raise ValueError
            else:
                #ingreso al menu encargado
                while not v:
                    print("#" * 20)
                    print("Bienvenido Encargado ")
                    print("1_Inscribir Alumnos")
                    print("2_Mostrar Alumnos")
                    print("3_Volver al Menu anterior")
                    op1 = input("")
                    print("#" * 20)
                    #verifica si existe el alumno o si no lo agrega
                    if op1 == "1":
                        fecha, alumno, materia, profesor, curso, division = input("ingrese: Fecha,Alumno,materia,profesor,curso,division ").split(",")
                        try:
                            if Enca.validarAlumno(alumno,materia) == "1":
                                raise ValueError
                            else:
                                Enca.inscribirAlumno(fecha,alumno,materia,profesor,curso,division)
                        except ValueError:
                            print("El Alumno ingresado ya se encuentra anotado en esa materia")
                            continue
                    if op1 == "2":
                        Enca.mostrarAlumnos()
                    if op1 == "3":
                        v = True
        except ValueError:
            print("No se encontraron datos, por favor intente nuevamente")
            continue
#falta la opcion de cargar o elminar alumnos o notas
#falta los tda de profe y enca
#falta abrir el archivo y leer