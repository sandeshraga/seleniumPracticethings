from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get('https://www.w3schools.com/default.asp')
driver.maximize_window()
time.sleep(2)

#to scroll down the page by pixel
driver.execute_script("window.scrollBy(0,1000)"," ")

#scroll down the page till element found
css=driver.find_element_by_xpath('//*[@id="main"]/div[9]/div[1]/div[2]')
driver.execute_script("arguments[0].scrollIntoView();", css)

#scroll down till end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")