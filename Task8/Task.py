from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd

def page(i):
    PATH = r'Task1\chromedriver.exe'
    driver = webdriver.Chrome(PATH)

    driver.get('https://www.justdial.com/Surat/Multispeciality-Hospitals/nct-10547585/page-'+str(i+1)+'')
    dev = driver.title
    print(dev)
    driver.close()
    driver.quit()

def main():
    for i in range(10):
        page(i)

if __name__ == '__main__':
    main()