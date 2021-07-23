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
driver.get('https://www.zulekhahospitals.com/dubai/best-doctors-in-dubai')

images = driver.find_elements_by_class_name('find-doctor-img.img-effect.green-border')
for i in  images:
    image = i.find_element_by_tag_name("img")
    img_src = image.get_attribute("src")
    print(img_src)

name = driver.find_elements_by_class_name('sm-tit')
for i in name:
    print(i.text)
speciality = driver.find_elements_by_class_name('des1')
for i in speciality:
    print(i.text)

Hospital = driver.find_elements_by_class_name('des')
for i in Hospital:
    print(i.text)
dev = driver.title
element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'load-more'))
            )
driver.execute_script("arguments[0].click();", element)
driver.quit()
driver.close()  