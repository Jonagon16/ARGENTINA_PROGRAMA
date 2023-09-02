class Persona:
    def __init__(self,nombre):
        self._nombre = nombre
    @property
    def nombre(self):
        """Nombre de la persona"""
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @nombre.deleter
    def nombre(self):
        del self._nombre

p = Persona("jona")
print(p.nombre)
p.nombre="diana"
print(p.nombre)
