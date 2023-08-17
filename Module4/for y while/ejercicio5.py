l = list(input("ingrese una lista de elementos separados por espacios: ").split())
lt = []
for i in l:
    lt.append(i[::-1])
l = lt
print(f"Resultado: {l}")