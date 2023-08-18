z = False
d = ""

def sumar(dic):
    num=0
    for i in dic:
        i = i.strip("\n")
        i = int(i)
        num = num + i
    return num


while not z:
    try:
        fs = input("Ingrese el nombre del archivo que quiere abrir: ")
        with open(fs,"r") as f:
            fd = f.readlines()
            d = sumar(fd)
            z = True
    except FileNotFoundError:
        print("Archivo no encontrado.")

print(f"la suma de los numeros del archivo son: {d} ")