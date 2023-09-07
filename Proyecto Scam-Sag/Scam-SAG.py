from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def ver_antecedente(f):
    with open(f,"r") as ant_file:
        antecedente = ant_file.readline()
    with open(f,"w") as ant_file:
        ant_file.truncate()
    return antecedente

def antecedente_dic(a,b):
    c = {}
    for i in range(len(a)):
        if a[i] not in c:
            c[a[i]] = b[i]
    return c

def imprimir_antecedente(dic):
    max_clave = max(len(clave) for clave in dic.keys())
    for i, j in dic.items():
        print(f'{i:{max_clave}}: {j}')

def guardar_antecedente(dic):
    max_clave = max(len(clave) for clave in dic.keys())
    with open("antecedente_salida.txt","w") as ant_salida:
        for i, j in dic.items():
            ant_salida.write(f'{i:{max_clave}}: {j}\n')

def pedir_antecedente(lista):
    dominio= lista.lower()
    print(f"Resultado del dominio {dominio}")
    antecedente = driver.find_element(by="id", value='txtDominio')
    antecedente.clear()
    antecedente.send_keys(dominio)
    antecedente.send_keys(Keys.RETURN)
    time.sleep(3)
    antecedentes1 =[]
    antecedentes2 = []
    item = driver.find_elements(by='class name', value='GrillaItem')
    resultado = driver.find_elements(by='class name', value='GrillaAlternado')
    for i in item:
        antecedentes1.append(i.text)
    for j in resultado:
        antecedentes2.append(j.text)
    return antecedentes1,antecedentes2


driver = webdriver.Chrome()
driver.get('https://sag.gna/login.aspx?ReturnUrl=%2fFrame_Principal.aspx%3fidpag%3d92%26fullscreen%3dFalse&idpag=92&fullscreen=False')
input("cuando este cargado apreta una tecla")
#Encuentra los campos de usuario y contraseña e ingrésalos
usuario = driver.find_element(by="id", value='txtUsuario')
usuario.send_keys('40211345')
contrasena = driver.find_element(by="id", value='txtPassword')
contrasena.send_keys('Agosto.4021')
contrasena.send_keys(Keys.RETURN)
time.sleep(3)
driver.get("https://sag.gna/VEH_ConsultaDNRPA.aspx")
time.sleep(3)
x = False
json_dominio2= ""
while not x:
    json_dominio=input("antecedente: ")
        #ver_antecedente("antecedente_entrada.txt"))
    if json_dominio == "ls":
        x = True
    elif json_dominio != json_dominio2:
        if json_dominio == "":
            time.sleep(5)
            continue
        else:
            m1,m2 = pedir_antecedente(json_dominio)
            time.sleep(2)
            md = antecedente_dic(m1,m2)
            imprimir_antecedente(md)
            guardar_antecedente(md)
            json_dominio2 = json_dominio

    time.sleep(1)
