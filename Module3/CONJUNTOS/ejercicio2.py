u = {i for i in range(1,21)}
print(u)
a = set(input("Ingrese un conjunto de datos: "))
b = set(input("Ingrese otro conjunto de datos: "))
union = (a | b)
interS = a & b
print(f"La union entre los dos conjuntos es: {union}")
print(f"La interseccion entre los dos conjuntos es: {interS}")
print(f"El complemento entre la Union y la Interseccion de los dos conjuntos es conjuntos es: {union - interS}")