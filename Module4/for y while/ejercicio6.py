n = int(input("Ingrese la cantidad de elementos que desea ingresar: "))
l=dict()
dcl=""
dvl=""
sd=0
for i in range(n):
    c=(input("ingrese una clave(entero): "))
    v = (input("ingrese una valor(string): "))
    l[c] = v
    if len(v) > sd:
        sd = len(v)
        dcl = c
        dvl = v
print(f"Del siguiente diccionario {l} el valor mas largo es {dvl} que tiene como clave {dcl}")