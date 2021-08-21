from selenium import webdriver
import pandas as pd

PATH = r'Task1\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://www.justdial.com/Surat/Women-Dermatologists/nct-12101295')
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

storeDetails = driver.find_elements_by_class_name('store-details')

nameList = []
addressList = []
numbersList = []

for i in range(len(storeDetails)):

    name = storeDetails[i].find_element_by_class_name('lng_cont_name').text
    address = storeDetails[i].find_element_by_class_name('cont_sw_addr').text
    contactList = storeDetails[i].find_elements_by_class_name('mobilesv')

    myList = []

    for j in range(len(contactList)):
        myString = contactList[j].get_attribute('class').split("-")[1]

        myList.append(strings_to_num(myString))

    nameList.append(name)
    addressList.append(address)
    numbersList.append("".join(myList))

data = {'Company Name': nameList,
        'Address': addressList,
        'Phone': numbersList}

df = pd.DataFrame(data)
print(df)

df.to_csv('doctors_data.csv', mode='w', header=False)
