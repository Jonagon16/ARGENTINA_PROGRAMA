from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time



CONFIG_FILE = "config.ini"

def iniciar_whatsapp():
    """
    Inicia el sistema SAG.
    Verifica si el archivo de configuración contiene cookies de sesión.
    Si contiene cookies, carga las cookies y abre WhatsApp Web.
    Si el archivo está vacío, escanea el código QR y guarda las cookies en el archivo.
    """
    if os.path.exists(CONFIG_FILE) and os.path.getsize(CONFIG_FILE) > 0:
        # Si el archivo existe y no está vacío, cargar las cookies
        cargar_cookies()
    else:
        pass


def guardar_cookies(driver,cf):
    """
    Guarda las cookies de sesión en el archivo de configuración.
    """
    cookies = driver.get_cookies()

    # Crear un archivo de configuración (INI) y guardar las cookies
    with open(cf, 'w') as config_file:
        for cookie in cookies:
            config_file.write(f"{cookie['name']}={cookie['value']}\n")
def cargar_cookies(driver,cf):
    """
    Carga las cookies de sesión desde el archivo de configuración.
    """
    with open(cf, 'r') as config_file:
        cookies = [line.strip().split('=') for line in config_file.readlines()]
        for cookie in cookies:
            if len(cookie) == 2:
                driver.add_cookie({'name': cookie[0], 'value': cookie[1]})

    # Actualiza la página para cargar las cookies
    print(cookies)
    driver.refresh()


def imprimir_antecedente(dic):
    max_clave = max(len(clave) for clave in dic.keys())
    for i, j in dic.items():
        print(f'{i:{max_clave}}: {j}')

def formatear_diccionario(dic):
    mensaje = ""
    for clave, valor in dic.items():
        if valor is not None and valor.strip() != "":
            mensaje += f"*{clave} :* {valor}\n"

    if mensaje.endswith('\n'):
        mensaje = mensaje[:-1]

    return mensaje
def formatear_mensaje_reducido(diccionario):
    claves_mostradas = ["Dominio", "Motor", "Chasis", "Marca", "Modelo", "Titular", "Denuncia"]
    mensaje = ""
    for clave in claves_mostradas:
        clave = clave.strip()
        valor = diccionario.get(clave, "")  # Obtén el valor de la clave o cadena vacía si no existe
        if valor.strip() != "":
            mensaje += f"*{clave} =* {valor}\n"

    # Elimina el último carácter de nueva línea adicional si es necesario
    if mensaje.endswith('\n'):
        mensaje = mensaje[:-1]

    return mensaje
def obtener_ultimo_mensaje(driver):
    ultimoMensaje = driver.find_elements(by="css selector", value="div.message-in")[-1].text
    antecedente = ultimoMensaje.split("\n")
    if len(antecedente) == 3:
        return antecedente
    elif len(antecedente) == 2:
        return antecedente
    else:
        return ultimoMensaje


def mensaje_en_pantalla(driver):
    try:
        ultimoMensaje = driver.find_elements(by="css selector", value="div.message-in")[-1].text
        return True
    except IndexError:
        return False

def enviar_antecedente(dic,driver):
    mensaje = formatear_mensaje_reducido(dic)
    input_box = driver.find_element(By.XPATH,'//div [@title="Escribe un mensaje"]')
    input_box.send_keys(mensaje)
    input_box.send_keys(Keys.RETURN)
def enviar_mensaje(mensaje,driver):
    input_box = driver.find_element(By.XPATH,'//div [@title="Escribe un mensaje"]')
    input_box.send_keys(mensaje)
    input_box.send_keys(Keys.RETURN)

def recibir_antecedente(ant):
    for linea in ant:
        partes = linea.split(' : ')
        if len(partes) == 2:
            clave, valor = partes
            ant[clave] = valor
        else:
            print(f"Formato incorrecto en la línea: {linea.strip()}")
    return ant


def abrir_contacto(driver):
    webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('2').key_up(Keys.CONTROL).perform()
    time.sleep(5)
    search_box = driver.find_element(by="css selector", value="div[contenteditable='true']")
    search_box.send_keys("INSECTA")
    time.sleep(2)
    contacto = "span[title='INSECTA']"
    driver.find_element(by="css selector", value=contacto).click()
    time.sleep(2)


