d = input("Ingrese un diccionario: ")
e = input("Ingrese un elemento: ")

i = []
de = d.split(",")
dee = {i.split(":")[0]:i.split(":")[1] for i in de}
print(de)
print(dee)
j = 0
for k in dee.values():
    if k == e:
        j += 1
print(f"El elemento {e} aparece {j} veces en los valores del diccionario.")
