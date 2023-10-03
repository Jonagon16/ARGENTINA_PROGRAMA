import tkinter as tk
from tkinter import ttk

def abrir_ventana_login(tipo_usuario):
    def validar_login(tipo_usuario, ventana_login):
        if tipo_usuario == "admin" or tipo_usuario == "encargado":
            # Lógica de validación para admin y encargado (usuario y contraseña)
            usuario, contraseña = entry_usuario.get(), entry_contraseña.get()
            # Aquí puedes realizar la validación de usuario y contraseña según tus requisitos
            if usuario == "admin" and contraseña == "admin":
                ventana_login.destroy()  # Cierra la ventana de inicio de sesión
                habilitar_ventana_principal()
            else:
                label_mensaje.config(text="Credenciales incorrectas")
        elif tipo_usuario == "profesor":
            # Lógica de validación para profesor (nombre, materia, clase, división)
            nombre, materia, clase, division = entry_nombre.get(), entry_materia.get(), entry_clase.get(), entry_division.get()
            # Aquí puedes realizar la validación de los datos del profesor según tus requisitos
            if nombre and materia and clase and division:
                ventana_login.destroy()  # Cierra la ventana de inicio de sesión
                habilitar_ventana_principal()
            else:
                label_mensaje.config(text="Completa todos los campos")

    ventana_principal.withdraw()  # Oculta la ventana principal temporalmente

    ventana_login = tk.Toplevel(ventana_principal)
    ventana_login.title("Inicio de Sesión")
    ventana_login.geometry("100x250")

    boton_atras = tk.Button(ventana_login, text="Atrás", command=lambda: cerrar_ventana_login(ventana_login))
    boton_atras.pack()
    boton_atras.configure(height=1,padx=18)

    if tipo_usuario == "admin" or tipo_usuario == "encargado":
        # Formulario de inicio de sesión para admin y encargado (usuario y contraseña)
        label_usuario = tk.Label(ventana_login, text="Usuario:")
        entry_usuario = tk.Entry(ventana_login)
        label_contraseña = tk.Label(ventana_login, text="Contraseña:")
        entry_contraseña = tk.Entry(ventana_login, show="*")  # La contraseña se muestra como asteriscos
        boton_ingresar = tk.Button(ventana_login, text="Ingresar",
                                   command=lambda: validar_login(tipo_usuario, ventana_login))

        label_usuario.pack()
        entry_usuario.pack()
        label_contraseña.pack()
        entry_contraseña.pack()
        boton_ingresar.pack()
        boton_ingresar.configure(height=1, padx=18)
    elif tipo_usuario == "profesor":
        # Formulario de inicio de sesión para profesor (nombre, materia, clase, división)
        label_nombre = tk.Label(ventana_login, text="Nombre:")
        entry_nombre = tk.Entry(ventana_login)
        label_materia = tk.Label(ventana_login, text="Materia:")
        entry_materia = tk.Entry(ventana_login)
        label_clase = tk.Label(ventana_login, text="Clase:")
        entry_clase = tk.Entry(ventana_login)
        label_division = tk.Label(ventana_login, text="División:")
        entry_division = tk.Entry(ventana_login)
        boton_ingresar = tk.Button(ventana_login, text="Ingresar",
                                   command=lambda: validar_login(tipo_usuario, ventana_login))

        label_nombre.pack()
        entry_nombre.pack()
        label_materia.pack()
        entry_materia.pack()
        label_clase.pack()
        entry_clase.pack()
        label_division.pack()
        entry_division.pack()
        boton_ingresar.pack()
        boton_ingresar.configure(height=1,padx=18)


def cerrar_ventana_login(ventana_login):
    ventana_login.destroy()
    habilitar_ventana_principal()

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

def mostrar_alumno():
    selected_alumno = select_alumno.get()
    modo_encargado_label.config(text=f"Modo: Encargado - Encargado: {nombre_encargado} - Alumno: {selected_alumno}")


def abrir_ventana_encargado():
    global ventana_encargado, nombre_encargado, listbox_alumnos, modo_encargado_label

    ventana_principal.withdraw()  # Oculta la ventana principal temporalmente

    ventana_encargado = tk.Toplevel(ventana_principal)
    ventana_encargado.title("Modo: Encargado")
    ventana_encargado.geometry("500x500")

    nombre_encargado = "Ejemplo Encargado"  # Reemplaza con el nombre real del encargado

    modo_encargado_label = tk.Label(ventana_encargado, text=f"Modo: Encargado - Encargado: {nombre_encargado}")
    modo_encargado_label.grid(row=0, column=0, sticky="nw")

    label_select = tk.Label(ventana_encargado, text="Seleccionar Alumno:")
    label_select.grid(row=1, column=0, sticky="w")

    alumnos = ["Jonah", "Diana"]

    listbox_alumnos = tk.Listbox(ventana_encargado, selectmode="single", height=len(alumnos))
    for alumno in alumnos:
        listbox_alumnos.insert(tk.END, alumno)
    listbox_alumnos.grid(row=2, column=2, rowspan=4, sticky="nsw")

    # Función para mostrar el alumno seleccionado en el Listbox
    def mostrar_alumno():
        selected_index = listbox_alumnos.curselection()
        if selected_index:
            selected_alumno = listbox_alumnos.get(selected_index[0])
            modo_encargado_label.config(text=f"Modo: Encargado - Encargado: {nombre_encargado} - Alumno: {selected_alumno}")

    mostrar_button = tk.Button(ventana_encargado, text="Mostrar Alumno", command=mostrar_alumno)
    mostrar_button.grid(row=2, column=1, sticky="nsew")

    agregar_button = tk.Button(ventana_encargado, text="Agregar Nuevo")
    modificar_button = tk.Button(ventana_encargado, text="Modificar")
    eliminar_button = tk.Button(ventana_encargado, text="Eliminar Alumno")
    mostrar_existente_button = tk.Button(ventana_encargado, text="Mostrar Datos")

    # Acomodar los botones uno arriba del otro con un margen
    agregar_button.grid(row=3, column=1, sticky="nsew", pady=10)
    modificar_button.grid(row=4, column=1, sticky="nsew", pady=10)
    eliminar_button.grid(row=5, column=1, sticky="nsew", pady=10)
    mostrar_existente_button.grid(row=6, column=1, sticky="nsew", pady=10)

    volver_button = tk.Button(ventana_encargado, text="Volver Atrás", command=volver_atras)
    volver_button.pack(side="bottom")

def habilitar_ventana_principal():
    ventana_principal.deiconify()  # Muestra la ventana principal
    label_mensaje.config(text="")  # Borra cualquier mensaje de error


# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana de Selección de Usuario")
ventana_principal.geometry("100x180")

# Crear botones para seleccionar el tipo de usuario
boton_profesor = tk.Button(ventana_principal, text="Profesor", command=lambda: abrir_ventana_login("profesor"))
boton_encargado = tk.Button(ventana_principal, text="Encargado", command=abrir_ventana_encargado)
boton_admin = tk.Button(ventana_principal, text="Admin", command=lambda: abrir_ventana_login("admin"))


boton_profesor.pack()
boton_encargado.pack()
boton_admin.pack()
boton_profesor.configure(height=3,padx=18)
boton_encargado.configure(height=3,padx=13)
boton_admin.configure(height=3,padx=23)

# Etiqueta para mostrar mensajes de error
label_mensaje = tk.Label(ventana_principal, text="")
label_mensaje.pack()

# Iniciar la ventana principal
ventana_principal.mainloop()

