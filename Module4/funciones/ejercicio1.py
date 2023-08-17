def pares (l):
    lp=[]
    for i in l:
        if int(i) % 2 == 0:
            lp.append(int(i))
    return lp

def impares (l):
    lip=[]
    for i in l:
        if int(i) % 2 != 0:
            lip.append(int(i))
    return lip

def mayoria(lp,lip):
    r=""
    if len(lp) == len(lip):
        r="En las dos listas hay igual cantidad de elementos"
    elif len(lp) > len(lip):
        r="Existen mas numeros pares que impares"
    elif len(lp) < len(lip):
        r="Existen mas numeros impares que pares"
    return r

l = list(input("ingrese una lista de nro separados por espacios ").split())
lp = pares(l)
lip = impares(l)
print(f"numeros pares: {lp}")
print(f"numeros Impares: {lip}")
print(mayoria(lp,lip))
m = input ("")
