from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

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
            mensaje += f"{clave} : {valor}\n"

    # Elimina el último carácter de nueva línea adicional si es necesario
    if mensaje.endswith('\n'):
        mensaje = mensaje[:-1]

    return mensaje
def obtener_ultimo_mensaje():
    #ultimo mensaje
    ultimoMensaje = driver.find_elements(by="css selector", value="div.message-in")[-1].text
    antecedente = ultimoMensaje.split("\n")
    with open("antecedente_entrada.txt","w") as ant_ent:
        ant_ent.write(antecedente[0])
    return antecedente

def enviar_antecedente(dic):
    mensaje = formatear_mensaje_reducido(dic)
    input_box = driver.find_element(By.XPATH,'//div [@title="Escribe un mensaje"]')
    input_box.send_keys(mensaje)
    input_box.send_keys(Keys.RETURN)

def recibir_antecedente():
    ant={}
    with open("antecedente_salida.txt", 'r') as archivo:
        for linea in archivo:
            partes = linea.split(' : ')
            if len(partes) == 2:
                clave, valor = partes
                ant[clave] = valor
            else:
                print(f"Formato incorrecto en la línea: {linea.strip()}")
    with open("antecedente_salida.txt", "w") as ant_file:
        ant_file.truncate()
    return ant



input("Escanea el código QR y presiona Enter para continuar...")
#abre la lista de contactos
webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('2').key_up(Keys.CONTROL).perform()
time.sleep(5)
#busca el contacto
search_box = driver.find_element(by="css selector", value="div[contenteditable='true']")
search_box.send_keys("INSECTA")
time.sleep(2)
contacto = "span[title='INSECTA']"
driver.find_element(by="css selector", value=contacto).click()
time.sleep(2)
ultimo_mensaje = ""
mensaje_actual = obtener_ultimo_mensaje()
while True:

    if mensaje_actual != ultimo_mensaje:
        mensaje_actual = obtener_ultimo_mensaje()
        print("Último antecedente:", mensaje_actual)
        antecedente = recibir_antecedente()
        print(antecedente)
        enviar_antecedente(antecedente)
        ultimo_mensaje = mensaje_actual
    time.sleep(1)

