import RenglonDeFactura
import Factura
import datetime
import DATOS
nroFacturasCar = 0
totalfact = 0
totalfacttemp=0
totalFacttotal = 0
iva=lambda num:num*21/100
nfc = False
mercaderiaD = []
nroF = 0
nroM = 0
fFinal=[]
v = 0
x=False
pf=lambda x,y:x*y
while not x:
    print("#" * 60)
    print("Bienvenido a su Sistema de Factura el QUIQUE")
    print("1_Guardar Ticket Automatico")
    print("2_Mostrar Tickets")
    print("3_Imprimir total de ventas")
    print("4_Cliente de mes")
    print("5_Salir")
    opcion = input("")
    print("#" * 60)
    if opcion == "1":
        try:
            v += 1
            totalfact = 0
            mercaderiaD=[]
            nroFactura = input("Ingrese su nro de factura: ")
            nroFacturasCar += 1
            nfc = True
            nomEmpresa = input("Ingrese nombre de la empresa: ")
            cantproductos = int(input("ingrese la cantidad de productos comprados: "))
            for u in range(cantproductos):
                nummer = f"mercaderia{u}"
                mercaderiaD.append(nummer)
            for i in range(cantproductos):
                mercaderia = input("Ingrese la mercaderia: ")
                cantMercaderia = input(f"Ingrese la cantidad comprada de {mercaderia}: ")
                precio = input(f"Ingrese precio por unidad de {mercaderia}: ")
                nuevaMerc = RenglonDeFactura.renglonDeFactura(int(cantMercaderia),mercaderia,int(precio))
                mercaderiaD.append(nuevaMerc)
                totalfact = int(totalfact) + (int(cantMercaderia)*int(precio))
            nombrePer = input("Ingrese nombre del cliente: ")
            dniPersona = input("Ingrese el DNI o CUIL: ")

            fF = Factura.factura(int(nroFactura), nomEmpresa,nombrePer,dniPersona,datetime.datetime.now())
            fFinal.append(fF)
            fFinal[0].setMerComprada(cantproductos)
            for i in range(len(mercaderiaD)):
                fFinal[0].setMercaderia(mercaderiaD[i])

            print(mercaderiaD)

        except ValueError:
            print("Se le ha olvidado de colocar un dato, intente nuevamente")
    elif opcion == "2":
        if nfc:
            fFinal[0].imprimirFactura(mercaderiaD)
            print("¿Desea imprimir el ticket? Y/N ")
            op=input("")
            print("#"*60)
            if op.lower() == "y":
                DATOS.guardarmerc("prueba.txt")
        else:
            print("No existe tickets guardados")

    elif opcion == "3":
        print(f"El total del dia de la fecha fue de: {totalFacttotal}")

    elif opcion == "4":
        print(f"El Cliente que realizo la compra mas buena fue: {personas[0]} con un total comprado de {personas[1]}")

    elif opcion == "5":
        x=True
    else:
        print("Elija una numero valido")