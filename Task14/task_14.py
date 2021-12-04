from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

spec = input('Enter Specialist:-')
loc = input('Enter Location:-')

name, designation, rate, rate_count = [],[],[],[]
PATH = 'chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(PATH, options=options)

def looping():
    time.sleep(5)
    names = driver.find_elements_by_class_name('cmGgZN')
    practitioner = driver.find_elements_by_class_name('jyfAkd')
    rating = driver.find_elements_by_class_name('dWnIDu')
    count_rating = driver.find_elements_by_class_name('ehwwpF')
    for a,b,c,d in zip(names, practitioner, rating, count_rating):
        name.append(a.text)
        designation.append(b.text)
        rate.append(c.text)
        rate_count.append(d.text)
        print(a.text)
        print(c.text)
        
    print(len(name),len(designation),len(rate),len(rate_count))
    time.sleep(2)
    # next = driver.find_element_by_xpath('//*[@id="main"]/div/main/div/nav/span['+str(i)+']/a')
    # next.click()



url = 'https://www.zocdoc.com/'
driver.get(url)
time.sleep(1)
search =driver.find_element_by_xpath('//*[@id="main"]/div[1]/main/div[1]/section/div/div/div/form/div/div/div/div[1]/div/div/div[2]/input')
search.click()
search.send_keys(spec)
time.sleep(3)
opt =driver.find_element_by_xpath('//*[@id="main"]/div[1]/main/div[1]/section/div/div/div/form/div/div/div/div[1]/div/div/div[4]/div[1]')
opt.click()
button =driver.find_element_by_xpath('//*[@id="main"]/div[1]/main/div[1]/section/div/div/div/form/div/div/div/div[3]/div/div[2]/div/div[1]/input')
button.click()
button.send_keys(loc)
time.sleep(3)
opt =driver.find_element_by_xpath('//*[@id="main"]/div[1]/main/div[1]/section/div/div/div/form/div/div/div/div[3]/div/div[2]/div[2]/div/div[1]')
opt.click()
search1 =driver.find_element_by_xpath('//*[@id="main"]/div[1]/main/div[1]/section/div/div/div/form/div/button')
search1.click()
time.sleep(3)
driver.execute_script("window.scrollTo(0, 150)") 
looping()
time.sleep(2)
driver.close()
driver.quit()