num = int(input("ingrese un numero: "))
li = input("ingrese varios elementos separados por una ',' : ")
lis = li.split(",")
print(lis)
if num < len(lis):
    print (lis[num])
else:
    print(lis[-1])