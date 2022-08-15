from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


drive = webdriver.Chrome("chromedriver2")

drive.get("http://www.python.org")

time.sleep(2)
elemento = drive.find_element(By.ID, "id-search-field")

elemento.send_keys("python")
print(elemento.tag_name)

botao = drive.find_element(By.ID, "submit")
botao.click()

elementos = drive.find_elements(By.TAG_NAME, "a")

for e in elementos:
    print(e.text)

    e.text = "Vinicius"






time.sleep(100)
drive.close()