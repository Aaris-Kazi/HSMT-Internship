from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd

# //*[@id="article_534441"]/div/div[3]/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[1]
# //*[@id="article_534441"]/div/div[3]/div[2]/div/div/div[1]/div/table/tbody/tr[2]/td[1]
# 
PATH = r'Qualifying\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://www.cipla.com/generic-product-list#antacid')
dev = driver.title 
print(dev)
td = ''
# table =driver.find_elements_by_class_name('table.table-hover.table-striped')
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