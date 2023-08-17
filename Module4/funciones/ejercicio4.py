def coordenadaZ ( x , y ) :
    x = x + 10
    y = y + 15
    return x+y
#programa p r i n c i p a l
x = int (input ( " Coordenada␣ ej e ␣x : ␣" ) )
y=int (input ( " Coordenada␣ ej e ␣y : ␣" ) )
for i in range ( 3 ) :
    z=coordenadaZ ( x , y )
    x=x+1
    y=y+1
    print ( x , "␣ . ␣" , y , "␣ . ␣" , z )
print("El programa hace lo siguiente:")
print("1.Pide dos numeros al usuario")
print("2.Mediante a la funcion coordenadaZ(), se le suma 10 al primer nro y 15 al segundo luego retorna la suma entre los dos")
print("3.En un bucle que se repite 3 veces imprime z que es es la funcion coordenadaZ y el primer nro aumentado en 1 y el segundo aumentado en 1")
m = input("")