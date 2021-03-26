from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://github.com/login")
driver.maximize_window()
time.sleep(2)

driver.find_element_by_id("login_field").send_keys('sandeshragashetty22@gmail.com')
driver.find_element_by_id("password").send_keys('Unicorn@2020#')
driver.find_element_by_name("commit").click()
print(driver.title)