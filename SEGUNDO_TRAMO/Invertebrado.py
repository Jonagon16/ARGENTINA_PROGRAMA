from Animal import *
class tEspecie(Exception):
    def __init__(self, mensaje = "ingrese una especie y subespecie valida como: artropodos (insectos, aracnidos, miriapodos,crustaceos), anelidos (lombrices, sanguijuelas), moluscos (bivalvos, gasteropodos, cefalopodos), poriferos (esponjas), cnidarios (medusas, polipos, corales), equinodermos (estrellas de mar), nematodos (gusanos cilíndricos), platelmintos (gusanos planos)"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
class invertebrado(animal):
    def __init__(self,especie,subEspecie):
        self.especies = {'artropodos': {'insectos', 'aracnidos', 'miriapodos', 'crustaceos'},
                    'anelidos': {'lombrises', 'sanguijuelas'},
                    'moluscos': {'bivalvos', 'gasteropodos', 'cefalopodos'},
                    'poriferos': {'esponjas'},
                    'cnidarios': {'medusas', 'polipos', 'corales'},
                    'equinodermo': {'estrella de mar'},
                    'nematodos': {'gusanos cilindricos'},
                    'platelmintos': {'gusanos planos'}}
        if especie in self.especies.keys():
            if subEspecie in self.especies[especie]:
                super().__init__("invertebrados")
                self.especie = especie
                self.subEspecie = subEspecie
            else:
                raise tEspecie
        else:
            raise tEspecie

    def setEspecie (self,especie,subEspecie):
        especie.lower().strip(" ")
        if especie in self.especies:
            self.especie = especie
            self.subEspecie = subEspecie
        else:
            raise tEspecie

    def getEspecie (self):
        return self.especie
    def getSubEspecie(self):
        return self.subEspecie
ave = invertebrado("poriferos","esponjas")
print(ave.getEspecie())
print(ave.getSubEspecie())
print(ave.getGrupo())
ave.setEspecie("anelidos","lombrises")
print(ave.getEspecie())
print(ave.getSubEspecie())
print(ave.getGrupo())