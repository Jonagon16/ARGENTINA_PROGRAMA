class Boton:
    def __init__(self,estado):
        estados = ["presionado","libre"]
        if estado.lower() in estados:
            self._estado = estado
        else:
            raise AttributeError("Valor invalido")
    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self,estado):
        estados = ["presionado","libre"]
        if estado.lower() in estados:
            self._estado = estado
        else:
            raise AttributeError("Valor invalido")
    @estado.deleter
    def estado(self):
        del self._estado

    estado.__doc__="El boton solo puede estar 'presionado' o 'libre'"

p = Boton("presionado")
print(p.estado)
p.estado="libre"
print(p.estado)
help(p)