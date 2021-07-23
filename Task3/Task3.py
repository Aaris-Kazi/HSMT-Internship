from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd

doc_spec = []
doc_name = []
doc_location = []
doc_hospitals = []
doc_number = []
name, spec, hop= [],[],[]
PATH = r'Qualifying\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://www.meddy.com/uae/doctors/cardiologist-dubai/')

# images = driver.find_elements_by_class_name('find-doctor-img.img-effect.green-border')
# for i in  images:
#     image = i.find_element_by_tag_name("img")
#     img_src = image.get_attribute("src")
#     print(img_src)

name = driver.find_elements_by_class_name('listings-card-header.ng-binding')
for i in name:
    print(i.text)

speciality = driver.find_elements_by_class_name('col-sm-6.col-xs-12.left-wrapper')
for i in speciality:
    spec = i.find_element_by_class_name('listings-card-subheader.ng-binding')
    print(spec.text)

Hospital = driver.find_elements_by_class_name('col-sm-5.col-xs-12.right-wrapper')
for i in Hospital:
    hop = i.find_element_by_class_name('ng-binding')
    doc_hospitals.append(i.text)
for i in doc_hospitals:
    hospital, Address, price =i.split('\n')
print(hospital, Address, price)
# dev = driver.title
# element = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.CLASS_NAME, 'load-more'))
#             )
# driver.execute_script("arguments[0].click();", element)
driver.quit()
driver.close()  