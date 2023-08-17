renta = int(input("Ingrese su renta anual: "))

if renta < 10000:
    print("Su renta anual es del 5%")
elif renta >= 10000 and renta <= 19999:
    print("Su renta anual es del 15%")
elif renta >= 20000 and renta <= 34999:
    print("Su renta anual es del 20%")
elif renta >= 35000 and renta <= 59999:
    print("Su renta anual es del 30%")
elif renta >= 60000:
    print("Su renta anual es del 45%")
else:
    print("El dato es inválido")
