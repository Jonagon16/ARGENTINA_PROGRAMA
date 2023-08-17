a = set(input("Ingrese un conjunto de datos: "))
b = set(input("Ingrese otro conjunto de datos: "))
r = "a es un subconjunto de b" if a.issubset(b) else "b es un sub conjunto de a"
print(f"Entre el Conjunto a: {a} y el Conjunto b: {b} claramente {r}")