class pezEquivocado(Exception):
    def __init__(self, mensaje="Ingrese tipo de agua: agua dulce, agua salada"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
class pez:

    def __init__(self,agua):
        self.agua = agua

    def setAgua (self,agua):
            tAguas = ("agua dulce", "agua salada")
            agua.lower()
            if agua in tAguas:
                self.agua = agua
            else:
                raise pezEquivocado
    def getAgua (self):
        return self.agua

