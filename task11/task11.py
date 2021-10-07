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
url = 'https://self-checks.mfine.co/s/Self-Check-for-COVID-19/tt-bf9bab?channel=website&utm_source=landingpage&utm_medium=banner&utm_campaign=covidnew'
driver.get(url)
driver.execute_script("window.scrollTo(0, 10)") 
time.sleep(10)
continue_button = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
continue_button.click()
def automate():
    continue_button1 = driver.find_element_by_class_name('surveysparrow-chat__question-text.ss-survey-text-align--left.ss-survey-text-size--sm.ss-survey-line-height--normal.ss-survey-text-weight--regular.ss-text-color--question')
    print(continue_button1.text)
    time.sleep(1)
    options1 = driver.find_elements_by_class_name('ss-chat__item-title')
    for j in options1:
        print(j.text)
    question = driver.find_elements_by_tag_name('strong')
    for k in question:
        print('strong')
        print(k.text)
    time.sleep(2)
    options1[1].click()
    time.sleep(9)
    continue_button2 = driver.find_element_by_class_name('ss-chat-row__bubble')
    print(continue_button2.text)
    time.sleep(1)
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    for j in options1:
        print(j.text)
    time.sleep(2)
    options1[1].click()
    time.sleep(1)
    question = driver.find_elements_by_tag_name('strong')
    for k in question:
        print('strong')
        print(k.text)
    next = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    next.click()
    time.sleep(3)
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    for j in options1:
        print(j.text)
    options1[2].click()
    time.sleep(1)
    question = driver.find_elements_by_tag_name('strong')
    for k in question:
        print('strong')
        print(k.text)
    time.sleep(3)
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    for j in options1:
        print(j.text)
    options1[2].click()
    time.sleep(1)
    question = driver.find_elements_by_tag_name('strong')
    for k in question:
        print('strong')
        print(k.text)
    time.sleep(3)
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--regular.ss-text-color--question.ss-border-color--answer.ss-highlight-answer.ss-chat-rounded-border.ss-chat-multiple-choice__item')
    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    for j in options1:
        print(j.text)
    time.sleep(2)
    driver.execute_script("arguments[0].click();", options1[1])
    driver.execute_script("arguments[0].click();", op1)
    # options1[1].click()
    # op1.click()

    # options1[2].click()
    time.sleep(1)
    question = driver.find_elements_by_tag_name('strong')
    for k in question:
        print('strong')
        print(k.text)
    
automate()
time.sleep(5)
driver.close()
driver.quit()