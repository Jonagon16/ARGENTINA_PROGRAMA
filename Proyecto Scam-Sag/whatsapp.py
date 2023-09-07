from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

def imprimir_antecedente(dic):
    max_clave = max(len(clave) for clave in dic.keys())
    for i, j in dic.items():
        print(f'{i:{max_clave}}: {j}')
def obtener_ultimo_mensaje():
    #ultimo mensaje
    ultimoMensaje = driver.find_elements(by="css selector", value="div.message-in")[-1].text
    antecedente = ultimoMensaje.split("\n")
    with open("antecedente_entrada.txt","w") as ant_ent:
        ant_ent.write(antecedente[0])
    return antecedente

def enviar_antecedente(dic):
    input_box = driver.find_element(by="css selector", value="div[data-tab='1'] [contenteditable='true']")
    input_box.send_keys(imprimir_antecedente(dic))
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
while True:
    mensaje_actual = obtener_ultimo_mensaje()
    if mensaje_actual != ultimo_mensaje:
        print("Último antecedente:", mensaje_actual)
        antecedente = recibir_antecedente()
        enviar_antecedente(antecedente)
        ultimo_mensaje = mensaje_actual
    time.sleep(1)

