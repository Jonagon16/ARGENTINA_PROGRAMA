z = False
d = {}

def contar(dic):
    df = {}
    for i in dic:
        i = i.strip("\n")
        if i in df:
            df[i] += 1
        else:
            df[i] = 1
    return df


def contarCinco(dic):
    temp1 = ["",1]
    temp2 = ["",1]
    temp3 = ["",1]
    temp4 = ["",1]
    temp5 = ["",1]
    l=[]
    for i,j in dic.items():
        if j > temp1[1]:
            temp5 = temp4
            temp4 = temp3
            temp3 = temp2
            temp2 = temp1
            temp1 = [i,j]
        elif int(j) > int(temp2[1]):
            temp5 = temp4
            temp4 = temp3
            temp3 = temp2
            temp2 = [i,j]
        elif j > temp3[1]:
            temp5 = temp4
            temp4 = temp3
            temp3 = [i,j]
        elif j > temp4[1]:
            temp5 = temp4
            temp4 = [i,j]
        elif j > temp5[1]:
            temp5 = [i,j]
    l = [temp1,temp2,temp3,temp4,temp5]
    return l


while not z:
    try:
        fs = input("Ingrese el nombre del archivo que quiere abrir: ")
        with open(fs,"r") as f:
            fd = f.readlines()
            d = contar(fd)
            z = True
    except FileNotFoundError:
        print("Archivo no encontrado.")
p = contarCinco(d)
print(p)
print(f"las palabras que mas se repitieron son:") #{p} de las siguientes palabras {d}")
for i in p:
    print(f"'{i[0]}' un total de {i[1]} veces")
print(f"de las palabras {d}")
