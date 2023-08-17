l = input("ingrese varios numeros separados por una ',': ")
li = l.split(",")
v = int(input("ingrese un numero: "))
a = []
b = []
for i in range(len(li)):
    if type(li[i]) == str:
        li[i] = int(li[i])
    a.append(li[i] + v)
    b.append(li[i] - v)
t = tuple(li)
s = tuple(a)
r = tuple(b)
print (f"La tupla contiene los numeros {t}")
print (f"La tupla mas el valor {v} es igual a {s}")
print (f"La tupla menos el valor {v} es igual a {r}")
