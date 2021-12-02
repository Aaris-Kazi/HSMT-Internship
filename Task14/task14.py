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

url = 'https://www.zocdoc.com/'
driver.get(url)
try:
    search =driver.find_element_by_xpath('//*[@id="main"]/div[1]/main/div[1]/section/div/div/div/form/div/div/div/div[1]/div/div/div[2]/input')
    search.click()
    time.sleep(1)
    opt =driver.find_element_by_xpath('//*[@id="main"]/div[1]/main/div[1]/section/div/div/div/form/div/div/div/div[1]/div/div/div[4]/div[2]/div')
    opt.click()
    time.sleep(1)
    opt =driver.find_element_by_xpath('//*[@id="main"]/div[1]/main/div[1]/section/div/div/div/form/div/button')
    opt.click()
    time.sleep(3)
    # name =driver.find_element_by_xpath('//*[@id="main"]/div/main/div/div[2]/div/div[2]/div/div/section/article[2]/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/a')
    # print(name.text)
    names = driver.find_elements_by_class_name('cmGgZN')
    practitioner = driver.find_elements_by_class_name('jyfAkd')
    rating = driver.find_elements_by_class_name('dWnIDu')
    count_rating = driver.find_elements_by_class_name('ehwwpF')
    next = driver.find_element_by_xpath('//*[@id="main"]/div/main/div/nav/span[2]/a')
    # //*[@id="main"]/div/main/div/nav/span[3]/a
    for i in names:
        print(i.text)
    for i in practitioner:
        print(i.text)
    for i in rating:
        print(i.text)
    for i in count_rating:
        print(i.text)
    # //*[@id="main"]/div/main/div/div[2]/div/div[2]/div/div/section/article[3]/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/a
except Exception as e:
    pass
time.sleep(5)
driver.close()
driver.quit()