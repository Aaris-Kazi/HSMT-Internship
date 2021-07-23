from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd



# images = driver.find_elements_by_class_name('find-doctor-img.img-effect.green-border')
# for i in  images:
#     image = i.find_element_by_tag_name("img")
#     img_src = image.get_attribute("src")
#     print(img_src)
def main():
    doc_name = []
    doc_spec = []
    hospital = []
    location = []
    price = []
    PATH = r'Qualifying\chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.meddy.com/uae/doctors/cardiologist-dubai/')
    def fetcher():
        # doc_spec = []
        # doc_name = []
        doc_location = []
        doc_hospitals = []
        doc_hospital = []
        doc_price = []
        name = driver.find_elements_by_class_name('listings-card-header.ng-binding')
        # for i in name:
        #     print(i.text)
        speciality = driver.find_elements_by_class_name('col-sm-6.col-xs-12.left-wrapper')
        for i in speciality:
            spec = i.find_element_by_class_name('listings-card-subheader.ng-binding')

        Hospital = driver.find_elements_by_class_name('col-sm-5.col-xs-12.right-wrapper')
        for i in Hospital:
            hop = i.find_element_by_class_name('ng-binding')
            doc_hospitals.append(i.text)
        # for i in doc_hospitals:
        #     hospital, Address, price =i.split('\n')
        #     doc_location.append(Address)
        #     doc_hospital.append(hospital)
        #     doc_price.append(price)
        # return name, spec, doc_hospital, doc_location, doc_price
        return name,doc_hospitals
    def next():
        element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'load-more'))
                    )
        driver.execute_script("arguments[0].click();", element)
    for i in range(3):
        # name, spec, doc_hospital, doc_location, doc_price = fetcher()
        name, doc_hospital = fetcher()
        # for i, j, k, l, m in zip(name, spec, doc_hospital, doc_location, doc_price):
        # for i in zip(name):
        #     doc_name.append(i.text)
            # doc_spec.append(j.text)
            # hospital.append(k)
            # location.append(l)
            # price.append(m)
        for i in doc_hospital:
            hospitals, Address, docprice =i.split('\n')
            location.append(Address)
            hospital.append(hospitals)
            price.append(docprice)
        # next()
    # print(doc_name,doc_spec,hospital,location,price)
    # print(doc_name)
    print(location, hospital, price)
    driver.quit()
    driver.close()  
if __name__ =='__main__':
    main()