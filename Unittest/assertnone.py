import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def assert_test(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.assertIsNone(driver)#false
        self.assertIsNotNone(driver)#True


if __name__ == "__main__":
    unittest.main()

