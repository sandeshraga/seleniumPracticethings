from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()


driver.find_element_by_css_selector('input[type="search"]').send_keys("ber")#search option
time.sleep(2)

products=driver.find_elements_by_xpath("//div[@class='products']/div")#number of products displayed on page
print(len(products))

buttons=driver.find_elements_by_xpath("//div[@class='product-action']/button")#TO add each product to cart
for button in buttons:
    button.click()
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()#proceed to checkout

wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print(driver.find_element_by_css_selector("span.promoInfo").text)

