from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("chromedriver")
driver.get("https://developer.marvel.com/")

abaMove = driver.find_element(By.ID, "mvl-flyout-button-3")
abaMove.click()  
time.sleep(5)
palavra = "Captain"
nameMove = driver.find_elements(By.XPATH, "//section/div/div/div/a/div/p")
time.sleep(5)
numFilmes = 0

for name in nameMove:
    if name.text.startswith(palavra) or name.text.endswith(palavra):
       print(name.text)
       numFilmes = numFilmes + 1

print("tem ", numFilmes," filmes contendo Captain")
