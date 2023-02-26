from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

FIREFOX = 0
CHROME = 1

def elegirDriver(tipo):
    if tipo == FIREFOX:
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif tipo == CHROME:
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
