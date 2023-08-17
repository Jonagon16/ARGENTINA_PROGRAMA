import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])
#Calculamos la altura donde num1 es la hipotenusa
altura= (num3*num2) / num1
print ("##################################")
print (f"El Area del triangulo es: {num1*altura/2}")
print ("##################################")
print (f"La Perimetro del triagulo es: {num1+num2+num3}")