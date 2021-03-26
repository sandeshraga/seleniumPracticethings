
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/")

#to take screenshot in any formats, png or jpg etc..
driver.save_screenshot("D:\Study material\MS\selenium testing codes\screen shots\homepage.jpg")
#to get screenshot only in png format
driver.get_screenshot_as_file("D:\Study material\MS\selenium testing codes\screen shots\homepage2.png")

