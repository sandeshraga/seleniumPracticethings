from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.get("https://www.facebook.com/") #opening Url takes some time
driver.implicitly_wait(10)# wait for 10 seconds until page loads completely or if page loads within 10 secs it proceed further
assert "Facebook – log in or sign up" in driver.title #checks condition, if true then executes next


driver.find_element_by_name("email").send_keys("sandeshraga@gmail.com")
driver.find_element_by_name("pass").send_keys("Aryaarya@3369@")
driver.find_element_by_name("login").click()