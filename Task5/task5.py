from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd

PATH = r'Qualifying\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://www.cipla.com/generic-product-list#antacid')
dev = driver.title 
print(dev)
td = ''

table =driver.find_elements_by_tag_name('td')
for i in table:
    if i.text == 'BRAND NAME MOLECULE DOSAGE FORM':
        pass
    else:
        # td1 = i.find_element_by_tag_name('td[1]')
        # print(td1.text)
        # x = td.split(' ')
        print(i.text)
time.sleep(5)
driver.close()
driver.quit()