from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import schedule
import random
import json
import inicializar

inicializar.start()

# Extraemos los datos del JSON
f = open ('datos.json', "r")
datos = json.loads(f.read())
f.close()

USER = datos["user"]
PASSWORD = datos["password"]
LINK = datos["link"]
ARROBAS_REUTILIZABLES = datos["arrobasReutilizables"]
ARROBAS = datos["arrobas"]

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
    elif numeroCuenta2 != len(ARROBAS) - 1:
        numeroCuenta1 += 1
        numeroCuenta2 += 1
    else:
        hayArrobasDisponibles = False

def escribirComentario():
    global driver
    time.sleep(random.randint(0, 10))
    actions = ActionChains(driver)
    actions.send_keys("@" + ARROBAS[numeroCuenta1] + " @" + ARROBAS[numeroCuenta2])
    actions.perform()
    cambiarNumero()
    driver.implicitly_wait(100)
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
loginButton.click()

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