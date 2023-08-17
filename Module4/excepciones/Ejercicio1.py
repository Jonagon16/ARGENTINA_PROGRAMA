c = list(input("Ingrese los datos con el siguiente formato clave,valor: ").split(","))
#creo un diccionario recorriendo la lista de dos en dos
l = {c[i]: c[i+1] for i in range(0, len(c), 2)}
cantidad = len(c)
x = False
#creo un loop solo si la lista c tiene almenos 2 elementos
while cantidad > 2 and not x:
    print("#"*20)
    print("Elija la opcion deseada")
    print("1_Insertar")
    print("2_Eliminar")
    print("3_Modificar")
    print("4_Mostrar Diccionario")
    print("5_Salir")
    op = input("")
    print("#" * 20)
#Opcion 1 inserta una clave y un valor en el diccionario
    if op == "1":
        j, k = input("ingrese clave,valor: ").split(",")
        # Si la clave esta en l crea el Keyerror
        try:
            if j in l.keys():
                raise KeyError
            else:
                l[j] = k
                print("se inserto correctamente")
        except KeyError:
            print("El valor ya existe desea modificar el valor, y/n ")
            w = input("")
            if w == "y":
                l[j] = k
                print("Se modifico correctamente")
            else:
                continue
#Opcion 2 elimina una clave del diccionario
    elif op == "2":
        j = input("Ingrese la clave que desea eleminar: ")
        try:
            l.pop(j)
            print("se elimino correctamente")
        except KeyError:
            print("La clave no existe")
            continue
#Opcion 3 modifica el diccionario
    elif op == "3":
        j, k = input("Ingrese clave,valor que desea modificar: ").split(",")
        #Si la clave no esta en l crea el Keyerror
        try:
            if j not in l.keys():
                raise KeyError
            else:
                l[j] = k
                print("se modifico correctamente")
        except KeyError:
            print("La clave no existe")
            continue
#Opcion 4 muestra el diccionario l
    elif op == "4":
        print(l)
#Opcion 5 salir
    elif op == "5":
        x = True



