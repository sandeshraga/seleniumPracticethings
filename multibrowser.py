from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Ie(executable_path="C:\Drivers\IEDriverServer_Win32_3.150.1\IEDriverServer")
driver.get("https://www.tutorialspoint.com/string-slicing-in-python-to-rotate-a-string")
print(driver.title)
print(driver.current_url)
driver.close()