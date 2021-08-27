from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd


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
def page(i):
    PATH = r'Task1\chromedriver.exe'
    driver = webdriver.Chrome(PATH)

    driver.get('https://www.justdial.com/Surat/Multispeciality-Hospitals/nct-10547585/page-'+str(i+1)+'')
    dev = driver.title
    print(dev)
    name = driver.find_elements_by_class_name('lng_cont_name')
    rating = driver.find_elements_by_class_name('green-box')
    votes = driver.find_elements_by_class_name('lng_vote')
    speciality = driver.find_elements_by_class_name('lng_commn')
    address = driver.find_elements_by_class_name('cont_sw_addr')
        # address = driver.find_elements_by_class_name('cont_fl_addr')
    contacts = driver.find_elements_by_class_name('mobilesv')
    storeDetails = driver.find_elements_by_class_name('store-details')
    links = driver.find_elements_by_class_name('jcn')
    page_links = []
    for i in links:
        x = i.find_element_by_tag_name('a')
        page_links.append(x.get_attribute('href'))
        # print(page_links)
    img_links = driver.find_elements_by_class_name('altImgcls')
    numbersList = []
    for i in range(len(storeDetails)):
        contactList = storeDetails[i].find_elements_by_class_name('mobilesv')
        myList = []

        for j in range(len(contactList)):
            myString = contactList[j].get_attribute('class').split("-")[1]
            myList.append(strings_to_num(myString))

        numbersList.append("".join(myList))
        
    
    return name, rating, votes,speciality, address, numbersList, img_links, page_links
    driver.close()
    driver.quit()
    # print(name)
    # print(len(name))


def main():
    doc_spec = []
    doc_name = []
    doc_rating = []
    doc_votes = []
    doc_add = []
    doc_contacts =[]
    doc_links =[]
    doc_page =[]
    for i in range(10):
        # name = page(i)
        # for i in name:
        #     doc_name.append(i.text)
        names, ratings, votes, specialties, address, contacts, img_links, page_links = page(i)
        for i in contacts:
            doc_contacts.append(i)
        for i, j, k, l, m, n, o in zip(names, ratings, votes, specialties, address, img_links, page_links):
            doc_name.append(i.text)
            doc_rating.append(j.text)
            doc_votes.append(k.text)
            doc_spec.append(l.text)
            doc_add.append(m.text)
            doc_links.append(n.get_attribute('src'))
            doc_page.append(o)

    doc_name = filtersx(doc_name)
    doc_rating = filtersx(doc_rating)
    doc_votes = filtersx(doc_votes)
    doc_spec = filtersx(doc_spec)
    doc_add = filtersx(doc_add)
    # print(doc_name)
    print(len(doc_name))
    print(len(doc_rating))
    print(len(doc_votes))
    print(len(doc_spec))
    print(len(doc_add))
    print(len(doc_contacts))
    print(len(doc_links))
    print(len(doc_page))
    df= pd.DataFrame({
        'Photo': doc_links,
        "Name": doc_name,
        "Speciality": doc_spec,
        "Address": doc_add,
        "Contacts": doc_contacts,
        "Page Link": doc_page,
        "Raitngs": doc_rating,
        "Votes": doc_votes
    })
    df.to_csv('surat_doctors1.csv')

if __name__ == '__main__':
    main()