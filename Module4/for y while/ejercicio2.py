n = int(input("Ingrese la cantidad de string que desea ingresar: "))
l=[]
sml=""
sd=0
for i in range(n):
    s=(input("ingrese el string: "))
    l.append(s)
    if len(s) > sd:
        sd = len(s)
        sml = s
print(f"De los siguientes strings {l} el mas largo es {sml}")