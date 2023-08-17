import sys
num1 = int(sys.argv[1])
ano1 = ((num1*4)/100) + num1
ano2 = ((ano1*4)/100) + ano1
ano3 = ((ano2*4)/100) + ano2
print ("#########################################################################")
print (f"Usted a depositado la cantidad de ${num1} pesos en Cuenta N° 005524858")
print ("#########################################################################")
print ("##############################################################")
print (f"El saldo de su cuenta despues de un año es ${round(ano1, 2)} pesos")
print ("##############################################################")
print (f"El saldo de su cuenta despues de dos años es ${round(ano2, 2)} pesos")
print ("##############################################################")
print (f"El saldo de su cuenta despues de tres años es ${round(ano3, 2)} pesos")
print ("##############################################################")