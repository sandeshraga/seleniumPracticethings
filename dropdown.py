from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get('https://demoqa.com/automation-practice-form')

#to give input to the boxes
driver.find_element_by_id("firstName").send_keys("sandesh")
time.sleep(1)
driver.find_element_by_id("lastName").send_keys('Ragashetti')

#to check radio box is selected or not
radio_box = driver.find_element_by_id('gender-radio-1').is_selected()
print(radio_box)# returns True/False

#to select radio box
driver.find_element_by_id('gender-radio-1').click()

time.sleep(5)
#to count No.of input_boxes
#inputboxes= driver.find_elements_by_class_name('mr-sm-2 form-control')
#print(len(inputboxes))

#to select check boxes
driver.find_element_by_id('hobbies-checkbox-1').click()
time.sleep(2)
driver.find_element_by_id('hobbies-checkbox-2').click()

#to select options from dropdown menu
element = driver.find_element_by_xpath('//*[@id="state"]')
drp=Select(element)
#3 methods are there
#element.select_by_visible_text('Haryana')#1st method
#element.select_by_index(2)
#select by value

#to count the No. of dropdown options
all_options=drp.options
print(len(all_options))

#to print all options
for option in all_options:
    print(option.text)