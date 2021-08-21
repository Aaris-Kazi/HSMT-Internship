
# https://www.justdial.com/Surat/260/Medical_fil
# https://www.justdial.com/Lucknow/260/Medical_fil
# jcl
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
doc_add = []
doc_contacts =[]
# try:
    # def filtersx(x):
    #     valid_output = []
    #     for i in x:
    #         if len(i) == 0:
    #             valid_output.append('NaN')
    #         else:
    #             valid_output.append(i)
    #     return valid_output


    # PATH = r'Task1\chromedriver.exe'
    # driver = webdriver.Chrome(PATH)
    # driver.get('https://www.justdial.com/Surat/Women-Dermatologists/nct-12101295')
    # dev = driver.title
    # print(dev)
    # def get_details():

    #     name = driver.find_elements_by_class_name('lng_cont_name')
    #     rating = driver.find_elements_by_class_name('green-box')
    #     votes = driver.find_elements_by_class_name('lng_vote')
    #     speciality = driver.find_elements_by_class_name('lng_commn')
    #     address = driver.find_element_by_class_name('cont_sw_addr')
    #     element = WebDriverWait(driver, 15).until(
    #                 # EC.element_to_be_clickable((By.CLASS_NAME, 'SearchResultsModule-nextPage'))
    #             EC.element_to_be_clickable((By.CLASS_NAME, 'jcl'))
    #         )
    #     driver.execute_script("arguments[0].click();", element)
    #     return name, rating, votes, address
        
    # for i in range(2):
    #     names, ratings, votes, specialties, address = get_details()
    #     for i, j, k, l, m in zip(names, ratings, votes, specialties, address):
    #         doc_name.append(i.text)
    #         doc_rating.append(j.text)
    #         doc_votes.append(k.text)
    #         doc_spec.append(l.text)
    #         doc_add.append(m.text)
    #     element = WebDriverWait(driver, 10).until(
    #                 # EC.element_to_be_clickable((By.CLASS_NAME, 'SearchResultsModule-nextPage'))
    #             EC.element_to_be_clickable((By.XPATH, '//*[@id="srchpagination"]/a[3]'))
    #         )
    #     driver.execute_script("arguments[0].click();", element)
    # doc_name = filtersx(doc_name)
    # doc_rating = filtersx(doc_rating)
    # doc_votes = filtersx(doc_votes)
    # doc_spec = filtersx(doc_spec)
    # doc_add = filtersx(doc_add)
    # print(doc_name)
    # print(doc_rating)
    # print(doc_votes)
    # print(doc_spec)
    # print(doc_add)
    # print(len(doc_name))
    # print(len(doc_rating))
    # print(len(doc_votes))
    # print(len(doc_spec))
    # print(len(doc_add))
    # driver.quit()
    # driver.close()
# except Exception as e:
#     # pass
#     print(e)

def strings_to_num(argument):
    switcher = {
        'dc': '+',
        'fe': '(',
        'hg': ')',
        'ba': '-',
        'acb': '0',
        'yz': '1',
        'wx': '2',
        'vu': '3',
        'ts': '4',
        'rq': '5',
        'po': '6',
        'nm': '7',
        'lk': '8',
        'ji': '9'
    }
    return switcher.get(argument, "nothing")
def filtersx(x):
    valid_output = []
    for i in x:
        if len(i) == 0:
            valid_output.append('NaN')
        else:
            valid_output.append(i)
    return valid_output


PATH = r'Task1\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.justdial.com/Surat/Women-Dermatologists/nct-12101295')
dev = driver.title
print(dev)
def get_details():

    name = driver.find_elements_by_class_name('lng_cont_name')
    rating = driver.find_elements_by_class_name('green-box')
    votes = driver.find_elements_by_class_name('lng_vote')
    speciality = driver.find_elements_by_class_name('lng_commn')
    address = driver.find_elements_by_class_name('cont_sw_addr')
    contacts = driver.find_elements_by_class_name('mobilesv')
    # element = WebDriverWait(driver, 15).until(
    #                 # EC.element_to_be_clickable((By.CLASS_NAME, 'SearchResultsModule-nextPage'))
    #         EC.element_to_be_clickable((By.CLASS_NAME, 'jcl'))
    # )
    # driver.execute_script("arguments[0].click();", element)
    # return name, rating, votes, address
    return name, rating, votes,speciality, address, contacts
        
for i in range(2):
    names, ratings, votes, specialties, address, contacts = get_details()
    for i, j, k, l, m, n in zip(names, ratings, votes, specialties, address, contacts):
        doc_name.append(i.text)
        doc_rating.append(j.text)
        doc_votes.append(k.text)
        doc_spec.append(l.text)
        doc_add.append(m.text)
    element = WebDriverWait(driver, 10).until(
                    # EC.element_to_be_clickable((By.CLASS_NAME, 'SearchResultsModule-nextPage'))//*[@id="srchpagination"]/a[3]
            EC.element_to_be_clickable((By.XPATH, '//*[@id="srchpagination"]/a[3]'))
    )
    driver.execute_script("arguments[0].click();", element)
doc_name = filtersx(doc_name)
doc_rating = filtersx(doc_rating)
doc_votes = filtersx(doc_votes)
doc_spec = filtersx(doc_spec)
doc_add = filtersx(doc_add)
print(doc_name)
print(doc_rating)
print(doc_votes)
print(doc_spec)
print(doc_add)
print(len(doc_name))
print(len(doc_rating))
print(len(doc_votes))
print(len(doc_spec))
print(len(doc_add))
driver.quit()
driver.close()
# df= pd.DataFrame({
#     "Name": doc_name,
#     "Raitngs": doc_rating,
#     "Votes": doc_votes
# })
# df.to_csv('surat_doctors.csv')

# //*[@id="srchpagination"]/a[3]
