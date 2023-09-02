iva=lambda num:num*21/100

class cantIns(Exception):
    def __init__(self, mensaje= "El valor ingresado no puede ser 0"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
class factura:
    def __init__(self,nroFactura=0,empresa="", cliente="",dni=0,hora=0):
        if nroFactura > 0:
            self.nroFactura = nroFactura
            self.empresa = empresa
            self.mercaderia = []
            self.merComprada = 0
            self.cliente = cliente
            self.dnicliente = dni
            self.hora = hora

        else:
            raise cantIns

    def setNroFactura(self,nroFactura):
        self.nroFactura = nroFactura

    def setEmpresa(self,empresa):
        self.empresa = empresa

    def setMercaderia(self,mercaderia):
        self.mercaderia.append(mercaderia)
        self.merComprada += 1

    def setCliente(self,cliente):
        self.cliente = cliente

    def setDniCliente(self,dni):
        self.dnicliente = dni

    def setMerComprada(self,merComprada):
        self.merComprada = merComprada

    def getNroFactura(self):
        return self.nroFactura

    def getEmpresa(self):
        return self.empresa

    def getMercaderia(self):
        return self.mercaderia

    def getMerComprada(self):
        return self.merComprada

    def getCliente(self):
        return self.cliente

    def getDniCliente(self):
        return self.dnicliente

    def imprimirFactura(self,mercaderia):
        print("#" * 60)
        print(f"Razon Social: {self.empresa}{' ' * 37}#{self.hora}#")
        print(f"Numero de Facturacion: {self.nroFactura}")
        print(f"Nombre: {self.cliente}, CONSUMIDOR FINAL")
        print(f"DNI/CUIL: {self.dnicliente}")
        print("#" * 60)
        print("DETALLE DE LA COMPRA")
        print(f"{'Producto':<10}{'Cantidad':<8}{'Precio/u':<10}{'Total':<10}")
        total_factura = 0
        for cantidad, producto, precio in mercaderia:
            total = cantidad * precio
            total_factura += total
            print(f"{producto:<10}{cantidad:<8}{precio:<10.2f}{total:<10.2f}")
        print(f"Importe Total")
        print(f"Es un total de {total_factura:.2f} sin IVA.")
        print(f"Es un total de {iva(total_factura) + total_factura:.2f} con IVA.")
        print(f"Total de recargo de IVA {iva(total_factura):.2f}")
        print("#" * 60)

