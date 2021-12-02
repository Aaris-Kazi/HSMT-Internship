from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

name, designation, rate, rate_count = [],[],[],[]
PATH = 'chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(PATH, options=options)

url = 'https://www.zocdoc.com/'
driver.get(url)
def looping():
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
    print(len(name),len(designation),len(rate),len(rate_count))

search =driver.find_element_by_xpath('//*[@id="main"]/div[1]/main/div[1]/section/div/div/div/form/div/div/div/div[1]/div/div/div[2]/input')
search.click()
time.sleep(1)
opt =driver.find_element_by_xpath('//*[@id="main"]/div[1]/main/div[1]/section/div/div/div/form/div/div/div/div[1]/div/div/div[4]/div[3]/div')
# //*[@id="main"]/div[1]/main/div[1]/section/div/div/div/form/div/div/div/div[1]/div/div/div[4]/div[3]
opt.click()
time.sleep(1)
opt =driver.find_element_by_xpath('//*[@id="main"]/div[1]/main/div[1]/section/div/div/div/form/div/button')
opt.click()
time.sleep(3)
for i in range(2,10):
    time.sleep(5)
    looping()
    time.sleep(1)
    next = driver.find_element_by_xpath('//*[@id="main"]/div/main/div/nav/span['+str(i)+']/a')
    next.click()
    # print(len(name),len(designation),len(rate),len(rate_count))
    # //*[@id="main"]/div/main/div/nav/span[3]/a
    # //*[@id="main"]/div/main/div/nav/span[2]/a
time.sleep(5)
driver.close()
driver.quit()

df = pd.DataFrame({
    "Name": name,
    "Practitioner": designation,
    "Ratings": rate,
    "Raring Counts": rate_count,
})
df.to_csv('zocdoc_aaris.csv', header = False, mode='a')