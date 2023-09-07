from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

elemento = driver.find_element_by_id("id_del_elemento")