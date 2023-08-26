class cantInsuficiente(Exception):
    def __init__(self, mensaje= "El valor ingresado no puede ser 0"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
class renglonDeFactura:

    def __init__(self,cantUnidades=0,desMercaderia=0,preUnitario=0):
        if cantUnidades > 0 and preUnitario >0:
            self.cantUnidades = cantUnidades
            self.desMercaderia = desMercaderia
            self.preUnitario = preUnitario
            self.preFinal = int(cantUnidades) * int(preUnitario)
        else:
            raise cantInsuficiente

    def setCantUnidades(self,cantUnidades):
        self.cantUnidades = cantUnidades

    def setDesMercaderia(self,desMercaderia):
        self.desMercaderia = desMercaderia

    def setPreUnitario(self,preUnitario):
        self.preUnitario = preUnitario

    def getCantUnidades(self):
        return self.cantUnidades

    def getDesMercaderia(self):
        return self.desMercaderia

    def getPreUnitario(self):
        return self.preUnitario

    def getPreFinal(self):
        return self.preFinal