from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def ver_antecedente(f):
    """
    Lee y muestra el último antecedente guardado en un archivo.
    Luego, borra el contenido del archivo.

    Args:
        f (str): Ruta al archivo de antecedentes.

    Returns:
        str: El último antecedente leído del archivo.
    """
    with open(f, "r") as ant_file:
        antecedente = ant_file.readline()
    with open(f, "w") as ant_file:
        ant_file.truncate()
    return antecedente


def antecedente_dic(a, b):
    """
    Combina dos listas en un diccionario.

    Args:
        a (list): Lista de claves.
        b (list): Lista de valores.

    Returns:
        dict: Diccionario con las claves de la lista "a" y los valores de la lista "b".
    """
    c = {}
    for i in range(len(a)):
        if a[i] not in c:
            c[a[i]] = b[i]
    return c

def antecedente_dominio_final(dic):
    """
    Procesa un diccionario de antecedentes y lo guarda en un archivo.

    Args:
        dic (dict): Diccionario de antecedentes a procesar y guardar.
    """

    dic_procesado = {}

    # Filtrar claves con valores no vacíos
    for clave, valor in dic.items():
        if valor.strip() != "":
            dic_procesado[clave] = valor

    # Verificar si el diccionario procesado tiene al menos una clave con valor
    if dic_procesado:
        imprimir_antecedente(dic_procesado)
        guardar_antecedente_dominio(dic_procesado)
        return "Dominio Valido"
    else:
        return "El Dominio es invalido"
def imprimir_antecedente(dic):
    """
    Imprime un diccionario formateado.

    Args:
        dic (dict): Diccionario de antecedentes a imprimir.
    """
    max_clave = max(len(clave) for clave in dic.keys())
    for i, j in dic.items():
        print(f'{i:{max_clave}}: {j}')


def guardar_antecedente_dominio(dic):
    """
    Guarda un diccionario de antecedentes en un archivo.

    Args:
        dic (dict): Diccionario de antecedentes a guardar.
    """
    max_clave = max(len(clave) for clave in dic.keys())
    with open("antecedente_salida.txt", "w") as ant_salida:
        for i, j in dic.items():
            ant_salida.write(f'{i:{max_clave}}: {j}\n')

def no_dni(driver):
    try:
        mensaje = driver.find_element(by="id",value="lblmensaje").text
        if mensaje == "La busqueda no tuvo coincidencias en SAG. ":
            return "sin novedad"
        elif mensaje == "Se muestran los primeros registros resultantes de la busqueda. Si no encuentra el registro en el resultado, por favor modifique el patron de su busqueda.":
            return True
    except IndexError:
        return False

def no_antecedente(driver):
     try:
        mensaje = driver.find_element (By.XPATH,'//*[@id="DatosPersona"]/tbody/tr[2]/td[1]/a')
        return True
     except IndexError:
        return False


def novedad_dni(driver):
    try:
        mensaje = driver.find_element(By.XPATH, '//*[@id="GrAntecedentes"]/tbody/tr[2]/td[1]/a')
        novedad = driver.find_element(By.XPATH,'//*[@id="GrAntecedentes"]/tbody/tr[2]/td[4]').text
        return f"CON NOVEDAD COMUNICARSE CON EL OPERADOR CONSULTAR {novedad}"
    except IndexError:
        return "SIN NOVEDAD"


def pedir_antecedente_dni(Dstr,driver):
    """
    Realiza una búsqueda de antecedentes en el sistema SAG.

    Args:
        lista (str): Dominio a buscar.

    Returns:
        tuple: Dos listas de antecedentes encontrados.
    """
    dni = Dstr.lower()
    print(f"Resultado del dni {dni}")

    # Encuentra el campo de búsqueda de dominio y realiza la búsqueda
    antecedente = driver.find_element(by="id", value='Nro_Documento')
    antecedente.clear()
    antecedente.send_keys(dni)
    antecedente.send_keys(Keys.RETURN)
    time.sleep(3)
    if no_dni(driver) == "sin novedad":
        antecedentes1 = ["DNI SIN NOVEDAD"]
        return antecedentes1
#Recolecta los antecedentes encontrados
    elif no_dni(driver):
        if no_antecedente(driver):
            link_dni = driver.find_element (By.XPATH,'//*[@id="DatosPersona"]/tbody/tr[2]/td[1]/a').click()
        time.sleep(3)
        antecedentes1 = []
        nro_documento = driver.find_elements(by='id', value='NRO_DOCUMENTO_1').text
        apellido = driver.find_elements(by='id', value='APELLIDO_1').text
        nombre = driver.find_elements(by='id', value='NOMBRE_1').text
        sin_novedad = novedad_dni(driver)
        antecedentes1.append(nro_documento)
        antecedentes1.append(apellido)
        antecedentes1.append(nombre)
        antecedentes1.append(sin_novedad)
        return antecedentes1


def pedir_antecedente_dominio(Dstr,driver):
    """
    Realiza una búsqueda de antecedentes en el sistema SAG.

    Args:
        lista (str): Dominio a buscar.

    Returns:
        tuple: Dos listas de antecedentes encontrados.
    """
    dominio = Dstr.lower()
    print(f"Resultado del dominio {dominio}")

    # Encuentra el campo de búsqueda de dominio y realiza la búsqueda
    antecedente = driver.find_element(by="id", value='txtDominio')
    antecedente.clear()
    antecedente.send_keys(dominio)
    antecedente.send_keys(Keys.RETURN)
    time.sleep(3)

    # Recolecta los antecedentes encontrados
    antecedentes1 = []
    antecedentes2 = []
    item = driver.find_elements(by='class name', value='GrillaItem')
    resultado = driver.find_elements(by='class name', value='GrillaAlternado')
    for i in item:
        antecedentes1.append(i.text)
    for j in resultado:
        antecedentes2.append(j.text)

    return antecedentes1, antecedentes2




def loguear_antecedente(driver):
    """
    Inicia sesión en el sistema SAG.
    """
    input("Cuando esté cargado, presiona una tecla para continuar...")

    # Encuentra los campos de usuario y contraseña e ingrésalos
    usuario = driver.find_element(by="id", value='txtUsuario')
    usuario.send_keys('40211345')
    contrasena = driver.find_element(by="id", value='txtPassword')
    contrasena.send_keys('Agosto.4021')
    contrasena.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.get("https://sag.gna/VEH_ConsultaDNRPA.aspx")

