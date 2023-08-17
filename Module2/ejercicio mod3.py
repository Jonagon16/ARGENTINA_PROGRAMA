correo = input("Ingrese su correo: ")
usuario = correo.split("@") 
dominio = usuario[1].split(".")
i = dominio[1:]
extencion = ".".join(i)
print (f"Tu usuario es {usuario[0]} \nEl dominio es: {dominio[0].capitalize()}\nLa extencion es: {extencion} ") 

