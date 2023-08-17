ln =[]
a =input("Ingrese una lista de valores en el siguiente formato 'Nombre,edad,Nombre,Edad': ")
ab = a.split(",")
ln = [(ab[i], ab[i+1]) for i in range(0, len(ab), 2)]
print (ln)
d = {x[0]: int(x[1]) for x in ln}
print(d)



