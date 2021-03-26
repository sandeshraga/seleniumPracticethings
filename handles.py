from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get('https://demoqa.com/automation-practice-form')
driver.maximize_window()
time.sleep(2)

#to upload picture
driver.find_element_by_id('uploadPicture').send_keys('E:/KLE days/R S/2017-06-29-12-08-31-998.jpg')