
class cantIns(Exception):
    def __init__(self, mensaje= "El valor ingresado no puede ser 0"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
class factura:

    def __init__(self,nroFactura=0,empresa="",mercaderia="",merComprada=0):
        if nroFactura > 0 and merComprada > o:
            self.nroFactura = nroFactura
            self.empresa = empresa
            self.mercaderia = mercaderia
            self.merComprada = merComprada
        else:
            raise cantIns

    def setNroFactura(self,nroFactura):
        self.nroFactura = nroFactura

    def setEmpresa(self,empresa):
        self.empresa = empresa

    def setMercaderia(self,mercaderia):
        self.mercaderia = mercaderia

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


