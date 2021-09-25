# https://www.healthgrades.com/hospital-directory/ca-california/san-jose
# https://www.healthgrades.com/hospital-directory/ca-california/san-diego
# https://www.healthgrades.com/hospital-directory/tx-texas/dallas
# name, location, phone_number, verified, rating, country, state, city, payment_mode
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
name, location, phone_number, verified, voting, country, state, city, payment_mode= [],[],[],[],[],[],[],[],[]
links = []
PATH = 'chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(PATH, options=options)
url = 'https://www.healthgrades.com/hospital-directory/ca-california/san-diego'
driver.get(url)
tabs = driver.find_elements_by_class_name('_2YLqr')
i = 0
tabs = driver.find_elements_by_class_name('_2YLqr')
for tab in tabs:
    link = tab.get_attribute('href')
    print(link)
    # tab.click()//*[@id="root"]/div/main/div[1]/div/div[2]/div[2]/svg/g/text//*[@id="root"]/div/main/div[1]/div/div[2]/div[2]/svg/g/text/text()[1]
    time.sleep(2)
    driver.execute_script("arguments[0].click();", tab)
    driver.switch_to.window(driver.window_handles[1])
    h = driver.find_element_by_xpath('//*[@id="root"]/div/main/div[1]/div/div[2]/h1').text
    add = driver.find_element_by_xpath('//*[@id="root"]/div/main/aside/div/div/div[1]/div[1]/div').text
    no = driver.find_element_by_xpath('//*[@id="root"]/div/main/aside/div/div/div[1]/div[1]/p[2]').text
    try:
        vote = driver.find_elements_by_class_name('per-wrapper')
        if len(vote) == 0:
            k = 0
            for j in vote:
                if k ==0:
                    v= j.find_element_by_tag_name('text').text
                    if len(v) == 0:
                        print('Empty')
                    else:
                        # print(v)
                        voting.append(v)
                elif k>1:
                    k=0
                else:
                    pass
                k+=1
        else:
            print('Not Found')
            voting.append('NaN')
        
    except Exception:
        print('Empty')
    name.append(h)
    location.append(add)
    phone_number.append(no)
    links.append(link)
    verified.append('YES')
    payment_mode.append('CASH')
    country.append('USA')
    state.append('California')
    city.append('San Diego')
    time.sleep(1)
    if i >= 1:
        driver.close()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    i +=1
time.sleep(3)
driver.quit()
driver.quit()
