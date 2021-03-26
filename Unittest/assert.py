import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def assert_test(self):
        print("hello")
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.amazon.in/")

        title1 = driver.title
        print(title1)
        self.assertEqual("Google", title1, "hiinkjsacdsk")
        self.assertNotEqual("Google123",title1)


if __name__ == "__main__":
    unittest.main()

