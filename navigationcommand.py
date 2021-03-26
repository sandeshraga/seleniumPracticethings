#navigation Commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.tutorialspoint.com/string-slicing-in-python-to-rotate-a-string")
time.sleep(5)
print(driver.title)

driver.get("https://www.w3schools.com/")
time.sleep(5)
print(driver.title)

driver.back()#it goes back to previous web page
print(driver.title)
time.sleep(2)

driver.forward()#it opens next page
print(driver.title)
time.sleep(2)

driver.close()