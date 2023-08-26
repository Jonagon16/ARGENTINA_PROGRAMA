import Perro
import Pez
perro = Perro.perro("EL gran pope")
pez = Pez.pez("pez ado")
lPerrosyPez = []
cantPerros = 0
cantPez = 0
x=False
while not x:
    print("#" * 20)
    print("ELIJE UN NRO")
    print("1_Agregar Perro")
    print("2_Agregar Pez")
    print("3_Mostrar Lista")
    print("4_Salir")
    opcion = input("")
    print("#" * 20)
    if opcion == "1":
        try:
            perroElejido = input("escribe la raza de tu perro:")
            perro.setRaza(perroElejido)
            lPerrosyPez.append(f"Perro {perroElejido}")
            cantPerros += 1
            print("Perro agregado correctamente")
        except ValueError:
            print("Debes colocar alguna raza")
    elif opcion == "2":
        try:
            pezElejido = input("escribe el tipo de agua de tu pez:")
            pez.setAgua(pezElejido)
            lPerrosyPez.append(f"Pez de {pezElejido}")
            cantPez += 1
            print("Pez agregado correctamente")
        except ValueError:
            print("Debes colocar alguna raza")
        except Pez.pezEquivocado as error:
            print(error)
    elif opcion == "3":
        print(f"Tienes una cantidad de {cantPerros}  Perros y una cantidad de {cantPez} peces")
        print(lPerrosyPez)
    elif opcion == "4":
        x=True
    else:
        print("Elija una numero valido")