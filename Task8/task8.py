
# https://www.justdial.com/Surat/260/Medical_fil
# https://www.justdial.com/Lucknow/260/Medical_fil
# jcl
# https://www.justdial.com/Surat/Multispeciality-Hospitals/nct-10547585
# jcn
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
doc_links =[]
doc_page =[]
try:
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

    driver.get('https://www.justdial.com/Surat/Sanskruti-Prasutigruh-Surgical-Hospital-Katargam/0261PX261-X261-190213231728-S5Y6_BZDET?xid=U3VyYXQgTXVsdGlzcGVjaWFsaXR5IEhvc3BpdGFscw==')
    dev = driver.title
    print(dev)
    # def get_details():

    #     name = driver.find_elements_by_class_name('lng_cont_name')
    #     rating = driver.find_elements_by_class_name('green-box')
    #     votes = driver.find_elements_by_class_name('lng_vote')
    #     speciality = driver.find_elements_by_class_name('lng_commn')
    #     address = driver.find_elements_by_class_name('cont_sw_addr')
    #     # address = driver.find_elements_by_class_name('cont_fl_addr')
    #     contacts = driver.find_elements_by_class_name('mobilesv')
    #     storeDetails = driver.find_elements_by_class_name('store-details')
    #     links = driver.find_elements_by_class_name('jcn')
    #     page_links = []
    #     for i in links:
    #         x = i.find_element_by_tag_name('a')
    #         page_links.append(x.get_attribute('href'))
    #     # print(page_links)
    #     img_links = driver.find_elements_by_class_name('altImgcls')
    #     numbersList = []
    #     for i in range(len(storeDetails)):
    #         contactList = storeDetails[i].find_elements_by_class_name('mobilesv')
    #         myList = []

    #         for j in range(len(contactList)):
    #             myString = contactList[j].get_attribute('class').split("-")[1]
    #             myList.append(strings_to_num(myString))

    #         numbersList.append("".join(myList))
        
    #     return name, rating, votes,speciality, address, numbersList, img_links, page_links
            
    # for i in range(1):
    #     names, ratings, votes, specialties, address, contacts, img_links, page_links = get_details()
    #     for i in contacts:
    #         doc_contacts.append(i)
    #     for i, j, k, l, m, n, o in zip(names, ratings, votes, specialties, address, img_links, page_links):
    #         doc_name.append(i.text)
    #         doc_rating.append(j.text)
    #         doc_votes.append(k.text)
    #         doc_spec.append(l.text)
    #         doc_add.append(m.text)
    #         doc_links.append(n.get_attribute('src'))
    #         doc_page.append(o)

    #     element = WebDriverWait(driver, 10).until(
    #                     # EC.element_to_be_clickable((By.CLASS_NAME, 'SearchResultsModule-nextPage'))//*[@id="srchpagination"]/a[3]
    #             EC.element_to_be_clickable((By.XPATH, '//*[@id="srchpagination"]/a[11]'))
    #     )
    #     driver.execute_script("arguments[0].click();", element)
    # doc_name = filtersx(doc_name)
    # doc_rating = filtersx(doc_rating)
    # doc_votes = filtersx(doc_votes)
    # doc_spec = filtersx(doc_spec)
    # doc_add = filtersx(doc_add)
    # # print(doc_name)
    # # print(doc_rating)
    # # print(doc_votes)
    # # print(doc_spec)
    # print(doc_add)
    # # print(doc_links)
    # # print(doc_contacts)
    # print(len(doc_name))
    # print(len(doc_rating))
    # print(len(doc_votes))
    # print(len(doc_spec))
    # print(len(doc_add))
    # print(len(doc_contacts))
    # print(len(doc_links))
    # print(len(doc_page))
    driver.quit()
    driver.close()
except Exception as e:
    # pass
    print(e)

# def strings_to_num(argument):
#     switcher = {
#         'dc': '+',
#         'fe': '(',
#         'hg': ')',
#         'ba': '-',
#         'acb': '0',
#         'yz': '1',
#         'wx': '2',
#         'vu': '3',
#         'ts': '4',
#         'rq': '5',
#         'po': '6',
#         'nm': '7',
#         'lk': '8',
#         'ji': '9'
#     }
#     return switcher.get(argument, "nothing")
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

# driver.get('https://www.justdial.com/Surat/Multispeciality-Hospitals/nct-10547585')
# dev = driver.title
# print(dev)
# def get_details():

#     name = driver.find_elements_by_class_name('lng_cont_name')
#     rating = driver.find_elements_by_class_name('green-box')
#     votes = driver.find_elements_by_class_name('lng_vote')
#     speciality = driver.find_elements_by_class_name('lng_commn')
#     address = driver.find_elements_by_class_name('cont_sw_addr')
#     # address = driver.find_elements_by_class_name('cont_fl_addr')
#     contacts = driver.find_elements_by_class_name('mobilesv')
#     storeDetails = driver.find_elements_by_class_name('store-details')
#     links = driver.find_elements_by_class_name('jcn')
#     page_links = []
#     for i in links:
#         x = i.find_element_by_tag_name('a')
#         page_links.append(x.get_attribute('href'))
#     # print(page_links)
#     img_links = driver.find_elements_by_class_name('altImgcls')
#     numbersList = []
#     for i in range(len(storeDetails)):
#         contactList = storeDetails[i].find_elements_by_class_name('mobilesv')
#         myList = []

#         for j in range(len(contactList)):
#             myString = contactList[j].get_attribute('class').split("-")[1]
#             myList.append(strings_to_num(myString))

#         numbersList.append("".join(myList))
    
#     return name, rating, votes,speciality, address, numbersList, img_links, page_links
        
# for i in range(2):
#     names, ratings, votes, specialties, address, contacts, img_links, page_links = get_details()
#     for i in contacts:
#         doc_contacts.append(i)
#     for i, j, k, l, m, n, o in zip(names, ratings, votes, specialties, address, img_links, page_links):
#         doc_name.append(i.text)
#         doc_rating.append(j.text)
#         doc_votes.append(k.text)
#         doc_spec.append(l.text)
#         doc_add.append(m.text)
#         doc_links.append(n.get_attribute('src'))
#         doc_page.append(o)
#         # print("".join(n))
#         # conctact = contacts[n].get_attribute('class').split("-")[1]
#         # doc_contacts.append(strings_to_num(conctact))

#     # element = WebDriverWait(driver, 10).until(
#     #                 # EC.element_to_be_clickable((By.CLASS_NAME, 'SearchResultsModule-nextPage'))//*[@id="srchpagination"]/a[3]
#     #         EC.element_to_be_clickable((By.XPATH, '//*[@id="srchpagination"]/a[3]'))
#     # )
#     # driver.execute_script("arguments[0].click();", element)
# doc_name = filtersx(doc_name)
# doc_rating = filtersx(doc_rating)
# doc_votes = filtersx(doc_votes)
# doc_spec = filtersx(doc_spec)
# doc_add = filtersx(doc_add)
# # print(doc_name)
# # print(doc_rating)
# # print(doc_votes)
# # print(doc_spec)
# # print(doc_add)
# # print(doc_links)
# # print(doc_contacts)
# print(len(doc_name))
# print(len(doc_rating))
# print(len(doc_votes))
# print(len(doc_spec))
# print(len(doc_add))
# print(len(doc_contacts))
# print(len(doc_links))
# print(len(doc_page))
# driver.quit()
# driver.close()
# df= pd.DataFrame({
#     'Photo': doc_links,
#     "Name": doc_name,
#     "Speciality": doc_spec,
#     "Address": doc_add,
#     "Contacts": doc_contacts,
#     "Page Link": doc_page,
#     "Raitngs": doc_rating,
#     "Votes": doc_votes
# })
# df.to_csv('surat_doctors.csv')

