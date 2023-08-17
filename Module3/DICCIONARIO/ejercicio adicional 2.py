j = input("Ingrese una frase: ")
j = j.replace(" ", "")
h = list(j)
d = {i for i in h}
print(d)


def c_letras(i):
    c = {}
    o = ""
    s = 0
    for j in i:
        if j in c:
            c[j] += 1
        else:
            c[j] = 1
        if c[j] > s:
            s = c[j]
            o = j
    return c, o, s


letras, letra, veces = c_letras(h)
print(letras)
print(f"La letra que mas se repite es {letra} y se repite {veces}")
