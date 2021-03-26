from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.maximize_window()
time.sleep(2)
#right click operation
element=driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')
action=ActionChains(driver)
action.context_click(element).perform()