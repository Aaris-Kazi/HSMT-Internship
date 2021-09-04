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
doc_rating = []
doc_votes = []
try:
    def filtersx(x):
        valid_output = []
        for i in x:
            if len(i) == 0:
                pass
            else:
                valid_output.append(i)
        return valid_output


    PATH = r'Task1\chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.justdial.com/Srinagar/Doctors/nct-10892680')
    dev = driver.title
    print(dev)
   
    name = driver.find_elements_by_class_name('lng_cont_name')
    for i in name:
        doc_name.append(i.text)

    
    rating = driver.find_elements_by_class_name('green-box')
    for i in rating:
        doc_rating.append(i.text)

    
    votes = driver.find_elements_by_class_name('rt_count.lng_vote')
    for i in votes:
        doc_votes.append(i.text)

    
    speciality = driver.find_elements_by_class_name('lng_commn')
    for i in speciality:
        doc_spec.append(i.text)

    doc_name = filtersx(doc_name)
    doc_rating = filtersx(doc_rating)
    doc_votes = filtersx(doc_votes)
    doc_spec = filtersx(doc_spec)
    print(doc_name)
    print('**********************')
    print(doc_rating)
    print('**********************')
    print(doc_votes)
    print('**********************')
    print(doc_spec)
    driver.quit()
    driver.close()
except Exception :
    pass

# df= pd.DataFrame({
#     "Name": doc_name,
#     "Raitngs": doc_rating,
#     "Votes": doc_votes
# })
# df.to_csv('srinagar_doctors.csv')
