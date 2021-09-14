from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#  Get Hotels data from around each hospital
# Get : Hospital Name ,hotel name , Star rating , Distance from Hotel ,room count ,price range , link
# Check hotels for each hospital from
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

NA = "NaN"
Name = [];Speciality = []; Address = []
Landline = [];Mobile = []; email = []
Website = []; TotalBeds = []; ICUBeds = []
Operatingrooms = []; Intlarr = []
Procedure = []; MaxCost = [];MinCost = []
Mindays = [];Maxdays = [];Certificate = []
hotel_name, star, distance, room, price = [], [], [], [], []
hosp = []
temp = ''
# url = 'https://www.indiahealthcare.org/?speciality=Diabetes%20%26%20Endocrinology'
url = 'https://www.indiahealthcare.org/?speciality=None/'
# url = 'https://www.indiahealthcare.org/?speciality=Urology'
# url = 'https://www.indiahealthcare.org/?speciality=Dermatology'
driver.get(url)
# search = driver.find_element_by_class_name('search-btn')
# search.click()
# state = driver.find_element_by_class_name('dropdown_selection')
element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="statesearch"]'))
        )
# driver.execute_script("arguments[0].click();", element)
element.click()
# states = driver.find_element_by_xpath('//*[@id="statesearch"]/option[2]')
# //*[@id="statesearch"]/option[14]
states = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="statesearch"]/option[14]'))
        )
states.click()
# //*[@id="statesearch"]/option[2]

def fetch():
    i = 0
    names = driver.find_elements_by_class_name("hospital-name")
    for name in names:
        driver.execute_script("arguments[0].click();", name)
        # print(name.text)
        temp = name.text
        i+=1
        time.sleep(2)
        Name.append(name.text)
        driver.switch_to.window(driver.window_handles[i])
        time.sleep(1)
        around_hospital = driver.find_element_by_id('nav-around-tab')
        around_hospital.click()
        hotel = driver.find_elements_by_class_name('hospital-item-card')
        for n in hotel:
            # print(temp)
            hosp.append(temp)
            # x = n.find_element_by_class_name('hospital-item-card_value')
            hotel_name.append(n.text)
            # print(n.text)
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        # driver.current_window_handle
# fetch()
# for j in range(2, 4):

#     fetch()
    
        
#     next = driver.find_element_by_xpath('//*[@id="pagination"]/li['+str(j)+']/a')
#     next.click()
# //*[@id="pagination"]/li[3]///*[@id="pagination"]/li[3]/a
# //*[@id="pagination"]/li[2]/a
# pages = driver.find_elements_by_class_name('page-link')
# pages = driver.find_element_by_xpath('//*[@id="pagination"]/li[2]')
# pages.click()
# pages = driver.find_elements_by_class_name('page-link')
page = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="pagination"]/li[2]'))
        )
page.click( )
# driver.execute_script("arguments[0].click();", pages)//*[@id="pagination"]/li[2]
# for page in pages:
#     print(page.text)
    # driver.execute_script("arguments[0].click();", pages)
# df = pd.DataFrame({
#     'Hospitals': hosp,
#     'Hotels': hotel_name
# })
# df = pd.DataFrame(dic)
# df.to_csv("hotel.csv", mode="a", header= False)
time.sleep(3)
driver.quit()
