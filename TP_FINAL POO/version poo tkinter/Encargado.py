import Alumno as al
class Encargado:
    __id = 0
    def __init__(self,nombre,dni):
        self.__nombre = nombre
        self.__dni = dni
        Encargado.__id += 1
        self.__id = Encargado.__id
        self.__alumnosInscriptos = []

    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self,n):
        n = limpiarDni(n)
        if isinstance(n,int):
            self.__dni = n
        else:
            raise ValueError ("El documento solo puede ser numerico")

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def alumnosInscriptos(self):
        return self.__alumnosInscriptos
    @alumnosInscriptos.setter
    def alumnosInscriptos(self,alumno):
        self.__alumnosInscriptos.append(alumno)

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        raise AttributeError ("Este valor es de solo lectura no puede modificarse")

    def inscribirAlumno(self,fecha=None, alumno=None, materia=None, profesor=None, curso=None, division=None, dic=None):
        a = al.Alumno(fecha, alumno, materia, profesor, curso, division, nota=-1)
        dic[a.id] = a
        self.__alumnosInscriptos.append(a)


def limpiarDni(s):
    s = s.replace(".","")
    return s

def crear (nombre,dni,dic):
    retorno = False
    for i in dic.values():
        if not int(i.dni) == int(dni):
            encargado = Encargado(nombre,dni)
            dic[encargado.id] = encargado
            retorno = True
    return retorno

def crearEncargados(archivo):
    fl = {}
    with open (archivo,'r') as arch:
        for i in arch:
            nombre, dni = i.strip().split(',')
            encargado = Encargado(nombre,dni)
            fl[encargado.id] = encargado
    return fl


def guardarEncargado(archivo,dict):
    f=open(archivo,"w")
    for i,j in dict.items():
        f.write(f"{j.nombre},{j.dni}\n")
    f.close()

def modificarEncargado (nombre,dni,dic):
    retorno = False
    for i in dic.values():
        if int(i.dni) == int(dni):
            dic[i.nombre] = nombre
            dic[i.dni] = dni
            retorno = True
    return retorno

def validarEncargado (nombre,dni,dic):
    r = False
    for i,j in dic.items():
        if nombre in j.nombre and dni == j.dni:
            r = True
    return r

def eliminarEncargado(dni,dic):
    retorno = False
    for i in dic.values():
        if int(i.dni) == int(dni):
            del dic[i]
            retorno = True
    return retorno

#tkinter

def volver_atras():
    ventana_encargado.destroy()
    habilitar_ventana_principal()

def agregar_alumno():
    # Lógica para agregar un nuevo alumno
    pass

def modificar_alumno():
    # Lógica para modificar un alumno existente
    pass

def mostrar_existente():
    # Lógica para mostrar los detalles de un alumno existente
    pass

def eliminar_alumno():
    # Lógica para eliminar un alumno
    pass


def abrir_ventana_encargado():
    global ventana_encargado, nombre_encargado, select_alumno, modo_encargado_label

    ventana_principal.withdraw()  # Oculta la ventana principal temporalmente

    ventana_encargado = tk.Toplevel(ventana_principal)
    ventana_encargado.title("Modo: Encargado")
    ventana_encargado.geometry("500x500")

    nombre_encargado = "Ejemplo Encargado"  # Reemplaza con el nombre real del encargado

    modo_encargado_label = tk.Label(ventana_encargado, text=f"Modo: Encargado - Encargado: {nombre_encargado}")
    modo_encargado_label.pack(side="top", anchor="ne")

    label_select = tk.Label(ventana_encargado, text="Seleccionar Alumno:")
    label_select.pack(anchor="w")

    alumnos = ["Jonah", "Diana"]
    select_alumno = ttk.Combobox(ventana_encargado, values=alumnos, state="readonly")
    select_alumno.pack()

    mostrar_button = tk.Button(ventana_encargado, text="Mostrar Alumno", command=mostrar_alumno)
    mostrar_button.pack()

    agregar_button = tk.Button(ventana_encargado, text="Agregar Nuevo", command=agregar_alumno)
    modificar_button = tk.Button(ventana_encargado, text="Modificar", command=modificar_alumno)
    existente_button = tk.Button(ventana_encargado, text="Existente", command=mostrar_existente)
    eliminar_button = tk.Button(ventana_encargado, text="Eliminar Alumno", command=eliminar_alumno)

    agregar_button.pack(side="right")
    modificar_button.pack(side="right")
    existente_button.pack(side="right")
    eliminar_button.pack(side="right")

    volver_button = tk.Button(ventana_encargado, text="Volver Atrás", command=volver_atras)
    volver_button.pack(side="bottom")

# Crear botón para abrir la ventana de encargado
boton_encargado = tk.Button(ventana_principal, text="Encargado", command=abrir_ventana_encargado, pady=20)
boton_encargado.pack()

# Iniciar la ventana principal
ventana_principal.mainloop()

