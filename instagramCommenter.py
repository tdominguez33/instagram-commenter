from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
from os.path import exists
import time
import schedule
import random
import json

if not exists("datos.json"):

    salir = False
    arrobas = []

    repetir = True

    datos = {
        "user": "user",
        "password": "password",
        "link": "link",
        "arrobas": [],
        "arrobasReutilizables": 0
    }

    while repetir == True:
        USER = input("Ingresar Usuario: ")
        rta = input("'" + USER + "' este es tu usuario ingresado, ¿Es correcto? S/N: ")
        if rta == 'S':
            repetir = False

    repetir = True

    while repetir == True:
        PASSWORD = input("Ingresar Contraseña: ")
        rta = input("'" + PASSWORD + "' este es tu contraseña ingresada, ¿Es correcta? S/N: ")
        if rta == 'S':
            repetir = False

    repetir = True

    while repetir == True:
        LINK = input("Ingresar link de la publicación a comentar: ")
        rta = input("'" + LINK + "' este es la página ingresada, ¿Es correcta? S/N: ")
        if rta == 'S':
            repetir = False


    print("Ahora hay que ingresar los usuarios de las cuentas que vamos a etiquetar SIN EL @")
    print("Para salir ingresar 0")
    while salir == False:
        usuario = input("Ingresar Usuario: ")
        if usuario == "0":
            salir = True
        else:
            arrobas.append(usuario)


    for i in arrobas:
        print(i)

    rta = input("Esta es la lista ¿estás seguro? S/N: ")
    if rta == 'N':
        exit()

    datos["user"] = USER
    datos["password"] = PASSWORD
    datos["link"] = LINK
    datos["arrobas"] = arrobas

    datos_json = json.dumps(datos, indent=4)

    with open("datos.json", "w") as archivo:
        archivo.write(datos_json)

# Extraemos los datos del JSON
f = open ('datos.json', "r")
datos = json.loads(f.read())
f.close()

USER = datos["user"]
PASSWORD = datos["password"]
LINK = datos["link"]
ARROBAS_REUTILIZABLES = datos["arrobasReutilizables"]

print(USER)
print(PASSWORD)
print(LINK)

# Función que devuelve la ruta absoluta
script_dir = os.path.dirname(os.path.abspath(__file__))

# Para que esto funcione hay que pegar el archivo geckodriver.exe en la carpeta donde está instalado el Firefox
driver = webdriver.Firefox()

numeroCuenta1 = 0
numeroCuenta2 = 1
hayArrobasDisponibles = True

if ARROBAS_REUTILIZABLES <= 2:
    usandoReutilizables = False
else:
    usandoReutilizables = True

def cambiarNumero():
    global ARROBAS_REUTILIZABLES
    global hayArrobasDisponibles
    global numeroCuenta1
    global numeroCuenta2
    global usandoReutilizables

    if usandoReutilizables:
        numeroCuenta2 += 1
        if numeroCuenta2 == numeroCuenta1:
            numeroCuenta2 += 1
        if numeroCuenta2 == ARROBAS_REUTILIZABLES:
            numeroCuenta2 = 0
            numeroCuenta1 += 1
            if numeroCuenta1 == numeroCuenta2:
                numeroCuenta1 += 1
            if numeroCuenta1 == ARROBAS_REUTILIZABLES:
                print("Vamos a cambiar la variable")
                usandoReutilizables = False
                numeroCuenta1 = ARROBAS_REUTILIZABLES - 1
                numeroCuenta2 = ARROBAS_REUTILIZABLES
    elif numeroCuenta2 != len(arrobas) - 1:
        numeroCuenta1 += 1
        numeroCuenta2 += 1
    else:
        hayArrobasDisponibles = False

def escribirComentario():
    global driver
    time.sleep(random.randint(0, 10))
    actions = ActionChains(driver)
    actions.send_keys("@" + arrobas[numeroCuenta1] + " @" + arrobas[numeroCuenta2])
    actions.perform()
    cambiarNumero()
    driver.implicitly_wait(10)
    sendButton = driver.find_element(by = "xpath", value = "//*[text()='Publicar']")
    sendButton.click()


driver.get("https://www.instagram.com")
driver.implicitly_wait(100)
user = driver.find_element(by = "name", value = 'username')
user.send_keys(USER)

password = driver.find_element(by = "name", value = 'password')
password.send_keys(PASSWORD)

driver.implicitly_wait(10)
loginButton = driver.find_element(by = "xpath", value = "//*[text()='Iniciar sesión']")
loginButton.lick()

driver.implicitly_wait(10)
dismissShit = driver.find_element(by = "xpath", value = "//*[text()='Ahora no']")
dismissShit.click()

driver.implicitly_wait(10)
dismissShit = driver.find_element(by = "xpath", value = "//*[text()='Ahora no']")
dismissShit.click()

driver.implicitly_wait(10)
driver.get(LINK)

driver.implicitly_wait(10)
commentBox = driver.find_element(by = "tag name", value = "textarea")
commentBox.click()
escribirComentario()

schedule.every(1).minutes.do(escribirComentario)

while hayArrobasDisponibles:
    schedule.run_pending()
    time.sleep(15)

driver.close()