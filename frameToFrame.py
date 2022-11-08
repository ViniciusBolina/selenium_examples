import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver")

driver.get("https://www.cursoemvideo.com/curso/curso-de-algoritmo/")
driver.get("https://www.youtube.com/")
print("oi")
driver.back()
time.sleep(6)
driver.forward()