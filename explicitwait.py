from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.expedia.co.in/") #opening Url takes some time

driver.find_element_by_xpath('//*[@id="uitk-tabs-button-container"]/li[2]/a').click()

driver.find_element_by_xpath('//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[1]/div/div[1]').clear()

driver.find_element_by_xpath('//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[1]/div/div[1]').send_keys("Bengaluru")
time.sleep(2)

driver.find_element_by_xpath('//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[1]/div/div[2]/div/div/div/button').clear()
driver.find_element_by_xpath('//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[1]/div/div[2]/div/div/div/button').send_keys("Dublin")
time.sleep(2)

driver.find_element_by_id('d1-btn').send_keys('17 Feb')
driver.find_element_by_id('d2-btn').send_keys('19 Feb')

driver.find_element_by_xpath('//*[@id="wizard-flight-pwa-1"]/div[3]/div[2]').click()

#expicit_wait
wait=WebDriverWait(driver,10)
element=wait.until(EC.element_to_be_clickable((By.NAME,"fa0")))
element.click()

time.sleep(5)
driver.quit()
