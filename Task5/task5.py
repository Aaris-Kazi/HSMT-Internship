from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd
import numpy as np

td = []
manufature = []
consume_type = []
med_names = []
brand_name = []
price = []
presc = []
units = []
PATH = r'Qualifying\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://www.cipla.com/generic-product-list#antacid')
dev = driver.title 
print(dev)

# j = 1
table =driver.find_elements_by_tag_name('td')
for i in table:
    if i.text == 'BRAND NAME MOLECULE DOSAGE FORM':
        pass
    else:
        td.append(i.text)
        
time.sleep(3)
driver.close()
driver.quit()

for i in range(len(td)):
    if i ==0:
        manufature.append('CIPLA')
        brand_name.append(td[i])
        med_names.append(td[i+1])
        consume_type.append(td[i+2])
        presc.append('Y')
        units.append('1')
        price.append(np.nan)

    if i%3 == 0:
        manufature.append('CIPLA')
        brand_name.append(td[i])
        med_names.append(td[i+1])
        consume_type.append(td[i+2])
        presc.append('Y')
        units.append('1')
        price.append(np.nan)

df = pd.DataFrame({
    "medName": brand_name,
    'manufacturer': manufature,
    "Molecules": med_names,
    "Dosage Form": consume_type,
    'Prescription Required': presc,
    'Units in Pack': units,
    'Price': price
})
df.to_csv('cipla1.csv')

