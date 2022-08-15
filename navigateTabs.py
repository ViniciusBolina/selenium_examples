from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver2")
driver.get("https://www.cursoemvideo.com/curso/curso-de-algoritmo/")
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://selenium-python.readthedocs.io/navigating.html")
driver.switch_to.window(driver.window_handles[0])