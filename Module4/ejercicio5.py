edad = int(input("Ingrese su edad: "))

if edad < 4:
    print("Usted puede ingresar gratis")
elif edad >= 4  and edad <= 18:
    print("Su entrada vale 5 pesos")
elif edad > 18:
    print("Su entrada vale 10 pesos")