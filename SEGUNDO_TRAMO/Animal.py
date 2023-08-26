class tAnimal(Exception):
    def __init__(self, mensaje="Ingrese un grupo valido: vertebrado, invertebrado, anelidos\n moluscos, poriferos, cdinarios, metodos, platelmintos"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
class animal:

    def __init__(self,grupo):
        self.grupo = grupo

    def setGrupo (self,grupo):
            grupos = ("vertebrado", "invertebrado", "anelidos", "moluscos",
                      "poriferos", "cnidarios", "nematodos", "platelmintos")
            grupo.lower().strip(" ")
            if grupo in grupos:
                self.grupo = grupo
            else:
                raise tAnimal
    def getGrupo (self):
        return self.grupo


