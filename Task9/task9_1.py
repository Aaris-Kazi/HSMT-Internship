from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd
contacts = []
links = []
# PATH = r'msedgedriver.exe'
# driver = webdriver.Edge(PATH)
PATH = r'chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(PATH, options=options)
# url = 'https://www.indiahealthcare.org/?speciality=Urology'
url = 'https://www.indiahealthcare.org/?speciality=Diabetes%20%26%20Endocrinology'
driver.get(url)
dev = driver.title
print(dev)
name = driver.find_elements_by_class_name('hospital-name')
location = driver.find_elements_by_class_name('hospital-location')
# for names in name:
#     name.click()
for i in range(len(location)):
    contact = driver.find_element_by_xpath('//*[@id="searched_results"]/div/div['+str(i+1)+']/div/p[2]').text
    contact = str(contact).replace('Contact - ', '')
    contacts.append(contact)
    print(contact)

for i, j in zip(name, location):
    print(i.text)
    print(j.text)
    # driver.execute_script("arguments[0].click();", i)
time.sleep(5)
driver.close()
driver.quit()
# //*[@id="searched_results"]/div/div[2]/div/p[2]
# //*[@id="pagination"]/li[1]/a