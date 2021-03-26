from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
time.sleep(2)

# example of mouse hover, but this code is not working try other
actions=ActionChains(driver)
menu=driver.find_element_by_id("mousehover")
actions.move_to_element(menu).perform()
childmenu=driver.find_element_by_link_text("Top")
actions.move_to_element(childmenu).click().perform()
