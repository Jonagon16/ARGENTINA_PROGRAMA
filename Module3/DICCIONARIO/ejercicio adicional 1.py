p = {}
c = input("Ingrese sus datos en el siguiente formato Nif;NyA;Email;Telefono;descuento/n: ")
de = c.split("/n")
for i in range(len(de)):
    nif, nombre, email, telefono, descuento = de[i].split(";")
    p[nif] = {
        'nombre': nombre,
        'email': email,
        'telefono': telefono,
        'descuento': float(descuento)
    }
print(p)

