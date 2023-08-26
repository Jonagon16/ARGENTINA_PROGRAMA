def guardarmerc(arc):
    with open(arc,"w") as archivo:
        for i, j in Facturafinal.items():
            archivo.write("#" * 60)
            archivo.write(f"\nRazon Social: {j['Nombre de empresa']}                              #{j['Hora']}#\n")
            archivo.write(f"Numero de Facturacion: {j['Numero de factura']}\n")
            archivo.write(f"Nombre: {j['Persona']}, CONSUMIDOR FINAL\n")
            archivo.write(f"DNI/CUIL: {j['Dni']}\n")
            archivo.write("#" * 60)
            mercaderiaD={'Harina':{'cantidad de mercaderia':10,'precio':50}, 'matecocido':{'cantidad de mercaderia':13,'precio':40}}
            archivo.write("\nDETALLE DE LA COMPRA\n")
            archivo.write(f"{'Producto':<10}{'Cantidad':<8}{'Precio/u':<10}{'Total':<10}\n")
            for producto, detalles in mercaderiaD.items():
                cantidad = int(detalles['cantidad de mercaderia'])
                precio = float(detalles['precio'])
                total = cantidad * precio
                archivo.write(f"{producto:<10}{cantidad:<8}{precio:<10.2f}{total:<10.2f}\n")
            archivo.write(f"Importe Total\n")
            archivo.write(f"Es un total de {totalfact} sin IVA.\n")
            archivo.write(f"Es un total de {iva(totalfact) + totalfact} con IVA.\n")
            archivo.write(f"Total de recargo de IVA {iva(totalfact)}\n")
            archivo.write(f"#" * 60)

guardarmerc("prueba.txt")
