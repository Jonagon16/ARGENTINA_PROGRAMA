punto = float(input("Ingrese su puntaje: "))
nivel = 2400
def sueldo(n):
    i = str(n)
    i = i.replace(".","")
    s = int(i) % 2
    return s

if punto == 0.0:
    print("Su rendimiento es inaceptable y su sueldo es de 0 pesos")
elif punto == 0.4:
    print("Su rendimiento es aceptable y su sueldo es de 960 pesos")
elif punto == 0.6:
    print("Su rendimiento meritorio y su sueldo es de 1440 pesos")
elif punto > 0.6 and sueldo(punto) == 0:
    print(f"Su rendimiento es meritorio y su sueldo es de {int(nivel*punto)} pesos")
else:
    print("ingrese un puntaje valido")




