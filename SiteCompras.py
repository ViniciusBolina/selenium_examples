"""
1- Abrir Chrome - ok
2- Acessar o site https://www.saucedemo.com/cart.html - ok 
3- Selecionar caixa de texto Username - ok
4- Jogar standard_user na caixa de texto Username - ok
5- Selecionar caixa de texto Password - ok
6- Jogar secret_sauce na caixa de texto Password - ok
7- Selecionar botão Login - ok
8- Aperta botão Login - ok
9- Ser jogado para nova pagina de compras - ok
10- escolher item Sauce Labs Bike Light -ok 
11- verificar se nome produto é igual do escolhido -ok 
12- Selecionar botão add to cart -ok 
13- Click no botão add to cart -ok

"""
from audioop import add
import time
from turtle import clear
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("chromedriver2")#Entra no Chrome
driver.get("https://www.saucedemo.com/cart.html")# Acessa o site SWAGlabs

userName = driver.find_element(By.ID, "user-name")#Seleciona caixa de texto "Username"
userName.send_keys("standard_user")#Preenche caixa de texto "Username"

pWord = driver.find_element(By.NAME, "password")#Seleciona caixa de texto "Password"
pWord.send_keys("secret_sauce")#Preenche caixa de texto "Password"

btnLogin = driver.find_element(By.CLASS_NAME, "btn_action")#Seleciona botão "Login"
btnLogin.click()#Click 

time.sleep(4)#Conta 4 segundos antes de ir para procimo comando
items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")#Guarda uma lista dos elementos da classe

for e in items:# faz um loop com os elementos da variavel items e um por vez fica na variavel "e"
    if e.text == "Sauce Labs Bolt T-Shirt":# Se o texto da varivel "e" for igual a "Sauce Labs Bolt T-Shirt"
        e.click()#Execulção da variavel "e" com click
        break #Para o loop do "for"

time.sleep(5)
btnAddCart = driver.find_element(By.CLASS_NAME, "btn_inventory")
btnAddCart.click()

time.sleep(5)
btnCar = driver.find_element(By.ID, "shopping_cart_container")
btnCar.click()

nameProduct = driver.find_element(By.CLASS_NAME, "inventory_item_name")

if nameProduct.text == "Sauce Labs Bolt T-Shirt":
    btnCheckout = driver.find_element(By.NAME, "checkout")
    btnCheckout.click()

else:
    btnRemove = driver.find_element(By.ID, "remove-sauce-labs-bolt-t-shirt")
    btnRemove.click()

firstName = driver.find_element(By.ID, "first-name")
lastName = driver.find_element(By.ID, "last-name")
postalCode = driver.find_element(By.ID, "postal-code")

firstName.send_keys("Vinicius")
lastName.send_keys("Bolina")
postalCode.send_keys("19432-504")

btnContinue = driver.find_element(By.ID, "continue")
btnContinue.click()

btnFinish = driver.find_element(By.ID, "finish")
btnFinish.click()