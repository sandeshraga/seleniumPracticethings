from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#chrome browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe") # it invokes chrome webdriver .exe file
driver.get('https://www.w3schools.com/') #it opens respective webpage in chrome browser

print(driver.title) #it fetches title of the page in respective webpage
print(driver.current_url) #it gives url
driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/a[1]').click() #it clicks on button and opens another page through X path
time.sleep(5)
driver.close()# close all webpages and browser