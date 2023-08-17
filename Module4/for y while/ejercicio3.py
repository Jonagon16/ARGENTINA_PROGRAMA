s0= input("ingrese un string")
s1= input("ingrese un segundo string")
l=[]
sm=max(len(s0),len(s1))
for i,j in zip(s0.ljust(sm),s1.ljust(sm)):
    l.append(i)
    l.append(j)
r="".join(l)
print(f"s0: {s0}")
print(f"s1: {s1}")
print("Resultado: ",r.replace(" ",""))