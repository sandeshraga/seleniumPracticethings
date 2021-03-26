from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get('https://demoqa.com/alerts')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="confirmButton"]').click()
time.sleep(5)
#it deselect the popup button

driver.switch_to().alert().dismiss()
#it selects the popup 
driver.switch_to().alert().accept()