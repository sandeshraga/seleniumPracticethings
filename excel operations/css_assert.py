import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element_by_id("autosuggest").send_keys("India")
time.sleep(2)
countries= driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    print(country.text)
    if country.text == "India":
        country.click()
        break
print(driver.find_element_by_id("autosuggest").text)
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"








