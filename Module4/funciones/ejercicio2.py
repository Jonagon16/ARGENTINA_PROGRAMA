def contarLetras(z):
    t = str.maketrans("ÁÉÍÓÚ", "AEIOU")
    a = z.upper().replace(" ","").translate(t)
    a = list(a)
    cc = {}
    for i in a:
        if i in cc:
            cc[i] += 1
        else:
            cc[i] = 1
    return cc


s = list(input("ingrese una lista de elementos separados por espacios: ").split())
print("#"*30)
for i in s:
    d = contarLetras(i)
    print(f"Palabra {i}, Resultado {d}")
    print("#"*30)

m = input("")