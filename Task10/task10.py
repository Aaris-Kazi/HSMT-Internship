# https://www.healthgrades.com/hospital-directory/ca-california/san-jose
# https://www.healthgrades.com/hospital-directory/ca-california/san-diego
# https://www.healthgrades.com/hospital-directory/tx-texas/dallas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
PATH = 'chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(PATH, options=options)
url = 'https://www.healthgrades.com/hospital-directory/ca-california/san-jose'
driver.get(url)
# _2YLqr
i = 0
tabs = driver.find_elements_by_class_name('_2YLqr')
for tab in tabs:
    # tab.click()
    time.sleep(1)
    driver.execute_script("arguments[0].click();", tab)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    if i >= 1:
        driver.close()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    i +=1
time.sleep(3)
driver.close()
driver.quit()