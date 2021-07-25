from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd

def filtersx(x):
    valid_output = []
    for i in x:
        if len(i) == 0:
            pass
        else:
            valid_output.append(i)
    return valid_output

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
    
def for_unique(list1):
    i= 0
    # print(len(list1))
    unique_list = []
    try:
        while i <= len(list1):
            # print(list1[i].text)
            unique_list.append(list1[i].text)
            i += 2
    except Exception:
        pass
    return unique_list

def unique_list(list1):
    i= 0
    unique_list = []
    try:
        while i <= len(list1):
            unique_list.append(list1[i])
            i += 2
    except Exception:
        pass
    return unique_list
try:
    PATH = r'Qualifying\chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.abeergroup.com/ksa/Doctors.aspx')
    dev = driver.title
    print(dev)
    name = driver.find_elements_by_class_name('Drname.ng-binding')
    htag = driver.find_elements_by_tag_name('strong')
    des = driver.find_elements_by_class_name('DrDept.ng-binding')
    design, location = [], []
    hospitals = []
    for i in des:
        design.append(i.text)
    design= filtersx(design)
    design = unique_list(design)
    # print(len(design))
    doctor_name= for_unique(name)
    # print(len(doctor_name))
    hospital = for_unique(htag)
    # print(len(hospital))
    for i in hospital:
        # print(i)
        if '-' in i:
            hospital_name, loc = i.split('-')
            location.append(loc)
            hospitals.append(hospital_name)
        else:
            hospital_name, loc = i.split('Ruwais')
            location.append('Ruwais')
            hospitals.append(hospital_name)
    print(len(location))
    print(len(hospitals))
    
    driver.quit()
    driver.close()
except Exception:
    pass


df= pd.DataFrame({
    "Name": doctor_name,
    "Speciality": design,
    "Location": location,
    "Hospitals": hospitals,
    # "Phone Number": doc_price
})
df.to_csv('doctors_ksa.csv')