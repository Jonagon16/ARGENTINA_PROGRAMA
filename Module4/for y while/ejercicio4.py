def vyc(z):
    #le robe su codigo jajajaj
    t = str.maketrans("ÁÉÍÓÚ", "AEIOU")
    a = z.upper().replace(" ","").translate(t)
    b = list(a)
    cv = []
    cc = []
    for i in b:
        if i in "AEIOU":
            cv.append(i)
        else:
            cc.append(i)
    return cv, cc


s = list(input("ingrese una lista de elementos separados por espacios: ").split())
for j in s:
    k,l = vyc(j)
    print(f"La palabra {j} contiene:")
    print(f"Consonantes: {l}")
    print(f"Volcales: {k}")
    print("#"*30)