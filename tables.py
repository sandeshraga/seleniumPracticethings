from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get('https://www.w3schools.com/html/html_tables.asp')
driver.maximize_window()
time.sleep(2)

rows=len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr'))
print(rows)

columns=len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr[1]/th'))
print(columns)
print("company"+"                          "+"contact"+"        "+"country")
for r in range(2,rows+1):
    for c in range(1, columns+1):
        value=driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr['+str(r)+']/td['+str(c)+']').text
        print(value, end="          ")
    print()

