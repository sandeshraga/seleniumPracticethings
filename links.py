from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get('https://artoftesting.com/samplesiteforselenium')
driver.implicitly_wait(5)

#to find total no.of links present in page
links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))
#to print all links
for link in links:
    print(link.text)
#to select on particular link
driver.find_element(By.LINK_TEXT,"Selenium Sample Script").click()

#driver.find_element(By.PARTIAL_LINK_TEXT, 'Selenium').click()