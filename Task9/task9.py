from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd
# Procedure/surgery name , Cost , Total days , Top hospitals, Top doctors
doc_name = []
hopsital = []
days = []
cost = []
surger_name = []
PATH = r'chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.vaidam.com/cost/24-hour-holter-monitoring-cost-in-india')
dev = driver.title
print(dev)
procedure = driver.find_element_by_class_name('title')
price = driver.find_element_by_xpath('//*[@id="treatment-cost"]/div/div/div/div[2]/div/table/tbody/tr/td[1]/span[2]')
tdays = driver.find_element_by_xpath('//*[@id="treatment-cost"]/div/div/div/div[2]/div/table/tbody/tr/td[5]/span[2]')
print(procedure.text)
print(price.text)
print(tdays.text)
for i in range(4):
    name = driver.find_element_by_xpath('//*[@id="top-doctors"]/div/div/div[2]/div['+str(i+1)+']/div[2]/h3/a')
    spec = driver.find_element_by_xpath('//*[@id="top-doctors"]/div/div/div[2]/div['+str(i+1)+']/div[2]/p[1]')
    exp_loc = driver.find_element_by_xpath('//*[@id="top-doctors"]/div/div/div[2]/div['+str(i+1)+']/div[2]/p[2]')
    hosp = driver.find_element_by_xpath('//*[@id="top-hospitals"]/div/div/div[2]/div['+str(i+1)+']/div[2]/h3/a')
    # print(name.text)
    print(spec.text)
    print(exp_loc.text)
    print(hosp.text)
    doc_name.append(name.text)
    hopsital.append(hosp.text)
    days.append(tdays.text)
    cost.append(price.text)
    surger_name.append(procedure.text)

time.sleep(5)
driver.close()
driver.quit()
df = pd.DataFrame({
    'Surgery Name': surger_name,
    'Cost': cost,
    'Total Days':days,
    'Top Hospital':hopsital,
    'Top Doctor': doc_name
})
df.to_csv('demo.csv')



# //*[@id="top-doctors"]/div/div/div[2]/div[1]/div[2]/h3/a
# //*[@id="top-doctors"]/div/div/div[2]/div[2]/div[2]/h3/a

# //*[@id="top-doctors"]/div/div/div[2]/div[2]/div[2]/p[1]

# //*[@id="top-doctors"]/div/div/div[2]/div[2]/div[2]/p[2]