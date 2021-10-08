from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
ques = []
PATH = 'chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(PATH, options=options)
url = 'https://self-checks.mfine.co/s/Self-Check-for-COVID-19/tt-bf9bab?channel=website&utm_source=landingpage&utm_medium=banner&utm_campaign=covidnew'
driver.get(url)
try:
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 10)") 
    time.sleep(10)
    continue_button = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    continue_button.click()
    time.sleep(3)
    options1 = driver.find_elements_by_class_name('ss-chat__item-title')
    for j in options1:
        print(j.text)
    question = driver.find_elements_by_tag_name('strong')
    for k in question:
        print('strong')
        print(k.text)
    options1[1].click()

    time.sleep(5)
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    for j in options1:
        print(j.text)
    options1[1].click()
    time.sleep(1)
    next = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    next.click()
    time.sleep(5)

    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    for j in options1:
        print(j.text)
    options1[1].click()
    time.sleep(5)

    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    for j in options1:
        print(j.text)
    driver.execute_script("arguments[0].click();", op1)
    time.sleep(5)

    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    for j in options1:
        print(j.text)
    driver.execute_script("arguments[0].click();", op1)
    time.sleep(5)

    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    for j in options1:
        print(j.text)
    driver.execute_script("arguments[0].click();", op1)
    time.sleep(5)

    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    for j in options1:
        print(j.text)
    driver.execute_script("arguments[0].click();", op1)
    time.sleep(5)

    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    for j in options1:
        print(j.text)
    driver.execute_script("arguments[0].click();", op1)
    time.sleep(5)

    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    for j in options1:
        print(j.text)
    driver.execute_script("arguments[0].click();", op1)
    time.sleep(5)

    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    for j in options1:
        print(j.text)
    driver.execute_script("arguments[0].click();", op1)
    time.sleep(5)

    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    for j in options1:
        print(j.text)
    driver.execute_script("arguments[0].click();", op1)
    time.sleep(6)

    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    for j in options1:
        print(j.text)
    driver.execute_script("arguments[0].click();", op1)
    time.sleep(5)

    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    for j in options1:
        print(j.text)
    driver.execute_script("arguments[0].click();", op1)
    
    question = driver.find_elements_by_tag_name('strong')
    for k in question:
        ques.append(k.text)
        print(k.text)
except Exception:
    pass
df = pd.DataFrame({
    "Questions": ques
})
df.to_csv('chat.csv')
time.sleep(5)
driver.close()
driver.quit()