import RenglonDeFactura
import Factura
import datetime
def guardarmerc(arc):
    with open(arc,"w") as archivo:
        for i, j in Facturafinal.items():
            archivo.write("#" * 60)
            archivo.write(f"\nRazon Social: {j['Nombre exit de empresa']}                              #{j['Hora']}#\n")
            archivo.write(f"Numero de Facturacion: {j['Numero de factura']}\n")
            archivo.write(f"Nombre: {j['Persona']}, CONSUMIDOR FINAL\n")
            archivo.write(f"DNI/CUIL: {j['Dni']}\n")
            archivo.write("#" * 60)
            archivo.write("\nDETALLE DE LA COMPRA\n")
            archivo.write(f"{'Producto':<10}{'Cantidad':<8}{'Precio/u':<10}{'Total':<10}\n")
            for k, l in j['mercaderia'].items():
                cantidad = int(l['Cantidad comprada'])
                precio = float(l['Precio por unidad'])
                total = cantidad * precio
                archivo.write(f"{k:<10}{cantidad:<8}{precio:<10.2f}{total:<10.2f}\n")
            archivo.write(f"Importe Total\n")
            archivo.write(f"Es un total de {j['total']} sin IVA.\n")
            archivo.write(f"Es un total de {iva(j['total']) + j['total']} con IVA.\n")
            archivo.write(f"Total de recargo de IVA {iva(j['total'])}\n")
            archivo.write(f"#" * 60)


Facturafinal = {}
nroFacturasCar = 0
totalfact = 0
totalfacttemp=0
totalFacttotal = 0
iva=lambda num:num*21/100
nfc = False
personas = ["",0]
mercaderiaD = {}


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
            totalfact = 0
            mercaderiaD={}
            nroFactura = input("Ingrese su nro de factura: ")
            nroFacturasCar += 1
            nfc = True
            nomEmpresa = input("Ingrese nombre de la empresa: ")
            cantproductos = int(input("ingrese la cantidad de productos comprados: "))
            for i in range(cantproductos):
                mercaderia = input("Ingrese la mercaderia: ")
                cantMercaderia = input(f"Ingrese la cantidad comprada de {mercaderia}: ")
                precio = input(f"Ingrese precio por unidad de {mercaderia}: ")
                mercaderiaD[mercaderia] = {'cantidad de mercaderia':cantMercaderia, 'precio':precio}
                totalfact = int(totalfact) + (int(cantMercaderia)*int(precio))
            totalFacttotal = int(totalFacttotal) + int(totalfact)
            nombrePer = input("Ingrese nombre del cliente: ")
            dniPersona = input("Ingrese el DNI o CUIL: ")
            if totalfact > personas[1]:
                personas= [nombrePer,totalfact]
            #fFinal = Factura.factura(nroFactura, nomEmpresa, mercaderia, cantmercaderiatotal)
            #renglonFactura = RenglonDeFactura.renglonDeFactura(cantmercaderiatotal, mercaderia,
            #                                                  mercaderiaD[mercaderia]['precio'])
            Facturafinal [nroFactura]= {'Numero de factura':nroFactura,
                                        'Nombre de empresa':nomEmpresa,
                                        'Persona':nombrePer,
                                        'Dni':dniPersona,
                                        'mercaderia':{},
                                        'total':totalfact,
                                        'Hora':datetime.datetime.now()}
            for i, j in mercaderiaD.items():
                Facturafinal[nroFactura]['mercaderia'][i] = {'Cantidad comprada': j['cantidad de mercaderia'],
                                               'Precio por unidad': j['precio']}
            print(Facturafinal)
            print(mercaderiaD)

        except ValueError:
            print("Se le ha olvidado de colocar un dato, intente nuevamente")
    elif opcion == "2":
        if nfc:
            for i,j in Facturafinal.items():
                print("#"*60)
                print(f"Razon Social: {j['Nombre de empresa']}                              #{j['Hora']}#")
                print(f"Numero de Facturacion: {j['Numero de factura']}")
                print(f"Nombre: {j['Persona']}, CONSUMIDOR FINAL")
                print(f"DNI/CUIL: {j['Dni']}")
                print("#"*60)
                print("DETALLE DE LA COMPRA")
                print(f"{'Producto':<10}{'Cantidad':<8}{'Precio/u':<10}{'Total':<10}")
                for k, l in j['mercaderia'].items():
                    cantidad = int(l['Cantidad comprada'])
                    precio = float(l['Precio por unidad'])
                    total = cantidad * precio
                    print(f"{k:<10}{cantidad:<8}{precio:<10.2f}{total:<10.2f}")
                print(f"Importe Total")
                print(f"Es un total de {j['total']} sin IVA.")
                print(f"Es un total de {iva(j['total'])+j['total']} con IVA.")
                print(f"Total de recargo de IVA {iva(j['total'])}")
                print(f"#"*60)
                print("¿Desea imprimir el ticket? Y/N ")
                op=input("")
                print("#"*60)
                if op.lower() == "y":
                    guardarmerc("prueba.txt")
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