from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd

PATH = r'Task1\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.vaidam.com/cost')
dev = driver.title
print(dev)
time.sleep(5)
driver.close()
driver.quit()