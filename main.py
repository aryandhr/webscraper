import random
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

url = "url"

coordinates = dict({"latitude": 3.1415927, "longitude": -2.7182818, "accuracy": 100})

driver = webdriver.Chrome()
driver.execute_cdp_cmd("Emulation.setGeolocationOverride", coordinates)
driver.get(url)

email_element = driver.find_element("xpath", '//*[@id="userEmail"]')
pass_element = driver.find_element("xpath", '//*[@id="userPassword"]')
email_element.send_keys("email")
pass_element.send_keys("password")
pass_element.send_keys(Keys.RETURN)

time.sleep(5)

cem_element = driver.find_element("xpath", '/html/body/div/div[2]/div/div/div/main/div[3]/ul[1]/li[1]/a')
cem_element.click()

time.sleep(7)

join_element = driver.find_element("xpath", '//*[@id="btnJoin"]')
join_element.click()

time.sleep(3)

while True:
    try:
        answer_a = driver.find_element("xpath", '//*[@id="multiple-choice-a"]')
        answer_b = driver.find_element("xpath", '//*[@id="multiple-choice-b"]')
        answer_c = driver.find_element("xpath", '//*[@id="multiple-choice-c"]')

        answers = [answer_a, answer_b, answer_c]

        answer = random.choice(answers)
        answer.click()
        time.sleep(5)

    except (StaleElementReferenceException, NoSuchElementException):
        time.sleep(5)
