import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from whatsapp import *
from Scam_SAG import *

def accion_dominio():
    print("Último antecedente:", mensaje_actual)

    time.sleep(1)
    m1, m2 = pedir_antecedente_dominio(mensaje_actual[0].strip("\n"),driver)
    datosDominio = antecedente_dic(m1, m2)
    resultado = antecedente_dominio_final(datosDominio)
    print(resultado)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    enviar_mensaje(resultado, driver)
    time.sleep(1)
    imprimir_antecedente(datosDominio)
    enviar_antecedente(datosDominio, driver)


def accion_dni1():
    print("Último antecedente:", mensaje_actual)
    driver.get('https://sag.gna/PER_Busqueda.aspx')
    time.sleep(1)
    m1 = pedir_antecedente_dni(mensaje_actual[1].strip("\n"),driver)
    print(m1)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    enviar_mensaje(m1, driver)
    time.sleep(1)

def accion_dni2():
    print("Último antecedente:", mensaje_actual)

    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://sag.gna/PER_Busqueda.aspx')
    time.sleep(1)
    m1 = pedir_antecedente_dni(mensaje_actual[1].strip("\n"), driver)
    print(m1)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    enviar_mensaje(m1, driver)
    time.sleep(1)

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
ultimo_mensaje = ""
x = False
y = False
z = False

# Ruta al archivo de configuración de cookies
CONFIG_FILEW = "Wconfig.ini"
CONFIG_FILES = "Sconfig.ini"
# Función para mostrar el menú
def mostrar_menu():
    print("\nMENU:")
    print("1. Iniciar SAG")
    print("2. LOGS ANTECEDENTES(SOON)")
    print("3. ANTECEDENTES CON NOVEDAD SOON")
    print("4. SALIR")

while not y:
    mostrar_menu()
    opcion=input("")
    if opcion == "1":
        y = True

    elif opcion == "2":
        print("Ver Logs de Antecedentes:")
        log_file = "antecedente_salida.txt"
        if os.path.exists(log_file) and os.path.getsize(log_file) > 0:
            with open(log_file, 'r') as file:
                logs = file.read()
            print(logs)
        else:
            print("No hay registros de antecedentes disponibles.")

    elif opcion == "3":
        print("Ver Logs de Antecedentes:")
        log_file = "antecedente_salida.txt"
        if os.path.exists(log_file) and os.path.getsize(log_file) > 0:
            with open(log_file, 'r') as file:
                logs = file.read()
            print(logs)
        else:
            print("No hay registros de antecedentes disponibles.")

    elif opcion == "4":
        print("Saliendo del programa")
        exit()
    else:
        print("Opción inválida.")
#MAIN
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
print("Iniciando Whatsapp.")
#verifica si el whatsapp tiene cookies o no
if os.path.exists(CONFIG_FILEW) and os.path.getsize(CONFIG_FILEW) > 0:
    cargar_cookies(driver, CONFIG_FILEW)
else:
    input("Por favor escanea el codigo QR")
    guardar_cookies(driver,CONFIG_FILEW)
#inicia sag
driver.execute_script("window.open('', '_blank');")
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
driver.get('https://sag.gna/login.aspx?ReturnUrl=%2fFrame_Principal.aspx%3fidpag%3d92%26fullscreen%3dFalse&idpag=92&fullscreen=False')
input("Aprete Enter una vez este cargado")
loguear_antecedente(driver)
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
abrir_contacto(driver)
while not z:
    if mensaje_en_pantalla(driver):
        mensaje_actual = obtener_ultimo_mensaje(driver)
        if mensaje_actual[0] == "antecedentes":
            z = True
    else:
        time.sleep(5)
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
                enviar_mensaje(mensaje_formato,driver)
                ultimo_mensaje = mensaje_actual

    else:
        time.sleep(3)