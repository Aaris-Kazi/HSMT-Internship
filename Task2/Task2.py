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
try:

    PATH = r'Qualifying\chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.castleconnolly.com/search?q=neurologist&postalCode=&location=Illinois+City%2C+IL&tf1=5117bfc9-a93e-3ba3-82f1-73359a3d585e')
    dev = driver.title
    print(dev) 
    def get_detail():
        time.sleep(1)
        name = driver.find_elements_by_class_name('PromoSearchResult-title')
        location = driver.find_elements_by_class_name('PromoSearchResult-address')
        hospitals = driver.find_elements_by_class_name('PromoSearchResult-related-desktop')
        speciality = driver.find_elements_by_class_name('PromoSearchResult-specialty')
        phone_number = driver.find_elements_by_class_name('PromoSearchResult-phoneNumber-item')
        return name, location, hospitals, speciality, phone_number
        
    
    for i in range(3):
        name, location, hospitals, speciality, phone_number = get_detail()
        for i, j, k, l, m in zip(name, location, hospitals, speciality, phone_number) :
            doc_name.append(i.text)
            doc_location.append(j.text)
            doc_hospitals.append(k.text)
            doc_spec.append(l.text)
            doc_number.append(m.text)
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'SearchResultsModule-nextPage'))
            )
            driver.execute_script("arguments[0].click();", element)

    print(doc_name)
    print('**********************')
    print(doc_location)
    print('**********************')
    print(doc_hospitals)
    print('**********************')
    print(doc_spec)
    print('**********************')
    print(doc_number)
    time.sleep(5)
    driver.quit()
    driver.close()
except Exception as e:
    print(e)


df= pd.DataFrame({
    "Name": doc_name,
    "Speciality": doc_spec,
    "Location": doc_location,
    "Hospitals": doc_hospitals,
    "Phone Number": doc_number
})
df.to_csv('doctors_usa.csv')
