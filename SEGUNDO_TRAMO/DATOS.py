import datetime

def guardarmerc(arc,Facturafinal):
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

def aumentar(nro):
    nro = nro +1

