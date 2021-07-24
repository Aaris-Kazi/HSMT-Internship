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
doc_hospital = []
doc_price = []
try:

    PATH = r'Qualifying\chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.meddy.com/uae/doctors/cardiologist-dubai/')
    dev = driver.title
    print(dev) 
    def get_detail():
        doc_hospitals = []
        time.sleep(1)
        name = driver.find_elements_by_class_name('listings-card-header.ng-binding')
        speciality = driver.find_elements_by_class_name('col-sm-6.col-xs-12.left-wrapper')
        Hospital = driver.find_elements_by_class_name('col-sm-5.col-xs-12.right-wrapper')
        for i in Hospital:
            hop = i.find_element_by_class_name('ng-binding')
            doc_hospitals.append(i.text)
        return name, speciality, doc_hospitals
        
    
    for i in range(1):
        name, speciality, doc_hospitals = get_detail()
        for i in name:
            doc_name.append(i.text)
        for i in speciality:
            spec = i.find_element_by_class_name('listings-card-subheader.ng-binding')
            doc_spec.append(spec.text)
        for i in doc_hospitals:
            hospital, Address, price =i.split('\n')
            doc_hospital.append(hospital)
            doc_location.append(Address)
            doc_price.append(price)
        # next = driver.find_element_by_class_name('next')
        # nexting = next.find_element_by_tag_name('a')
        # nexting.click()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'meddy-light-chevron.gray-chevron.chevron-right'))
        )
        driver.execute_script("arguments[0].click();", element)

    print(doc_name)
    print('**********************')
    print(doc_location)
    print('**********************')
    print(doc_hospital)
    print('**********************')
    print(doc_spec)
    print('**********************')
    print(doc_price)
    time.sleep(5)
    driver.quit()
    driver.close()
except Exception as e:
    pass


df= pd.DataFrame({
    "Name": doc_name,
    "Speciality": doc_spec,
    "Location": doc_location,
    "Hospitals": doc_hospitals,
    "Phone Number": doc_price
})
df.to_csv('doctors_uae.csv')
