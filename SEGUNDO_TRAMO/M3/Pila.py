class pila:
    def __init__(self):
        self.carga = []
    def empty(self):
        if not self.carga:
            return True
        else:
            return False
    def full(self):
        if self.carga:
            return True
        else:
            return False

    def push(self,elemento):
        self.carga.append(elemento)

    def pop(self,elemento=-1):
        self.carga.pop(elemento)

    def top(self):
        return self.carga[-1]

    def __str__(self):
        return str(self.carga)


p = pila()
print(p.empty())

class PilaDeEnteros(pila):
    def __init__(self):
        super().__init__()

    def __add__(self, other):
        if isinstance(other, int):
            self.push(other)
            return self.carga
        else:
            raise TypeError("Solo pueden usarse enteros para la operacion +")

    def __sub__(self,other):
        if other in self.carga:
            other = self.carga.index(other)
            self.carga.pop(other)
            return self.carga
        else:
            raise ValueError ("El entero no se encuentra en la pila")

    def __repr__(self):
        return f"Pila:{self.carga}"

    def __eq__(self, other):
        return bool(self.carga == other.carga)

    def __len__(self):
        return len(self.carga)


p = PilaDeEnteros()
print(p.empty())
p.push(2)
print(p)
p + 3
print(p)
p - 2
print(p)
q = PilaDeEnteros()
q.push(2)
print(q)
q + 3
print (p == q)
print(q.top())

