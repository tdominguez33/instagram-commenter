from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from os.path import exists
import pickle
import time
import schedule
import random
import json
import inicializar

inicializar.start()

# Extraemos los datos del JSON
with open('datos.json', 'r') as json_file:
	datos = json.load(json_file)

# Constantes del JSON
USER = datos["user"]
PASSWORD = datos["password"]
LINK = datos["link"]
COMENTARIO = datos["comentario"]
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
    
    print(contador, " comentarios")
    
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
def cargarCookies(driver, user, password):
    if not exists("cookies.pkl"):
        
        driver.get("https://www.instagram.com")

        driver.implicitly_wait(100)
        user = driver.find_element(by = "name", value = 'username')
        user.send_keys(user)

        driver.implicitly_wait(10)
        password = driver.find_element(by = "name", value = 'password')
        password.send_keys(password)

        driver.implicitly_wait(10)
        loginButton = driver.find_element(by = "xpath", value = "//*[text()='Iniciar sesión']")
        loginButton.click()

        driver.implicitly_wait(10)
        dismissShit = driver.find_element(by = "xpath", value = "//*[text()='Ahora no']")
        dismissShit.click()

        driver.implicitly_wait(10)
        dismissShit = driver.find_element(by = "xpath", value = "//*[text()='Ahora no']")
        dismissShit.click()

        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

    else:
        driver.get("https://www.instagram.com")

        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)


cargarCookies(driver, USER, PASSWORD)

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