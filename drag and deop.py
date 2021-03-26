from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get('https://demoqa.com/droppable')
driver.maximize_window()
time.sleep(2)

#drag and drop operation,
source=driver.find_element_by_xpath('//*[@id="draggable"]')
target=driver.find_element_by_xpath('//*[@id="droppable"]')
actions=ActionChains(driver)
actions.drag_and_drop(source,target).perform()