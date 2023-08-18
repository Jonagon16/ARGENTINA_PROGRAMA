z = False
d = []


while not z:
    try:
        fs = input("Ingrese el nombre del archivo que quiere abrir: ")
        with open(fs,"r") as f:
            fd = f.readlines()
            d = fd[::-1]
        with open(fs, "w") as f:
            f.write("")
        for i in range(len(d)):
            print(f"{d[i]}")
            with open(fs,"a") as f:
                f.write(f"{d[i]}")
                z = True

    except FileNotFoundError:
        print("Archivo no encontrado.")

print(f"el archivo quedario asi: {d} ")