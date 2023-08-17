l=[34, 3.2, "Juan", "Pedro",-2]
print("INCISO 1")
print (l)
s=input("ingrese un string: ")
l.append(s)
print(l)
print("#"*50)
print("INCISO 2")
elemento= input("ingrese el elemento que quiere buscar: ")
veces = 0
#iteramos la cantidad de elemento de la lista l
for i in range(len(l)):
#verificamos si existe un entero o flotante lo convertimos a string
    if type(l[i]) == int or type(l[i]) == float:
        l[i] = str(l[i])
#imprimimos la cantidad resultante
print (f"El elemento {elemento} se repite {l.count(elemento)} ")
print("################################################")
print("INCISO 3")
s = input("ingrese los elementos que quiera agregar separados por una ',' : ")
sa = s.split(",")
l.extend(sa)
print(l)
print("################################################")
input("ingrese una tecla para continuar y luego enter: ")
print("INCISO 4")
l.reverse()
print(l)