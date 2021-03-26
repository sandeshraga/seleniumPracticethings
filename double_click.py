from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get('https://www.w3schools.com/html/html_basic.asp')
driver.maximize_window()
time.sleep(2)
#double click operation
element=driver.find_element_by_xpath('/html/body/div[1]/a')
action=ActionChains(driver)
action.double_click(element).perform()