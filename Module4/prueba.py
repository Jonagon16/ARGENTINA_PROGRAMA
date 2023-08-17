def validar_nota(nota):
    try:
        note = int(nota)
        if 0 <= note <= 10:
            return nota
        else:
            return -1
    except ValueError:
        return -1

print(validar_nota(11))