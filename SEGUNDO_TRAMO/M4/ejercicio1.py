import math
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



