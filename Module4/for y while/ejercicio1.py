su = input("ingrese un string: ")
s = list(su.upper().replace(" ",""))
c = 0
for i in s:
    if i in "AEIOU":
        c = c + 1
print(f"La cantidad de consonantes que contiene {su} es {len(s)-c}")
print(f"La cantidad de volcales que contiene {su} es {c}")