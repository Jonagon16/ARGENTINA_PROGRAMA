li = input("ingrese los numero separados por una ',' ")
l = li.split(",")
print("################################################")
elemento= int(input("ingrese el numero que quiere buscar: "))
for i in range(len(l)):
    if type(l[i]) == str:
        l[i] = int(l[i])
t = tuple(l)
v = t.count(elemento)
ve = "vez" if v == 1 else "veces"
print (f"El numero {elemento} se repite {v} {ve} en la tupla {t}")
print("################################################")

