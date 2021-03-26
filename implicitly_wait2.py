from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)


driver.find_element_by_css_selector('input[type="search"]').send_keys("ber")#search option
time.sleep(2)

products=driver.find_elements_by_xpath("//div[@class='products']/div")#number of products displayed on page
print(len(products))


buttons=driver.find_elements_by_xpath("//div[@class='product-action']/button")#TO add each product to cart
#//div[@class='product-action']/button/parent::div/parent::div/h4  -----this is x path for traversing from child to grand parent and again coming back
#to another child
list1=[]
for button in buttons:
    list1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list1)


driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()#proceed to checkout


list2=[]
veggies=driver.find_elements_by_css_selector("p.product-name")
for veg in veggies:
    list2.append(veg.text)
print(list2)

#to verify discount amount is less than final amount
originalamount = driver.find_element_by_css_selector("span.discountAmt").text
print(originalamount)

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()

time.sleep(5)
finalamount = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/span[3]').text
print(finalamount)
assert (float(finalamount) < int(originalamount))

#to verify total sum and shown value are correct
amounts=driver.find_elements_by_xpath("//tbody/tr/td[5]")
sum=0
for amount in amounts:
    sum=sum+int(amount.text)
print(sum)

final_amount=int(driver.find_element_by_css_selector("span.totAmt").text)
assert final_amount ==sum