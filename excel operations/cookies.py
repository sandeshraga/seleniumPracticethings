import XLutilsfile
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/")

#to capture all cookies present in the web browser
coockies=driver.get_cookies()
#total no. of cookies
print(len(coockies))

#to print all cookies
print(coockies)

#adding new coocki to the browser
cookie={'name':'mycookies', 'value':'12345678'}
driver.add_cookie(cookie)

#result after adding
coockies=driver.get_cookies()
print(len(coockies))
print(coockies)

#deleting cookie
driver.delete_cookie('mycookies')
#result after deleting
coockies=driver.get_cookies()
print(len(coockies))
print(coockies)

#deleting all cookies from the browser
driver.delete_all_cookies()
coockies=driver.get_cookies()
print(len(coockies))

