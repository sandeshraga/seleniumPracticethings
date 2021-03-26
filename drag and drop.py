from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get('https://www.globalsqa.com/demo-site/draganddrop/')
driver.maximize_window()
time.sleep(2)

#drag and drop operation,it is not working try other
source=driver.find_element_by_xpath('//*[@id="gallery"]/li[1]')
target=driver.find_element_by_xpath('//*[@id="trash"]')
actions=ActionChains(driver)
actions.drag_and_drop(source,target).perform()