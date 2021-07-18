from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException
import filter

PATH = r'chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://docplus.online')
dev = driver.title
print(dev)
search = driver.find_element_by_class_name('ant-input.ant-input-lg')
search.click()
search.send_keys('Dentist')

search_button = driver.find_element_by_class_name('search-icon')
search_button.click()

time.sleep(1)
doc_name = driver.find_elements_by_tag_name('div')

op = ''
try:
    for i in doc_name:
        if 'Dr.' in i.text:
            op =  str(i.text)


except StaleElementReferenceException :
    driver.close()
    driver.quit()

f = open('document.txt', 'w')
f.write(op)
f.close()

time.sleep(3)

filter.making_to_csv()