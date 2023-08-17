l = [10,"hola", 2.5, 20,"que", 3.5, 30,"tal", 4.5]
print (l[6])
print (l[1])
print (l[0:3])
#declaro listas vacias
sStr = []
sFloat = []
sInt = []
# obtengo cada item de la lista l
for i in l:
#La primer forma la hice con type(), verifico si el tipo de dato i es un String
    if type(i) == str:
        sStr.append(i)
# y la segunda forma use isinstance(), verifico si el tipo de dato es un flotante
    elif isinstance(i,float):
        sFloat.append(i)
    elif isinstance(i, int):
        sInt.append(i)
print (sStr)
print (sFloat)
print (sInt)


