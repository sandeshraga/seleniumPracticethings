from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get('https://www.facebook.com/')

user_ele= driver.find_element_by_name("email")
print(user_ele.is_displayed())#returns true/False
print(user_ele.is_enabled())#returns true/false
user_ele.send_keys("sandeshraga@gmail.com")

user_ele= driver.find_element_by_name("pass")
print(user_ele.is_displayed())#returns true/false
print(user_ele.is_enabled())#returns true/false
user_ele.send_keys("Aryaarya@3369@")

driver.find_element_by_name('login').click()


