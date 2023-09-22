def butlast(n,lista):
    """
    Ejercicio 1
    :param n: Int
    :param lista: List
    :return: Lista sin los n ultimos nros
    """
    if n > len(lista):
        raise ValueError ("El numero ingresado exede el largo de la lista")
    else:
        return lista[:-n]

def remove_if(p,l):
    """
    Ejercio 2
    :param p: Predicado
    :param l: List
    :return: Retorna los enteros que no devulvan True de la funcion p

    Ejemplo
    m = remove_if(mul_5, li) // mul_5 devuelve los multiplos de 5
    """
    s=[]
    for i in l:
        if not p(i):
            s.append(i)
    return s

def mul_5(n):
    """
    :param n: Int
    :return: True si es multiplo de 5
    """
    return (n % 5) == 0

#Funciones Lambda
#Ejercicio 3
mayor = lambda x,y: y if x < y else (x if x == y else x)# mayor(5,6), Retorna 6
#Ejercicio 4
doble_n = lambda n: n * 2 # doble_n(5), Retorna 10
es_impar = lambda n: True if not (n % 2) == 0 else False # es_impar(5), Retorna True
mayor_long = lambda s1,s2: s2 if len(s1) < len(s2) else (s1 if len(s1) == len(s2) else s1) # mayor_long("hola","hi") Retorna hi
dupla = lambda d: (d[0]*2, d[1]*3) #dupla(3,6) Retorna (6,18)
mayor_que_cero = lambda n: True if n > 0 else False # mayor_que_cero(1) Return True
dentro_rango = lambda n,rmin,rmax: True if n in range(rmin,rmax) else False #dentro_rango(2,1,6) Retorna True
punto_dentro = lambda p, c, r: ((p[0] - c[0])**2 + (p[1] - c[1])**2) < r**2 #punto_dentro((0,1),(0,0),4) Retorna True
area_triangulo = lambda b,a: (b*a)/2 #area_triangulo(3,5) Retorna 7.5
area_cuadrado = lambda l: l*l#area_cuadrado(4) Retorna 16
ordenar = lambda  l,sentido="False": sorted(l, reverse=sentido)#ordenar([1,6,8,0,4,2],True) Retorna [8, 6, 4, 2, 1, 0]
#Ejercicio 5
mayusculas = lambda s: s.upper()
def may_usculas(s):
    """
    Ejercicio 5
    :param s: String
    :return: String.upper()
    """
    return mayusculas(s)

def generar_area(f,b,a):
    """
    Ejercicio 6
    :param f: True:Area de Tiangulo // False:Area de Rectangulo
    :param b: base o ancho
    :param a: altura
    :return: Area de triangulo o Rectangulo
    """
    if f:
        return f"Area del Triangulo {area_triangulo(b,a)}"
    else:
        return f"Area del Rectangulo {b*a}"

class ContadorModulo:
    """
Ejemplo de uso:
c = ContadorModulo(3)
i = iter(c)
print(next(i))  #imprimirá 0
print(next(i))  #imprimirá 1
print(next(i))  #imprimirá 2
print(next(i))  #imprimirá 0
    """
    def __init__(self, m):
        self.modulo = m
        self.valor = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.valor < self.modulo:
            r = self.valor
            self.valor += 1
            return r
        else:
            self.valor = 0
            return 0



li=[1,2,3,4,5,6,7,8,9,10]
print(f"Lista original {li}")
m = remove_if(mul_5, li)
n = butlast(3,li)
print(f"Ejemplo de butlast {n}")
print(f"Ejemplo de remove_if {m}")
