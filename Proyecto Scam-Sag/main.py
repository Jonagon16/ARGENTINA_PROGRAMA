def recibir_antecedente():
    ant={}
    with open("antecedente_salida.txt", 'r') as archivo:
        for linea in archivo:
            partes = linea.split(' : ')
            if len(partes) == 2:
                clave, valor = partes
                ant[clave.strip()] = valor
            else:
                print(f"Formato incorrecto en la línea: {linea.strip()}")
    return ant
def formatear_mensaje_reducido(diccionario):
    claves_mostradas = ["Dominio", "Motor", "Chasis", "Marca", "Modelo", "Titular", "Denuncia"]
    mensaje = ""
    for clave in claves_mostradas:
        valor = diccionario.get(clave, "")  # Obtén el valor de la clave o cadena vacía si no existe
        if valor.strip() != "":
            mensaje += f"{clave} : {valor}\n"

    # Elimina el último carácter de nueva línea adicional si es necesario
    if mensaje.endswith('\n'):
        mensaje = mensaje[:-1]

    return mensaje

a = recibir_antecedente()
b= formatear_mensaje_reducido(a)
print(a)
print(b)