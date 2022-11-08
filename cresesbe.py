from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome("chromedriver")
driver.get("https://www.google.com/maps/@-23.5093291,-47.4568369,352m/data=!3m1!1e3")

caixaTexto = driver.find_element(By.ID, "searchboxinput")
caixaTexto.send_keys("Goiania")
time.sleep(4)
lupaPesquisa = driver.find_element(By.CLASS_NAME, "mL3xi")
lupaPesquisa.click()
time.sleep(7)

movimentoMouse = driver.find_element(By.CLASS_NAME, "EIbCs")
acao = ActionChains(driver)
acao.move_to_element(movimentoMouse)
acao.context_click()
print("oiiiiiiiiiiiiiiiiiiiiiii")

#cordenadas = driver.find_element(By.CLASS_NAME, "mLuXec")

#print(cordenadas.text)