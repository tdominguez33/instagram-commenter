from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from os.path import exists
import pickle
import time
import schedule
import random
import json
import inicializar
from scripts.cls import cls

inicializar.start()

# Extraemos los datos del JSON
with open('datos.json', 'r') as json_file:
	datos = json.load(json_file)

# Constantes del JSON
LINK = datos["link"]
COMENTARIO = datos["comentario"]
ARROBAS_REUTILIZABLES = datos["arrobasReutilizables"]
ARROBAS = datos["arrobas"]


# SOPORTE DE CHROME NO TESTEADO

FIREFOX = 0
CHROME = 1

def elegirDriver(tipo):
    if tipo == FIREFOX:
        return webdriver.Firefox()
    elif tipo == CHROME:
        return webdriver.Chrome()

# Para que esto funcione hay que pegar el archivo geckodriver.exe en la carpeta donde está instalado el Firefox
driver = elegirDriver(FIREFOX)

numeroCuenta1 = 0
numeroCuenta2 = 1
hayArrobasDisponibles = True

if ARROBAS_REUTILIZABLES <= 2:
    usandoReutilizables = False
else:
    usandoReutilizables = True

def cambiarNumero():
    global ARROBAS_REUTILIZABLES
    global numeroCuenta1
    global numeroCuenta2
    global hayArrobasDisponibles
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

def actualizarContador():
    with open('contador.txt', 'r') as archivoContador:
        contador = int(archivoContador.read()) + 1
    
    cls()
    print(contador, " Comentarios")
    
    with open('contador.txt', 'w') as archivoContador:
        archivoContador.write(str(contador))

def reiniciarContador():
    with open('contador.txt', 'w') as archivoContador:
        archivoContador.write("0")

def escribirComentarioSimple(driver):
    time.sleep(random.randint(0, 10))
    actions = ActionChains(driver)
    actions.send_keys(COMENTARIO)
    actions.perform()
    driver.implicitly_wait(100)
    sendButton = driver.find_element(by = "xpath", value = "//*[text()='Publicar']")
    sendButton.click()
    actualizarContador()

def escribirComentarioArrobas(driver):
    time.sleep(random.randint(0, 10))
    actions = ActionChains(driver)
    actions.send_keys("@" + ARROBAS[numeroCuenta1] + " @" + ARROBAS[numeroCuenta2])
    actions.perform()
    cambiarNumero()
    driver.implicitly_wait(100)
    sendButton = driver.find_element(by = "xpath", value = "//*[text()='Publicar']")
    sendButton.click()
    actualizarContador()

# Obtenemos las cookies para el usuario si no existen
def cargarCookies(driver):
    if not exists("cookies.pkl"):

        print("Se va a abrir una ventana para loguearse a Instagram, una vez que estés en la pantalla principal, presioná enter para continuar...")

        driver.get("https://www.instagram.com")
        input()
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

    else:
        cookies = pickle.load(open("cookies.pkl", "rb"))

        driver.get("https://www.instagram.com")
            
        for cookie in cookies:
            driver.add_cookie(cookie)
            
        driver.get("https://www.instagram.com")


cargarCookies(driver)

driver.implicitly_wait(10)
driver.get(LINK)

driver.implicitly_wait(10)
commentBox = driver.find_element(by = "tag name", value = "textarea")
commentBox.click()

# Definimos que tipo de comentario se hace dependiendo de los datos que hay en el JSON
if COMENTARIO != "":
    escribirComentarioSimple(driver)
    schedule.every(1).minutes.do(escribirComentarioSimple, driver)
else:
    escribirComentarioArrobas(driver)
    schedule.every(1).minutes.do(escribirComentarioArrobas, driver)


while hayArrobasDisponibles:
    schedule.run_pending()
    time.sleep(15)

driver.close()