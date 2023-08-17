def invertir (s):
    s = s[::-1]
    return s

def invertirTodo (l):
    s = []
    for i in l:
      s.append(i[::-1])
    return s

ls = list(input("ingrese una lista de string separados por espacios ").split())
print(ls)
print(invertirTodo(ls))
m = input("")