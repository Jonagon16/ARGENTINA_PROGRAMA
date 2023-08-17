eUno = input("ingrese el nombre de un equipo y cuantos goles realizo ej river:15 ")
eDos = input("ingrese el nombre de un equipo y cuantos goles realizo ej boca:0 ")
i = eUno.split(":")
j = eDos.split(":")
if int(i[1]) > int(j[1]):
    print (f"Gano el equipo {i[0]} resultando el partido en {i[1]} - {j[1]}")
elif int(i[1]) < int(j[1]):
    print (f"Gano el equipo {j[0]} resultando el partido en {j[1]} - {i[1]}")
else:
    print (f"Ambos equipos empataron resultando el partido en {j[1]} - {i[1]}")
