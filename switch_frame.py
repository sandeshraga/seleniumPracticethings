from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get('https://demoqa.com/frames')
driver.maximize_window()
time.sleep(2)
driver.switch_to.frame('frame1')
time.sleep(3)
driver.switch_to.default_content()
time.sleep(2)
driver.switch_to.frame("frame2")
time.sleep(3)
driver.quit()