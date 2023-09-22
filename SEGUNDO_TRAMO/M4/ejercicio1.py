
def factorial(num):
    """
    Ejercicio 1
    """
    if num == 0:
        return 1
    return num * factorial(num - 1)
print(factorial(5))

def fibonacci(n):
    """
    Ejercicio 2
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))

def mcd(n1,n2):
    """
    Ejercicio 3
    """
    if n2 == 0:
        return n1
    else:
        return mcd(n2,n1 % n2)

print(mcd(10,2))

def esPotencia(n,b):
    """
    Ejercicio 4
    """
    if n == 1:
        return True
    if n % b != 0 or n < b:
        return False
    return esPotencia(n // b, b)

print(esPotencia(8,2))
print(esPotencia(70,10))
print(esPotencia(64,4))


class arbol_ternario:
    def __init__(self,id):
        self.id = id
        self.hojaizq = ""
        self.hojacent = ""
        self.hojader = ""

    def arbol_dic(self):
        arbol_dict = {'id': self.id}
        if self.hojaizq:
            arbol_dict['izquierda'] = self.hojaizq.arbol_dic()
        if self.hojacent:
            arbol_dict['centro'] = self.hojacent.arbol_dic()
        if self.hojader:
            arbol_dict['derecha'] = self.hojader.arbol_dic()
        return arbol_dict

#made in copy adaptado(soy sincero) no lo entendi
def recorrido_simetrico(arbol):
    if arbol:
        recorrido_simetrico(arbol.hojaizq)
        print(f"{arbol.id} \n", end=' ')
        recorrido_simetrico(arbol.hojacent)
        recorrido_simetrico(arbol.hojader)

def recorrido_postorden(arbol):
    if arbol:
        recorrido_postorden(arbol.hojaizq)
        recorrido_postorden(arbol.hojacent)
        recorrido_postorden(arbol.hojader)
        print(arbol.id, end=' ')

def recorrido_preorden(arbol):
    if arbol:
        print(arbol.id, end=' ')
        recorrido_preorden(arbol.hojaizq)
        recorrido_preorden(arbol.hojacent)
        recorrido_preorden(arbol.hojader)

#fin copy

arbol = arbol_ternario(0)
arbol.hojader = arbol_ternario(1)
arbol.hojader.hojaizq = arbol_ternario(2)
arbol.hojader.hojader = arbol_ternario(3)
arbol.hojader.hojacent = arbol_ternario(4)
arbol.hojader.hojacent.hojader = arbol_ternario(5)
print(arbol.arbol_dic())
recorrido_preorden(arbol)






