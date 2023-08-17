import os
d = {'40211345':{'dni':'40211345','nombre':'Jonathan','domicilio':'bouchard'},'41154684':{'dni':'41154684','nombre':'Diana','domicilio':'bouchard'}}
v = {'milei':0,'massa':0,'larreta':0,'bullrich':0}
op3 = False
lseg = ["¿Estás seguro de eso?","¿Estás completamente seguro?","¿Tienes la certeza?","¿Estás convencido?","¿Estás seguro de lo que estás diciendo?","¿Estás seguro de lo que vas a hacer?","¿Estás absolutamente seguro?","¿Estás 100% seguro?","¿Estás seguro de que es la decisión correcta?","¿Tienes alguna duda al respecto?","¿Estás seguro de que no quieres reconsiderar?","¿Estás seguro de que lo comprendes todo?","¿Estás seguro de que no te equivocaste?","¿Estás seguro de que no quieres pensarlo de nuevo?","¿Estás seguro de que estás preparado para eso?","Si estas muy seguro escribe 'muy seguro' para continuar..."]
seg = iter(lseg)
cookie = ""
def limpiarDni(s):
    s = s.replace(".","")
    return s

def lp():
    os.system('cls' if os.name == 'nt' else 'clear')

def votar (s):
    if s == "1":
        v['milei'] += 1
    elif s == "2":
        v['massa'] += 1
    elif s == "3":
        v['larreta'] += 1
    elif s == "4":
        v['bullrich'] += 1

def cargarPersona(dni,nombre,domicilio):
    d[dni] = {
        'dni': limpiarDni(dni),
        'nombre': nombre,
        'domicilio': domicilio
    }

def modificarPersona(dni,nombre,domicilio):
    d[dni] = {
        'dni': limpiarDni(dni),
        'nombre': nombre,
        'domicilio': domicilio
    }

def eliminarPersona(dni):
    d.pop(dni)

def mostrarPersonas(dic):
    print(f"Personas anotadas en el padron {len(dic)}")
    for i,j in dic.items():
        print("#"*20)
        print(f"Dni: {i}")
        print(f"Nombre: {j['nombre']}")
        print(f"Domicilio: {j['domicilio']}")
    return
c = False
while not c:
    print(cookie)
    print("#"*20)
    print("Bienvenido al Padron Electoral Argentino")
    print("1_Cargar Persona")
    print("2_Modificar Persona")
    print("3_Mostrar Personas")
    print("4_Eliminar Persona")
    print("5_Votar")
    print("6_Salir")
    op = input("")
    print("#" * 20)
    cookie = ""
    if op == "1":
        try:
            dni, nombre, domicilio = input("Ingrese: Dni,Nombre,Domicilio ").split(",")
            if dni in d:
                raise KeyError(f"La persona {nombre} ya se encuentra en el padron ")
            else:
                cargarPersona(dni,nombre, domicilio)
                cookie = "Se cargo en el padron la persona correctamente"
                lp()
        except ValueError as e2:
            lp()
            print("Debe colocar todos los datos")

        except KeyError as e1:
            lp()
            print(f"Error:{e1}, ¿desea modificarlo? y/n")
            ope = input("")
            if ope == "y":
                modificarPersona(limpiarDni(dni),nombre,domicilio)
    elif op == "2":
        try:
            dni, nombre, domicilio = input("Ingrese: Dni,Nombre,Domicilio ").split(",")
            if dni in d:
                modificarPersona(limpiarDni(dni), nombre, domicilio)
                cookie = "Se modifico la persona Correctamente"
                lp()
            else:
                raise KeyError(f"La persona no se encuentra en el padron ")
        except KeyError as e1:
            lp()
            print(f"Error:{e1}")
        except ValueError as e2:
            lp()
            print("Debe colocar todos los datos")
    elif op == "3":
        lp()
        mostrarPersonas(d)
    elif op =="4":
        try:
            dni = input("Ingrese el Dni de la persona que quiere eliminar:  ")
            if limpiarDni(dni) in d:
                eliminarPersona(dni)
                cookie = "Se elimino la persona correctamente"
                lp()
            else:
                raise KeyError(f"La persona no se encuentra en el padron ")
        except KeyError as e1:
            lp()
            print(f"Error:{e1}")

        except ValueError as e2:
            lp()
            print("Debe colocar algun Dni")

    elif op == "5":
            dni = input("Ingrese su DNI: ")
            if dni in d:
                lp()
                r = False
                while not r:
                    print("#" * 20)
                    print(f"Bienvenido Argentino")
                    print("1_Votar a Milei")
                    print("2_Votar a Massa")
                    print("3_Votar a Larreta")
                    print("4_Votar a Bullrich")
                    print("5_Mostrar Resultados")
                    print("6_Volver al Menu anterior")
                    op2 = input("")
                    print("#"*20)
                    if op2 == "1":
                        votar(op2)
                        lp()
                        print("Excelente opcion")
                    elif op2 == "2":
                        while not op3:
                            op4 = input(f"{next(seg)}: ")
                            if op4 == "muy seguro":
                                votar(op2)
                                break
                    elif op2 == "3":
                        votar(op2)
                        lp()
                        print("Sos una persona de gustos excentricos, pero no discrimino")
                    elif op2 == "4":
                        votar(op2)
                        lp()
                        print("Excelente opcion")
                    elif op2 == "5":
                        lp()
                        print(f"Votos a Milei:{v['milei']}")
                        print(f"Votos a Massa:{v['massa']}")
                        print(f"Votos a Larreta:{v['larreta']}")
                        print(f"Votos a Bullrich:{v['bullrich']}")
                    elif op2 == "6":
                        lp()
                        r = True
                    else:
                        lp()
                        print("ingrese una opcion correcta")
            else:
                lp()
                cookie = "Usted no se encuentra en el padron"
                continue
    elif op == "6":
        c = True
    else:
        lp()
        cookie = "Ingrese una opcion correcta"