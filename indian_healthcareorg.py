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
url = 'https://www.indiahealthcare.org/?speciality=None/'
driver.get(url)
element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="statesearch"]'))
        )
element.click()
states = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="statesearch"]/option[2]'))
        )
states.click()
driver.get(url)
time.sleep(10)
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
            print(temp)
            hosp.append(temp)
            # x = n.find_element_by_class_name('hospital-item-card_value')
            hotel_name.append(n.text)
            # print(n.text)

        
        # try:
        #     htname = driver.find_element_by_xpath('//*[@id="nav-around"]/div[1]/div/div/div/span[1]/span[2]').text
        #     hotel_name.append(htname)
        #     print(htname)
        # except Exception:
        #     hotel_name.append('NaN')
        time.sleep(1)
        # //*[@id="nav-around"]/div[1]/div/div/div/span[1]/span[2]
        # //*[@id="nav-around"]/div[1]/div/div/div/span[2]/span[2]
        # //*[@id="nav-around"]/div[1]/div/div/div[2]/span[1]/span[2]
# //*[@id="nav-around"]/div[1]/div/div/div[1]/span[1]/span[2]

        # try:
        #     address = driver.find_element_by_class_name("hospital-content").text
        #     Address.append(address.split('ADDRESS')[1].lstrip('\n'))
        # except:Address.append(NA)

        # try:
        #     TotalBeds.append(driver.find_element_by_id('beds_count').text)
        # except:TotalBeds.append(NA)

        # try:
        #     ICUBeds.append(driver.find_element_by_id('icu_beds').text)
        # except:ICUBeds.append(NA)

        # try:
        #     Operatingrooms.append(driver.find_element_by_id('operating_rooms').text)
        # except:Operatingrooms.append(NA)

        # try:
        #     Intlarr.append(driver.find_element_by_id('intl_patients').text)
        # except:Intlarr.append(NA)

        # try:
        #     Landline.append(driver.find_element_by_xpath('/html/body/section/hospital-data/div/div/div[2]/div[3]/div[1]/p[2]').text)
        # except:Landline.append(NA)

        # try:
        #     Mobile.append(driver.find_element_by_xpath('/html/body/section/hospital-data/div/div/div[2]/div[3]/div[2]/p[2]').text)
        # except:Mobile.append(NA)

        # try:
        #     Website.append(driver.find_element_by_xpath('/html/body/section/hospital-data/div/div/div[2]/div[3]/div[3]/p[2]/b/a').text)
        # except:Website.append(NA)

        # try:
        #     email.append(driver.find_element_by_xpath('/html/body/section/hospital-data/div/div/div[2]/div[3]/div[4]/p[2]/b').text)
        # except:email.append(NA)
        # # Accreditions Photo
        # try:
        #     accrds = driver.find_elements_by_class_name('mr-4 > img')
        #     Certificate.append(' , '.join([str(elem.get_attribute('src')) for elem in accrds]))
        # except:Certificate.append(NA)

        # print(driver.current_window_handle)
        driver.switch_to.window(driver.window_handles[0])
        # driver.current_window_handle
fetch()
# for j in range(2, 4):

#     fetch()
    
        
#     next = driver.find_element_by_xpath('//*[@id="pagination"]/li['+str(j)+']/a')
#     next.click()
# //*[@id="pagination"]/li[3]///*[@id="pagination"]/li[3]/a

# df = pd.DataFrame({
#     'Hospitals': hosp,
#     'Hotels': hotel_name
# })
# df = pd.DataFrame(dic)
# df.to_csv("hotel.csv", mode="a", header= False)
driver.quit()
