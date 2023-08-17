p = {}
o = 0

while o < 3:
    c = input("Ingrese sus datos en el siguiente formato DNI:NOMBRE,DOMICILIO,EDAD: ")
    de = c.split(":")
    dni = de[0]
    nombre, domicilio, edad = de[1].split(",")
    p[dni] = {
        'nombre': nombre,
        'domicilio': domicilio,
        'edad': edad
    }
    o += 1

print("\nInformación de las personas registradas:")
for dni, d in p.items():
    nombre = d['nombre']
    domicilio = d['domicilio']
    edad = d['edad']
    print(f"DNI: {dni}")
    print(f"Nombre: {nombre}")
    print(f"Domicilio: {domicilio}")
    print(f"Edad: {edad}")
    print("#################################################\n")
