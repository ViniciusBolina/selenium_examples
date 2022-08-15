from selenium import webdriver

import time
driver = webdriver.Chrome("chromedriver2")

driver.get("http://www.linhadecodigo.com.br/artigo/1187/guia-pratico-de-html-parte-4.aspx")
time.sleep(10)
driver.maximize_window()
time.sleep(5)
driver.minimize_window()