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
    name = driver.find_elements_by_class_name('PromoSearchResult-title')
    for i in name:
        doc_name.append(i.text)

    location = driver.find_elements_by_class_name('PromoSearchResult-address')
    for i in location:
        doc_location.append(i.text)

    
    hospitals = driver.find_elements_by_class_name('PromoSearchResult-related-desktop')
    for i in hospitals:
        doc_hospitals.append(i.text)

    
    speciality = driver.find_elements_by_class_name('PromoSearchResult-specialty')
    for i in speciality:
        doc_spec.append(i.text)

    phone_number = driver.find_elements_by_class_name('PromoSearchResult-phoneNumber-item')
    for i in phone_number:
        doc_number.append(i.text)

    print(doc_name)
    print('**********************')
    print(doc_location)
    print('**********************')
    print(doc_hospitals)
    print('**********************')
    print(doc_spec)
    print('**********************')
    print(doc_number)
    
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/ps-search-results-module/form/div[2]/ps-search-filters/div/main/div[3]/div[3]/a'))
        )
    driver.execute_script("arguments[0].click();", element)
    
    time.sleep(5)
    driver.quit()
    driver.close()
except Exception as e:
    print(e)


# df= pd.DataFrame({
#     "Name": doc_name,
#     "Raitngs": doc_rating,
#     "Votes": doc_votes
# })
# df.to_csv('srinagar_doctors.csv')