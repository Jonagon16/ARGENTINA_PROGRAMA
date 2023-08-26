from Animal import *
class tEspecie(Exception):
    def __init__(self, mensaje= "ingrese una especie valida: aves, mamiferos, anfibios, reptiles, peces"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
class vertebrado(animal):
    def __init__(self,especie):
        super().__init__("vertebrados")
        self.especie = especie

    def setEspecie (self,especie):
        especies = ("aves","mamiferos","anfibios","reptiles","peces")
        especie.lower().strip(" ")
        if especie in especies:
            self.especie = especie
        else:
            raise tEspecie

    def getEspecie (self):
        return self.especie

ave = vertebrado("aves")
ave.setEspecie("aves")
print(ave.getEspecie())
print(ave.getGrupo())
