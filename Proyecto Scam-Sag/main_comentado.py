import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from whatsapp import *  # Asumiendo que este módulo existe
from Scam_SAG import *  # Asumiendo que este módulo existe

# Variables globales
CONFIG_FILEW = "Wconfig.ini"
CONFIG_FILES = "Sconfig.ini"
ultimo_mensaje = ""
x = False
y = False
z = False


# Función para mostrar el menú
def mostrar_menu():
    print("\nMENU:")
    print("1. Iniciar SAG")
    print("2. LOGS ANTECEDENTES(SOON)")
    print("3. ANTECEDENTES CON NOVEDAD SOON")
    print("4. SALIR")


# Función para realizar acciones en el dominio
def accion_dominio():
    print("Último antecedente:", mensaje_actual)
    time.sleep(1)

    # Obtener información del dominio
    m1, m2 = pedir_antecedente_dominio(mensaje_actual[0].strip("\n"), driver)
    datosDominio = antecedente_dic(m1, m2)
    resultado = antecedente_dominio_final(datosDominio)
    print(resultado)

    # Cambiar al chat de WhatsApp
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    enviar_mensaje(resultado, driver)
    time.sleep(1)
    imprimir_antecedente(datosDominio)
    enviar_antecedente(datosDominio, driver)


# Función para realizar acciones con DNI
def accion_dni1():
    print("Último antecedente:", mensaje_actual)
    driver.get('https://sag.gna/PER_Busqueda.aspx')
    time.sleep(1)
    m1 = pedir_antecedente_dni(mensaje_actual[1].strip("\n"), driver)
    print(m1)

    # Cambiar al chat de WhatsApp
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    enviar_mensaje(m1, driver)
    time.sleep(1)


# Función para realizar acciones con DNI (segunda ventana)
def accion_dni2():
    print("Último antecedente:", mensaje_actual)

    # Cambiar a la segunda ventana del navegador
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://sag.gna/PER_Busqueda.aspx')
    time.sleep(1)
    m1 = pedir_antecedente_dni(mensaje_actual[1].strip("\n"), driver)
    print(m1)

    # Cambiar al chat de WhatsApp
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    enviar_mensaje(m1, driver)
    time.sleep(1)


# Mensaje de formato
mensaje_formato = """"*FORMATOS PERMITIDOS:*
*EJEMPLO 1:*
ABC123
40211345
*EJEMPLO 2:*
ABC123
*EJEMPLO 3:*
40211345
*EJEMPLO 4:*
LS
"""

# MAIN
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
print("Iniciando Whatsapp.")

# Verificar si WhatsApp tiene cookies o no
if os.path.exists(CONFIG_FILEW) and os.path.getsize(CONFIG_FILEW) > 0:
    cargar_cookies(driver, CONFIG_FILEW)
else:
    input("Por favor escanea el código QR")
    guardar_cookies(driver, CONFIG_FILEW)

# Iniciar SAG
driver.execute_script("window.open('', '_blank');")
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
driver.get(
    'https://sag.gna/login.aspx?ReturnUrl=%2fFrame_Principal.aspx%3fidpag%3d92%26fullscreen%3dFalse&idpag=92&fullscreen=False')
input("Apreta Enter una vez este cargado")
loguear_antecedente(driver)
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
abrir_contacto(driver)

# Esperar a que aparezca el mensaje "antecedentes"
while not z:
    if mensaje_en_pantalla(driver):
        mensaje_actual = obtener_ultimo_mensaje(driver)
        if mensaje_actual[0] == "antecedentes":
            z = True
    else:
        time.sleep(5)

# Procesar mensajes
while not x:
    if mensaje_en_pantalla(driver):
        mensaje_actual = obtener_ultimo_mensaje(driver)
        if mensaje_actual != ultimo_mensaje:
            mensaje_actual = obtener_ultimo_mensaje(driver)

            if len(mensaje_actual) == 3:
                accion_dominio()
                accion_dni1()
                ultimo_mensaje = mensaje_actual
            elif len(mensaje_actual) == 2:
                if int(mensaje_actual[1]):
                    accion_dni2()
                    ultimo_mensaje = mensaje_actual
                elif mensaje_actual[0] == "LS":
                    break
                else:
                    accion_dominio()
                    ultimo_mensaje = mensaje_actual
            else:
                print(mensaje_actual)
                enviar_mensaje(mensaje_formato, driver)
                ultimo_mensaje = mensaje_actual

    else:
        time.sleep(3)

# Cerrar el navegador al finalizar
driver.quit()
