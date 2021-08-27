from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

PATH = r'Task1\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# options = webdriver.ChromeOptions()
# options.add_argument('--disable-blink-features=AutomationControlled')
# driver = webdriver.Chrome(PATH,ChromeDriverManager().install(),options=options)

driver.get("https://www.justdial.com/Surat/Sanskruti-Prasutigruh-Surgical-Hospital-Katargam/0261PX261-X261-190213231728-S5Y6_BZDET?xid=U3VyYXQgTXVsdGlzcGVjaWFsaXR5IEhvc3BpdGFscw==")
link = []
NA = "NaN"
# '<span class="lng_cont_name">Hcg Ics Khubchandani Cancer..</span>'

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

hosps = driver.find_elements_by_class_name("store-name > span > a")
for hosp in hosps:
    link.append(hosp.get_attribute("href"))

# ---------Ignore-------------
# link = ["https://www.justdial.com/Mumbai/Thunga-Hospital-Pvt-Ltd-TMRCT-Near-Jsw-Ltd-Takinaka-Tarapur-MIDC/022PXX22-XX22-170814131518-J5G6_BZDET?xid=TXVtYmFpIFB1YmxpYyBIb3NwaXRhbHM=",]
# link = ['https://www.justdial.com/Mumbai/Srv-Mamata-Hospital-Near-Omkar-International-School-Next-to-ICICI-Bank-Dombivli-East/022P1152424_BZDET?xid=TXVtYmFpIFB1YmxpYyBIb3NwaXRhbHM=']
# link = ['https://www.justdial.com/Mumbai/Srv-Hospital-Goregaon-Near-Jawahar-Nagar-Phatak-Jawahar-Nagar-goregaon-West/022PXX22-XX22-180706122025-E1F2_BZDET?xid=TXVtYmFpIFB1YmxpYyBIb3NwaXRhbHM=']

for l in link:
    print(l)
    driver.get(l)
    time.sleep(1)
    city = "Mumbai"
    state = "Maharashtra"
    country = "India"
    type = "Hospital"

    try:
        name = driver.find_element_by_class_name("rstotle > span > span").text
        print("Name : ",name)
    except:
        name = NA
        print("Name : ",name)

    try:
        ratings = driver.find_element_by_class_name("total-rate > span").text
        print("Rat : ", ratings)
    except:
        print("Rat : ", NA)

    try:
        votes = driver.find_element_by_class_name("rtngsval > span").text
        print("Votes : ",votes)
    except:
        pass

    try:
        driver.find_element_by_class_name("jd_verified")
        verified = "Y"
        print("Verified : ",verified)
    except:
        pass

    try:
        add = driver.find_element_by_id("fulladdress").text
        print("Address : ",add)
    except:
        pass

    try:
        web = driver.find_elements_by_class_name("mreinfp.comp-text > a")
        web = ' , '.join([str(elem) for elem in [w.get_attribute("href") for w in web if w.get_attribute("href")]])
        print("Websites : ",web)
        # for w in web:
        #     if w.get_attribute("href"):
        #         print("Web : ",w.get_attribute("href"))
    except:
        pass

    try:
        bt = driver.find_element_by_id("vhall")
        driver.execute_script("arguments[0].click();", bt)
        time.sleep(1)
        open = driver.find_element_by_id("mhd").text.split(")")[1].split("\n")
        open = ','.join([str(elem) for elem in open])
        print("Timings : ",open)
    except:
        pass

    try:
        info = driver.find_element_by_id("qckinf").text
        amn = info.split("Amenities")[1].split("\n")
        amn = ','.join([str(elem).lstrip() for elem in amn])
        print("Amn : ",amn)
        serv = info.split("Amenities")[0].split("Services")[1].split("\n")
        serv = ','.join([str(elem).lstrip() for elem in serv])
        print("Services : ",serv)
    except:
        pass

    try:
        pay = ','.join([str(elem.text) for elem in driver.find_elements_by_class_name('lng_mdpay')])
        print("Payment : ",pay)
    except:
        pass

    try:
        try:
            year = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[4]/div[1]/div[8]/ul/li').text
        except:
            year = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[4]/div[1]/div[6]/ul/li').text
        print("Year Established : ",year)
    except:
        pass

    try:
        social = driver.find_element_by_class_name("social_media_icons > a").get_attribute("href")
        print("Social : ",social)
    except:pass

    print("------------------------------------------------------")


driver.quit()

