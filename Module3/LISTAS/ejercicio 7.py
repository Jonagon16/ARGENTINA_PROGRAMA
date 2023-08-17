l = (input("ingrese varios elementos separados por una ',' : "))
li = list(l.split(","))
for i in range(len(li)):
    if type(li[i]) == str:
        li[i] = int(li[i])
li.sort()
mayor = max(li)
menor = min(li)
print(f"La lista contiene los siguientes numeros: {li}")
print(f"El numero mas grande es {mayor}")
print(f"El numero mas chico es {menor}")