import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def Google_test(self):
        self.driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print(self.driver.title)
        self.driver.close()

    def IE_test(self):
        self.driver=webdriver.Ie(executable_path="C:\Drivers\IEDriverServer_Win32_3.150.1\IEDriverServer.exe")
        self.driver.get("https://www.google.com/")
        print(self.driver.title)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()