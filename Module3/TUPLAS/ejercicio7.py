li = input("ingrese los numero separados por una ',' ")
l = li.split(",")
t= tuple(l)
print(t)
elemento = input("ingrese el numero que quiere buscar: ")
a = "no se encuentra" if t.count(elemento) == 0 else "si se encuentra"
print(f"El elemento {elemento} {a} dentro de la tupla")