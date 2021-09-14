from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
PATH = 'chromedriver.exe'
#  Get Hotels data from around each hospital
# Get : Hospital Name ,hotel name , Star rating , Distance from Hotel ,room count ,price range , link
# Check hotels for each hospital from
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(PATH, options=options)
# driver = webdriver.Chrome(PATH)

NA = "NaN"
Name = []
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
            EC.element_to_be_clickable((By.XPATH, '//*[@id="statesearch"]/option[23]'))
        )
states.click()
time.sleep(10)
def fetch():
    i = 0
    names = driver.find_elements_by_class_name("hospital-name")
    for name in names:
        driver.execute_script("arguments[0].click();", name)
        # name.click()
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
fetch()
# page = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, '//*[@id="pagination"]/li[2]'))
#         )
# page.click()
time.sleep(3)
driver.quit()
df = pd.DataFrame({
    'Hospitals': hosp,
    'Hotels': hotel_name
})
# # df = pd.DataFrame(dic)
df.to_csv("hotels_hosp.csv", mode="a", header= False)
