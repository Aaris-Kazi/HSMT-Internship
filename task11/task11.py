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
url = 'https://self-checks.mfine.co/s/Self-Check-for-Breast-Cancer/tt-9f6b41?&channel=website&utm_source=landingpage&utm_medium=banner&utm_campaign=breastcancer'
driver.get(url)
i = 0
time.sleep(9)
driver.execute_script("window.scrollTo(0, 10)") 
continue_button = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
continue_button.click()
def automate():
    ques, multiple = [], []
    global i
    
    time.sleep(5)
    options1 = driver.find_elements_by_class_name('ss-chat__item-title')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    time.sleep(2)
    options1[1].click()
    time.sleep(9)
# 1
    options1 = driver.find_elements_by_class_name('ss-chat__item-title')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    options1[1].click()
    time.sleep(1)
    next = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    next.click()
    time.sleep(9)
# 2
 
    options1 = driver.find_elements_by_class_name('ss-chat__item-title')
    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    op1.click()
    time.sleep(1)
    next = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    next.click()
# 3
    time.sleep(9)

 
    options1 = driver.find_elements_by_class_name('ss-chat__item-title')
    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    op1.click()
    # time.sleep(1)
    # next = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    # next.click()
# 4
    time.sleep(9)

 
    options1 = driver.find_elements_by_class_name('ss-chat__item-title')
    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    op1.click()
    time.sleep(1)
    next = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    next.click()
# 5
    time.sleep(9)

 
    options1 = driver.find_elements_by_class_name('ss-chat__item-title')
    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    op1.click()
    # time.sleep(1)
    # next = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    # next.click()
# 6
    time.sleep(9)

 
    options1 = driver.find_elements_by_class_name('ss-chat__item-title')
    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    op1.click()
    # time.sleep(1)
    # next = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    # next.click()
# 7
    time.sleep(9)

 
    options1 = driver.find_elements_by_class_name('ss-chat__item-title')
    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    op1.click()
    # time.sleep(1)
    # next = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    # next.click()
# 8
    time.sleep(9)

 
    options1 = driver.find_elements_by_class_name('ss-chat__item-title')
    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    op1.click()
    # time.sleep(1)
    # next = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    # next.click()
# 9

    time.sleep(9)
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    # options1[2].click()
    op1.click()
    time.sleep(7)
# 10

    
    time.sleep(9)

 
    options1 = driver.find_elements_by_class_name('ss-chat__item-title')
    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    op1.click()
    # time.sleep(1)
    # next = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    # next.click()
# 11
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    op1.click()
    
# 12 
    time.sleep(9)
    # //*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]
    options1 = driver.find_elements_by_class_name('ss-chat__item-title')
    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    op1.click()

# 13
    time.sleep(9)

    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    op1.click()
    # next = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    # next.click()
# 14
    time.sleep(9)

    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    options1 = driver.find_elements_by_class_name('ss-chat__item-title')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    op1.click()
# 15
    time.sleep(9)

    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    op1.click()
    # next = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    # next.click()
# 16
    time.sleep(9)

    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    op1.click()
    # next = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    # next.click()
# 17
    time.sleep(9)

    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]')
    options1 = driver.find_elements_by_class_name('ss-chat-multiple-choice__item')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    op1.click()
    
# 18
    time.sleep(9)

    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]/div[2]')
    options1 = driver.find_elements_by_class_name('ss-chat__item-title')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    op1.click()
    # time.sleep(1)
    # next = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    # next.click()
# 19
    time.sleep(9)

    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]/div[2]')
    options1 = driver.find_elements_by_class_name('ss-chat__item-title')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    op1.click()
    # time.sleep(1)
    # time.sleep(1)
    # next = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    # next.click()
# 20
    time.sleep(9)

    op1 = driver.find_element_by_xpath('//*[@id="surveysparrow-chat__scroll-container"]/div/div[4]/div[1]/div[1]/div[2]')
    options1 = driver.find_elements_by_class_name('ss-chat__item-title')
    texting = ''
    for j in options1:
        print(j.text)
        temp = j.text
        texting = texting+temp+', '
    multiple.append(texting)
    i= i+1
    print(i)
    # op1.click()
    # time.sleep(1)
    # time.sleep(1)
    # next = driver.find_element_by_class_name('surveysparrow-chat__btn-default.surveysparrow-chat__btn--primary.ss-background-color--answer.ss-text-color--answer-invert.ss-border-color--answer.ss-survey-text-size--sm.ss-survey-line-height--tight.ss-survey-text-weight--medium')
    # next.click()
# 21
    
    question = driver.find_elements_by_tag_name('strong')
    for k in question:
        ques.append(k.text)
        print(k.text)
    # op1.click()
    df = pd.DataFrame({
    "Questions": ques,
    # "Options": multiple,
    })
    sf = pd.DataFrame({
    # "Questions": ques,
    "Options": multiple,
    })
    df.to_csv('chat1.csv')
    sf.to_csv('chat.csv')
automate()
time.sleep(5)
driver.close()
driver.quit()