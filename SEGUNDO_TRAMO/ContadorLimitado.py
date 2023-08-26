class vMaximo(Exception):
    def __init__(self, mensaje="Ingrese un nro mayor a 0 y menor que 200"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
class contadorLimitado:
    def __init__(self,vInicial=0):
        self.valor = vInicial
    def setValor(self,valor):
        vMax = 200
        valor = int(valor)
        if valor < vMax and valor > -1:
            self.valor = valor
        else:
            raise vMaximo
    def getValor(self):
        return self.valor

    def incrementar(self):
        self.valor += 1

    def __repr__(self):
        return f"Valor({self.valor})"


cont = contadorLimitado(56)
print(cont.getValor())
cont.setValor(59)
print(cont.getValor())
cont.incrementar()
print(eval(repr(cont.valor)))

