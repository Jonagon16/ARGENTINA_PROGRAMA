print("Ingrese los datos con el siguiente formato clave:valor,clave:valor")
a = input("Ingrese el diccionario a: ")
b = input("Ingrese el diccionario b: ")
s_a = set(a.split(","))
s_b = set(b.split(","))
u = (s_a | s_b)
i = (s_a & s_b)
d = (s_a - s_b)
ds = (s_a ^ s_b)
print("unión (u): ", u)
print("Intersección (i): ", i)
print("Diferencia (d): ", d)
print("Diferencia simétrica (ds): ", ds)