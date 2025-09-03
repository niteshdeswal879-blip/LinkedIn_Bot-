from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import time, sleep

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4237412182&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

sleep(3)

sign=driver.find_element(by=By.XPATH,value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign.click()

sleep(2)
email=driver.find_element(By.ID, "base-sign-in-modal_session_key")
email.send_keys("serinox65@gmail.com",Keys.ENTER)

password=driver.find_element(By.ID, value="base-sign-in-modal_session_password")
password.send_keys("Serinox@65now",Keys.ENTER)




sleep(9)



jobs=driver.find_elements(By.CSS_SELECTOR, 'li.scaffold-layout__list-item')
for i in jobs:
    try:
        i.click()
        sleep(2)
        try:
            save = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button__text")
            save.click()

        except NoSuchElementException:
            saved= driver.find_element(By.CSS_SELECTOR, value=".jobs-saved-button__text")

    except NoSuchElementException:
        print("No such element found")

